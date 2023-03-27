from __future__ import annotations
import xml.etree.ElementTree as ET


class ClassyXml:
    def __init__(self, xml_file: str):
        """ClassyXml Class
        An xml file parser that makes the element text and attributes of an 
        xml file accessible as ClassyXml class attributes.

        Args:
            xml_file (str): xml file to parse
        """

        root = ET.parse(xml_file).getroot()
        parsed_element_root = self.parse_xml(root, XmlElement())
        for attr_name in dir(parsed_element_root):
            attr = getattr(parsed_element_root, attr_name)
            if isinstance(attr, XmlElement) or (isinstance(attr, list) and isinstance(attr[0], XmlElement)):
                setattr(self, attr_name, attr)

    def parse_xml(self, root: ET.Element, element: XmlElement):
        """Parse the xml file and create class attributes for the elements and
        attributes defined in the xml file.
        """
        for key, value in root.attrib.items():
            setattr(element, key, value)
        children = root.findall('*')
        for child in children:
            child_element = self.parse_xml(child, XmlElement())
            setattr(element, child.tag, child_element)
            setattr(child_element, 'text', child.text)
        return element


class XmlElement:
    def __init__(self):
        """Helper class for the ClassyXml class
        """
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 1:
            self._index = 0
            raise StopIteration
        self._index += 1
        return self

    def __len__(self):
        return 1

    def __getattribute__(self, name):
        if name[0] == '_':
            return super().__getattribute__(name)
        else:
            hidden_attr = super().__getattribute__(f'_{name}')
            if len(hidden_attr) == 1:
                return hidden_attr[0]
            else:
                return hidden_attr

    def __setattr__(self, name, value):
        if name[0] == '_':
            super().__setattr__(name, value)
            return
        try:
            super().__getattribute__(f'_{name}').append(value)
        except AttributeError:
            super().__setattr__(f'_{name}', [value])
            super().__setattr__(name, value)
