from typing import Any, List, Optional

from lxml import etree

class BaseDef:
    def __init__(self) -> None:
        self.typeid: str = ''

        self.defName: str = 'UnnamedDef'
        self.label: Optional[str] = None
        self.description: Optional[str] = None
        self.descriptionHyperlinks: Optional[List[str]] = None
        self.ignoreConfigErrors: Optional[bool] = None
        self.ignoreIllegalLabelCharacterConfigError: Optional[bool] = None
        self.modExtensions: Optional[List[Any]] = None
        
    def fromXML(self, e: etree._Element) -> None:
        self.defName = e.find('defName').text
        
        if (se := e.find('label')) is not None:
            self.label = se.text
        else:
            self.label = None

        if (se := e.find('description')) is not None:
            self.description = se.text
        else:
            self.description = None

        if (se := e.find('descriptionHyperlinks')) is not None:
            self.descriptionHyperlinks = [x.text for x in se.getchildren()]
        else:
            self.descriptionHyperlinks = None

        if (se := e.find('ignoreConfigErrors')) is not None:
            self.ignoreConfigErrors = bool(se.text)
        else:
            self.ignoreConfigErrors = None

        if (se := e.find('ignoreIllegalLabelCharacterConfigError')) is not None:
            self.ignoreIllegalLabelCharacterConfigError = bool(se.text)
        else:
            self.ignoreIllegalLabelCharacterConfigError = None