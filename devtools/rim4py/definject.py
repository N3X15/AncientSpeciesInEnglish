'''
DefInject file class
'''
from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List

from lxml import etree

ALL_LABELS: FrozenSet[str] = frozenset({'label', 'labelMechanoids', 'labelMale', 'labelFemale', 'labelShort', 'skillLabel', 'text',
          'rejectInputMessage', 'description', 'adjective', 'pawnLabel', 'gerundLabel', 'reportString', 'verb',
          'gerund', 'deathMessage', 'pawnsPlural', 'leaderTitle', 'jobString', 'quotation', 'beginLetterLabel',
          'beginLetter', 'recoveryMessage', 'baseInspectLine', 'graphLabelY', 'fixedName', 'letterLabel', 'letterText',
          'letterLabelEnemy', 'arrivalTextEnemy', 'letterLabelFriendly', 'arrivalTextFriendly', 'Description',
          'endMessage', 'successfullyRemovedHediffMessage', 'helpText'})
ALL_LIST_LABELS: FrozenSet[str] = frozenset({'helpTexts', 'comps', 'stages', 'degreeDatas', 'rulePack', 'lifeStages', 'scoreStages', 'verbs',
                   'hediffGivers', 'logRulesInitiator', 'logRulesRecipient', 'parts'})
LIST_SUBLABELS:FrozenSet[str] = frozenset({'label', 'description', 'labelTendedWell', 'labelTended', 'labelTendedWellInner', 'labelTendedInner',
              'labelSolidTendedWell', 'labelSolidTended', 'oldLabel', 'discoverLetterLabel', 'discoverLetterText',
              'letterLabel', 'letter', 'labelSocial', 'customLabel'})
ALL_NESTED_LABELS: FrozenSet[str] = frozenset({'rulesStrings'})

class BaseDefInjection:
    def __init__(self) -> None:
        pass

    def toXML(self, parent: etree._Element) -> None:
        pass

class ScalarDefInjection(BaseDefInjection):
    def __init__(self, val: str = '') -> None:
        self.value: str = val

    def toXML(self, parent: etree._Element) -> None:
        parent.text = self.value

class ListDefInjection(BaseDefInjection):
    def __init__(self, vals: List[str] = []) -> None:
        self.values: List[str] = vals

    def toXML(self, parent: etree._Element) -> None:
        for v in self.values:
            etree.SubElement(parent, 'li',{}).text = v

class DefInjectedFile:
    def __init__(self) -> None:
        self.defs: Dict[str, Dict[str, BaseDefInjection]] = {}

    def setEntryAsStr(self, defName: str, labelID: str, value: str) -> None:
        if defName not in self.defs:
            self.defs[defName] = {labelID: ScalarDefInjection(value)}
            return
        self.defs[defName][labelID] = ScalarDefInjection(value)

    def setEntryAsList(self, defName: str, labelID: str, values: Iterable[str]) -> None:
        for i, li in enumerate(values):
            self.setEntryAsStr(defName, f'{labelID}.{i}', li)

    def fromXML(self, root: etree._Element) -> None:
        e: etree._Element
        for e in root:
            self.defs[e.tag] = e.text
        
    def toXML(self, doc: etree._Element) -> None:
        for defName, defs in sorted(self.defs.items()):
            for k, v in sorted(defs.items()):
                e = etree.SubElement(doc, f'{defName}.{k}', {})
                v.toXML(e)

    def keyset(self) -> List[str]:
        return [str(x) for x in self.defs.keys()]

    @classmethod
    def FromFile(cls, path: Path) -> DefInjectedFile:
        doc: etree._ElementTree
        dif = DefInjectedFile()
        with path.open('rb') as f:
            doc = etree.parse(path)
        dif.fromXML(doc.getroot())
        return dif

    @classmethod
    def FromDef(cls, path: Path) -> DefInjectedFile:
        doc: etree._ElementTree
        le: etree._Element
        child: etree._Element

        dif = DefInjectedFile()
        
        doc = etree.parse(path)
        
        for child in doc.getroot().getiterator():
            #print(child)
            if etree.iselement(child) and str(child.tag).lower() == 'defname':
                defname = str(child.text)
                defel = child.getparent()
                # <ABC.label>...</ABC.label>
                for lblid in ALL_LABELS:
                    if (le := defel.find(lblid)) is not None and isinstance(le.text, str):
                        dif.setEntryAsStr(defname, lblid, le.text)
                # <ABC.label><li>...</li></ABC.label>
                for lblid in ALL_LIST_LABELS:
                    if (le := defel.find(lblid)) is not None:
                        # <ABC.label><li>...</li></ABC.label>
                        if (liList := le.findall('li')) is not None:
                            for i, li in enumerate(liList):
                                if len(list(li)) == 0:
                                    dif.setEntryAsStr(defname, f'{lblid}.{i}', li.text)
                                else:
                                    for slid in sorted(LIST_SUBLABELS):
                                        if (slie := li.find(slid)) is not None:
                                            dif.setEntryAsStr(defname, f'{lblid}.{i}.{slid}', slie.text)
                        else:
                            #<ABC.label><...><li>
                            for slid in ALL_NESTED_LABELS:
                                if (sl := le.findall(slid)) is not None:
                                    for i, li in enumerate(sl.findall('li')):
                                        dif.setEntryAsStr(defname, f'{lblid}.{slid}.{i}', li.text)
        return dif

    def save(self, path: Path, verbose: bool=False) -> None:
        print(f'Writing {len(self.defs):,} DefInjections to {path}...')
        tmppath = path.with_suffix(path.suffix+'~')
        tmppath.parent.mkdir(parents=True, exist_ok=True)
        el = etree.Element('LanguageData')
        tree = etree.ElementTree(el)
        self.toXML(tree.getroot())
        try:
            with tmppath.open('wb') as f:
                tree.write(f, pretty_print=True, encoding='utf-8', xml_declaration=True)
            os.replace(tmppath, path)
            print(f'  Wrote {os.path.getsize(path):,} B')
        finally:
            if tmppath.is_file():
                tmppath.unlink()
