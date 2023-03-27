
import os
import pytest
from classy_xml import ClassyXml, XmlElement


@pytest.fixture
def classy_xml_fixture():
    filepath = os.path.split(__file__)[0]
    test_xml = os.path.join(filepath, 'test.xml')
    return ClassyXml(test_xml)


def test_basic_element_length(classy_xml_fixture):
    assert len(classy_xml_fixture.basic_element) == 1


def test_basic_element_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_element.text == 'basic_element_text'


def test_multi_element_length(classy_xml_fixture):
    assert len(classy_xml_fixture.multi_element) == 2


def test_multi_element_0_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_element[0].text == 'multi_element_text_0'


def test_multi_element_1_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_element[1].text == 'multi_element_text_1'


def test_empty_element_with_attributes_length(classy_xml_fixture):
    assert len(classy_xml_fixture.empty_element_with_attributes) == 1


def test_empty_element_with_attributes_text(classy_xml_fixture):
    assert classy_xml_fixture.empty_element_with_attributes.text is None


def test_empty_element_with_attributes_attributes(classy_xml_fixture):
    assert classy_xml_fixture.empty_element_with_attributes.name == 'attr_name'
    assert classy_xml_fixture.empty_element_with_attributes.value == 'attr_value'


def test_empty_multi_element_with_attributes_length(classy_xml_fixture):
    assert len(classy_xml_fixture.empty_multi_element_with_attributes) == 2


def test_empty_multi_element_with_attributes_text(classy_xml_fixture):
    assert classy_xml_fixture.empty_multi_element_with_attributes[0].text is None
    assert classy_xml_fixture.empty_multi_element_with_attributes[1].text is None


def test_empty_multi_element_with_attributes_attributes(classy_xml_fixture):
    assert classy_xml_fixture.empty_multi_element_with_attributes[0].name == 'attr_0_name'
    assert classy_xml_fixture.empty_multi_element_with_attributes[0].value == 'attr_0_value'
    assert classy_xml_fixture.empty_multi_element_with_attributes[1].name == 'attr_1_name'
    assert classy_xml_fixture.empty_multi_element_with_attributes[1].value == 'attr_1_value'


def test_basic_element_with_attributes_length(classy_xml_fixture):
    assert len(classy_xml_fixture.basic_element_with_attributes) == 1


def test_basic_element_with_attributes_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_element_with_attributes.text == 'basic_element_with_attributes_text'


def test_basic_element_with_attributes_attributes(classy_xml_fixture):
    assert classy_xml_fixture.basic_element_with_attributes.name == 'attr_name'
    assert classy_xml_fixture.basic_element_with_attributes.value == 'attr_value'


def test_multi_element_with_attributes_length(classy_xml_fixture):
    assert len(classy_xml_fixture.multi_element_with_attributes) == 2


def test_multi_element_with_attributes_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_element_with_attributes[
        0].text == 'multi_element_with_attributes_text_0'
    assert classy_xml_fixture.multi_element_with_attributes[
        1].text == 'multi_element_with_attributes_text_1'


def test_multi_element_with_attributes_attributes(classy_xml_fixture):
    assert classy_xml_fixture.multi_element_with_attributes[0].name == 'attr_0_name'
    assert classy_xml_fixture.multi_element_with_attributes[0].value == 'attr_0_value'
    assert classy_xml_fixture.multi_element_with_attributes[1].name == 'attr_1_name'
    assert classy_xml_fixture.multi_element_with_attributes[1].value == 'attr_1_value'


def test_basic_nested_element_length(classy_xml_fixture):
    assert len(classy_xml_fixture.basic_nested_element) == 1


def test_basic_nested_element__basic_element_child_length(classy_xml_fixture):
    assert len(classy_xml_fixture.basic_nested_element.basic_element_child) == 1


def test_basic_nested_element__basic_element_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.basic_element_child.text == 'basic_element_child_text'


def test_basic_nested_element__multi_element_child_length(classy_xml_fixture):
    assert len(classy_xml_fixture.basic_nested_element.multi_element_child) == 2


def test_basic_nested_element__multi_element_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.multi_element_child[
        0].text == 'multi_element_child_text_0'
    assert classy_xml_fixture.basic_nested_element.multi_element_child[
        1].text == 'multi_element_child_text_1'


