import collections
import html
import isort
import black
from io import StringIO
from pathlib import Path
from typing import Any, Dict, List, Optional, OrderedDict, Tuple, Type

from buildtools.indentation import IndentWriter

PATH_STRUCTS: Path = Path('data') / 'def-structs'
PATH_PYDEFS: Path = Path('devtools') / 'rim4py' / 'defs'

FIELD_TYPES: Dict[str, Type['BaseDefField']] = {}
class BaseDefField:
    TYPEID: str = ''
    TYPEDEF: str = ''
    IMPORTS: List[str] = []

    def __init__(self, 
        name: Optional[str] = None,
        optional: Optional[str] = None,
        default: Optional[Any] = None,
        help: Optional[List[str]] = None,
        xml_name: Optional[str] = None
    ) -> None:
        self.name: str = name or ''
        self.optional: bool = optional or False
        self.default: Optional[Any] = default
        self.help: List[str] = help or []
        self.xml_name: str = xml_name or name or ''

    def deserialize(self, k: str, data: Dict[str, Any]) -> None:
        self.name = k
        self.optional = data.get('optional', False)
        self.default = data.get('default')
        self.help = data.get('help')
        self.xml_name = data.get('xml-name') or self.name

    def generateImports(self, w: IndentWriter) -> None:
        '''Spit out imports'''
        if self.optional:
            w.writeline('from typing import Optional')
        for l in self.IMPORTS:
            w.writeline(l)

    def generateInitCode(self, w: IndentWriter) -> None:
        '''What to write in def __init__.'''
        td = self.TYPEDEF
        if self.optional:
            td = f'Optional[{td}]'
        w.writeline(f'self.{self.name}: {td} = {self.default}')

    def generateFromDef(self, w: IndentWriter) -> None:
        '''The actual Def XML deserialization code'''
        with w.writeline(f'if (ie := element.find({self.xml_name!r})) is not None:'):
            self.generateInnerDeserializeFromElement(w, 'ie')
        with w.writeline(f'else:'):
            if self.optional:
                self.generateInnerAssignNull(w)
            else:
                w.writeline(f'raise new MissingElementException(tree.getpath(element), {self.xml_name!r})')

    def generateInnerDeserializeFromElement(self, w: IndentWriter, inner_element_var: str) -> None:
        pass

    def generateInnerAssignNull(self, w: IndentWriter) -> None:
        w.writeline(f'self.{self.name} = None')

    def generateToDefElementTextCode(self) -> str:
        return f'str(self.{self.name})'

    def generateToDefInjectable(self, w: IndentWriter, parent_element: str) -> None:
        '''<{defname}.{fieldname}>'''
        defid: str = f'f\'{{self.defName}}.{self.xml_name}\''
        contents: str = f'html.escape({self.generateToDefElementTextCode()})'
        w.writeline(f'etree.SubElement({parent_element}, {defid!r}, {{}}, {contents})')

class DefStrField(BaseDefField):
    TYPEID = 'str'
    TYPEDEF = 'str'
    IMPORTS = []

    def generateInnerDeserializeFromElement(self, w: IndentWriter, inner_element_var: str) -> None:
        w.writeline(f'self.{self.name} = {inner_element_var}.text')
FIELD_TYPES[DefStrField.TYPEID] = DefStrField

class DefIntField(BaseDefField):
    TYPEID = 'int'
    TYPEDEF = 'int'
    IMPORTS = []

    def generateInnerDeserializeFromElement(self, w: IndentWriter, inner_element_var: str) -> None:
        w.writeline(f'self.{self.name} = int({inner_element_var}.text)')
FIELD_TYPES[DefIntField.TYPEID] = DefIntField

class DefMeta:
    def __init__(self) -> None:
        self.type: str = ''
        self.fields: OrderedDict[str, BaseDefField] = collections.OrderedDict()

    def fromYAML(self, data: Dict[str, Any]) -> None:
        self.type = data['type']
        for k,v in data['fields'].items():
            fld = FIELD_TYPES[v['type']]()
            fld.deserialize(k, v)
            self.fields[fld.name] = fld

    def toPython(self, w: IndentWriter) -> None:
        #w.writeline('# @generated by gen_rim4py_defs.py - DO NOT EDIT BY HAND')
        w.writeline('import html')
        w.writeline('from lxml import etree')
        w.writeline('from rim4py.defs.def import Def')
        [x.generateImports(w) for x in self.fields.values()]
        with w.writeline(f'class {self.type}(Def):'):
            w.writeline(f'TAG: str = {self.type!r}')
            with w.writeline(f'def __init__(self) -> None:'):
                [x.generateInitCode(w) for x in self.fields.values()]
            with w.writeline(f'def fromDefElement(self, element: etree._Element) -> None:'):
                [x.generateFromDef(w) for x in self.fields.values()]
            with w.writeline(f'def toDefInjectElement(self, element: etree._Element) -> None:'):
                [x.generateToDefInjectable(w, 'element') for x in self.fields.values()]

def main():
    defs: List[Tuple[str, str]] = []
    for path in PATH_STRUCTS.glob('*.yml'):
        print(f'{path}...', end='')
        with path.open('r') as f:
            data = YAML.load(f)
        def_ = DefMeta()
        def_.fromYAML(data)
        intermediate = ''
        with StringIO() as f:
            w = IndentWriter(f)
            def_.toPython(w)
            intermediate = f.getvalue()
        intermediate = isort.code(intermediate)
        intermediate = black.format_str(intermediate, mode=black.Mode())
        with (PATH_PYDEFS / f'{path.stem}.py').open('w') as f:
            genfile = Path(__file__).relative_to(Path.cwd())
            f.write(f'# @generated by {genfile} - DO NOT EDIT BY HAND\n')
            f.write(intermediate)
        defs.append((path.stem, def_.type))
        print(' DONE!')
    o: str = '''from typing import Dict, Type
from .def import Def
'''

    data = {}
    for stem, clsname in sorted(defs):
        o += f'from .{stem} import {clsname}\n'
        data[stem]=clsname
    o += f'DEF_TYPES: Dict[str, Type[Def]] = {data!r}\n'
    o = isort.code(o)
    o = black.format_str(o, mode=black.Mode())
    with (PATH_PYDEFS / '__init__.py').open('w') as f:
        f.write(o)
if __name__ == '__main__':
    main()