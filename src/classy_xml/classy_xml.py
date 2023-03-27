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
        self.parsed_element_root = self.parse_xml(root, XmlElement())
        for attr_name in dir(self.parsed_element_root):
            attr = getattr(self.parsed_element_root, attr_name)
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

    def add_element(self, name):
        self.parsed_element_root.add_element(name)
        setattr(self, name, getattr(self.parsed_element_root, name))

    def remove_element(self, name):
        self.parsed_element_root.remove_element(name)
        delattr(self, name)


class XmlElement:

    class_methods = [
        'add_element',
        'remove_element',
        'add_text',
        'remove_text',
        'add_attribute',
        'remove_attribute'
    ]

    def __init__(self):
        """Helper class for the ClassyXml class
        """
        self._index = 0

    def add_element(self, name):
        attr = XmlElement()
        setattr(attr, 'text', None)
        setattr(self, name, attr)

    def remove_element(self, name):
        delattr(self, name)
        delattr(self, f'_{name}')

    def add_text(self, text, overwrite=False):
        if self.text is None or overwrite:
            delattr(self, 'text')
            delattr(self, '_text')
            setattr(self, 'text', text)
        else:
            raise AttributeError(
                f'This element already has the text {self.text} associated with it. Set the overwrite flag to overwrite the text')

    def remove_text(self):
        delattr(self, 'text')
        delattr(self, '_text')
        setattr(self, 'text', None)

    def add_attribute(self, name, value, overwrite=False):
        if not hasattr(self, name) or overwrite:
            setattr(self, name, str(value))
        else:
            raise AttributeError(
                f'The attribute {name} already exists. Set the overwrite flag to overwrite the attribute')

    def remove_attribute(self, name):
        delattr(self, name)
        delattr(self, f'_{name}')

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
        if name == 'class_methods' or name in self.class_methods or name[0] == '_':
            return super().__getattribute__(name)
        else:
            hidden_attr = super().__getattribute__(f'_{name}')
            if len(hidden_attr) == 1:
                return hidden_attr[0]
            else:
                return hidden_attr

    def __setattr__(self, name, value):
        if name in self.class_methods or name[0] == '_':
            super().__setattr__(name, value)
            return
        try:
            super().__getattribute__(f'_{name}').append(value)
        except AttributeError:
            super().__setattr__(f'_{name}', [value])
            super().__setattr__(name, value)