def test_basic_nested_element__empty_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.basic_nested_element.empty_element_with_attributes_child) == 1


def test_basic_nested_element__empty_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.empty_element_with_attributes_child.text is None


def test_basic_nested_element__empty_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.empty_element_with_attributes_child.name == 'child_attr_name'
    assert classy_xml_fixture.basic_nested_element.empty_element_with_attributes_child.value == 'child_attr_value'


def test_basic_nested_element__empty_multi_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child) == 2


def test_basic_nested_element__empty_multi_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        0].text is None
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        1].text is None


def test_basic_nested_element__empty_multi_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        0].name == 'child_attr_0_name'
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        0].value == 'child_attr_0_value'
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        1].name == 'child_attr_1_name'
    assert classy_xml_fixture.basic_nested_element.empty_multi_element_with_attributes_child[
        1].value == 'child_attr_1_value'


def test_basic_nested_element__basic_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.basic_nested_element.basic_element_with_attributes_child) == 1


def test_basic_nested_element__basic_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.basic_element_with_attributes_child.text == 'basic_element_with_attributes_child_text'


def test_basic_nested_element__basic_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.basic_element_with_attributes_child.name == 'child_attr_name'
    assert classy_xml_fixture.basic_nested_element.basic_element_with_attributes_child.value == 'child_attr_value'


def test_basic_nested_element__multi_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child) == 2


def test_basic_nested_element__multi_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        0].text == 'multi_element_with_attributes_child_text_0'
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        1].text == 'multi_element_with_attributes_child_text_1'


def test_basic_nested_element__multi_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        0].name == 'child_attr_0_name'
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        0].value == 'child_attr_0_value'
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        1].name == 'child_attr_1_name'
    assert classy_xml_fixture.basic_nested_element.multi_element_with_attributes_child[
        1].value == 'child_attr_1_value'


def test_multi_nested_element_length(classy_xml_fixture):
    assert len(classy_xml_fixture.multi_nested_element) == 2


def test_multi_nested_element__basic_element_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].basic_element_child) == 1
    assert len(
        classy_xml_fixture.multi_nested_element[1].basic_element_child) == 1


def test_multi_nested_element__basic_element_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].basic_element_child.text == 'basic_element_child_0_text'
    assert classy_xml_fixture.multi_nested_element[1].basic_element_child.text == 'basic_element_child_1_text'


def test_multi_nested_element__multi_element_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].multi_element_child) == 2
    assert len(
        classy_xml_fixture.multi_nested_element[1].multi_element_child) == 2


def test_multi_nested_element__multi_element_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[
        0].multi_element_child[0].text == 'multi_element_child_0_text_0'
    assert classy_xml_fixture.multi_nested_element[
        0].multi_element_child[1].text == 'multi_element_child_0_text_1'
    assert classy_xml_fixture.multi_nested_element[
        1].multi_element_child[0].text == 'multi_element_child_1_text_0'
    assert classy_xml_fixture.multi_nested_element[
        1].multi_element_child[1].text == 'multi_element_child_1_text_1'


def test_multi_nested_element__empty_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].empty_element_with_attributes_child) == 1
    assert len(
        classy_xml_fixture.multi_nested_element[1].empty_element_with_attributes_child) == 1


def test_multi_nested_element__empty_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].empty_element_with_attributes_child.text is None
    assert classy_xml_fixture.multi_nested_element[1].empty_element_with_attributes_child.text is None


def test_multi_nested_element__empty_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[
        0].empty_element_with_attributes_child.name == 'child_0_attr_name'
    assert classy_xml_fixture.multi_nested_element[
        0].empty_element_with_attributes_child.value == 'child_0_attr_value'
    assert classy_xml_fixture.multi_nested_element[
        1].empty_element_with_attributes_child.name == 'child_1_attr_name'
    assert classy_xml_fixture.multi_nested_element[
        1].empty_element_with_attributes_child.value == 'child_1_attr_value'


def test_multi_nested_element__empty_multi_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child) == 2
    assert len(
        classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child) == 2


def test_multi_nested_element__empty_multi_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        0].text is None
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        1].text is None
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        0].text is None
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        1].text is None


def test_multi_nested_element__empty_multi_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        0].name == 'child_0_attr_0_name'
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        0].value == 'child_0_attr_0_value'
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        1].name == 'child_0_attr_1_name'
    assert classy_xml_fixture.multi_nested_element[0].empty_multi_element_with_attributes_child[
        1].value == 'child_0_attr_1_value'
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        0].name == 'child_1_attr_0_name'
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        0].value == 'child_1_attr_0_value'
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        1].name == 'child_1_attr_1_name'
    assert classy_xml_fixture.multi_nested_element[1].empty_multi_element_with_attributes_child[
        1].value == 'child_1_attr_1_value'


def test_multi_nested_element__basic_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].basic_element_with_attributes_child) == 1
    assert len(
        classy_xml_fixture.multi_nested_element[1].basic_element_with_attributes_child) == 1


def test_multi_nested_element__basic_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[
        0].basic_element_with_attributes_child.text == 'basic_element_with_attributes_child_0_text'
    assert classy_xml_fixture.multi_nested_element[
        1].basic_element_with_attributes_child.text == 'basic_element_with_attributes_child_1_text'


def test_multi_nested_element__basic_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[
        0].basic_element_with_attributes_child.name == 'child_0_attr_name'
    assert classy_xml_fixture.multi_nested_element[
        0].basic_element_with_attributes_child.value == 'child_0_attr_value'
    assert classy_xml_fixture.multi_nested_element[
        1].basic_element_with_attributes_child.name == 'child_1_attr_name'
    assert classy_xml_fixture.multi_nested_element[
        1].basic_element_with_attributes_child.value == 'child_1_attr_value'


def test_multi_nested_element__multi_element_with_attributes_child_length(classy_xml_fixture):
    assert len(
        classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child) == 2
    assert len(
        classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child) == 2


def test_multi_nested_element__multi_element_with_attributes_child_text(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        0].text == 'multi_element_with_attributes_child_0_text_0'
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        1].text == 'multi_element_with_attributes_child_0_text_1'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        0].text == 'multi_element_with_attributes_child_1_text_0'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        1].text == 'multi_element_with_attributes_child_1_text_1'


def test_multi_nested_element__multi_element_with_attributes_child_attributes(classy_xml_fixture):
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        0].name == 'child_0_attr_0_name'
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        0].value == 'child_0_attr_0_value'
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        1].name == 'child_0_attr_1_name'
    assert classy_xml_fixture.multi_nested_element[0].multi_element_with_attributes_child[
        1].value == 'child_0_attr_1_value'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        0].name == 'child_1_attr_0_name'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        0].value == 'child_1_attr_0_value'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        1].name == 'child_1_attr_1_name'
    assert classy_xml_fixture.multi_nested_element[1].multi_element_with_attributes_child[
        1].value == 'child_1_attr_1_value'


def test_multi_nested_element__unique_element_child_existence(classy_xml_fixture):
    assert hasattr(
        classy_xml_fixture.multi_nested_element[0], 'unique_element_child')
    assert not hasattr(
        classy_xml_fixture.multi_nested_element[1], 'unique_element_child')


def test_classy_xml_add_element(classy_xml_fixture):
    assert not hasattr(classy_xml_fixture, 'test_element')
    classy_xml_fixture.add_element('test_element')
    assert hasattr(classy_xml_fixture, 'test_element')


def test_classy_xml_remove_element(classy_xml_fixture):
    classy_xml_fixture.add_element('test_element')
    assert hasattr(classy_xml_fixture, 'test_element')
    classy_xml_fixture.remove_element('test_element')
    assert not hasattr(classy_xml_fixture, 'test_element')


def test_classy_xml_add_element_array(classy_xml_fixture):
    assert not hasattr(classy_xml_fixture, 'test_element_array')
    classy_xml_fixture.add_element('test_element_array')
    classy_xml_fixture.add_element('test_element_array')
    assert isinstance(classy_xml_fixture.test_element_array[0], XmlElement)
    assert isinstance(classy_xml_fixture.test_element_array[1], XmlElement)
    assert len(classy_xml_fixture.test_element_array) == 2


def test_classy_xml_remove_element_array(classy_xml_fixture):
    classy_xml_fixture.add_element('test_element_array')
    classy_xml_fixture.add_element('test_element_array')
    assert len(classy_xml_fixture.test_element_array) == 2
    classy_xml_fixture.remove_element('test_element_array')
    assert not hasattr(classy_xml_fixture, 'test_element_array')


def test_xml_element_add_element(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert isinstance(
        classy_xml_fixture.classy_element.xml_element, XmlElement)


def test_xml_element_remove_element(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert hasattr(classy_xml_fixture.classy_element, 'xml_element')
    classy_xml_fixture.classy_element.remove_element('xml_element')
    assert not hasattr(classy_xml_fixture.classy_element, 'xml_element')


def test_xml_element_add_element_array(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert isinstance(
        classy_xml_fixture.classy_element.xml_element[0], XmlElement)
    assert isinstance(
        classy_xml_fixture.classy_element.xml_element[1], XmlElement)
    assert len(classy_xml_fixture.classy_element.xml_element) == 2


def test_xml_element_remove_element_array(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert len(classy_xml_fixture.classy_element.xml_element) == 2
    classy_xml_fixture.classy_element.remove_element('xml_element')
    assert not hasattr(classy_xml_fixture.classy_element, 'xml_element')


def test_xml_element_add_text(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert classy_xml_fixture.classy_element.xml_element.text is None
    classy_xml_fixture.classy_element.xml_element.add_text('test')
    assert classy_xml_fixture.classy_element.xml_element.text == 'test'


def test_xml_element_remove_text(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element.add_text('test')
    assert classy_xml_fixture.classy_element.xml_element.text == 'test'
    classy_xml_fixture.classy_element.xml_element.remove_text()
    assert classy_xml_fixture.classy_element.xml_element.text is None


def test_xml_element_array_add_text(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    assert classy_xml_fixture.classy_element.xml_element[0].text is None
    assert classy_xml_fixture.classy_element.xml_element[1].text is None
    classy_xml_fixture.classy_element.xml_element[0].add_text('test')
    assert classy_xml_fixture.classy_element.xml_element[0].text == 'test'
    assert classy_xml_fixture.classy_element.xml_element[1].text is None


def test_xml_element_array_remove_text(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element[0].add_text('test_0')
    classy_xml_fixture.classy_element.xml_element[1].add_text('test_1')
    assert classy_xml_fixture.classy_element.xml_element[0].text == 'test_0'
    assert classy_xml_fixture.classy_element.xml_element[1].text == 'test_1'
    classy_xml_fixture.classy_element.xml_element[0].remove_text()
    assert classy_xml_fixture.classy_element.xml_element[0].text is None
    assert classy_xml_fixture.classy_element.xml_element[1].text == 'test_1'


def test_xml_element_add_attribute(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element.add_attribute(
        'name', 'test_name')
    classy_xml_fixture.classy_element.xml_element.add_attribute('value', 1)
    assert classy_xml_fixture.classy_element.xml_element.name == 'test_name'
    assert classy_xml_fixture.classy_element.xml_element.value == '1'


def test_xml_element_remove_attribute(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element.add_attribute('value', 1)
    assert hasattr(classy_xml_fixture.classy_element.xml_element, 'value')
    classy_xml_fixture.classy_element.xml_element.remove_attribute('value')
    assert not hasattr(classy_xml_fixture.classy_element.xml_element, 'value')


def test_xml_element_array_add_attribute(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element[0].add_attribute(
        'name', 'test_name_0')
    classy_xml_fixture.classy_element.xml_element[1].add_attribute(
        'name', 'test_name_1')
    assert classy_xml_fixture.classy_element.xml_element[0].name == 'test_name_0'
    assert classy_xml_fixture.classy_element.xml_element[1].name == 'test_name_1'


def test_xml_element_array_remove_attribute(classy_xml_fixture):
    classy_xml_fixture.add_element('classy_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.add_element('xml_element')
    classy_xml_fixture.classy_element.xml_element[0].add_attribute(
        'name', 'test_name_0')
    classy_xml_fixture.classy_element.xml_element[1].add_attribute(
        'name', 'test_name_1')
    assert hasattr(classy_xml_fixture.classy_element.xml_element[0], 'name')
    assert hasattr(classy_xml_fixture.classy_element.xml_element[1], 'name')
    classy_xml_fixture.classy_element.xml_element[0].remove_attribute('name')
    assert not hasattr(
        classy_xml_fixture.classy_element.xml_element[0], 'name')
    assert hasattr(classy_xml_fixture.classy_element.xml_element[1], 'name')
