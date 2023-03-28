import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries_gen.xml')
    if os.path.isfile(countries_xml):
        os.remove(countries_xml)
    obj = ClassyXml()

    # Creating Country 1 Element
    # Setting the text and attributes using the XmlElement arguments
    obj.country = XmlElement(attributes={'name': 'Liechtenstein'})
    obj.country[0].rank = XmlElement(text=1)
    obj.country[0].year = XmlElement(text=2008)
    obj.country[0].gdppc = XmlElement(text=141100)
    obj.country[0].neighbor = XmlElement(
        attributes={'name': 'Austria', 'direction': 'E'})
    obj.country[0].neighbor = XmlElement(
        attributes={'name': 'Switzerland', 'direction': 'W'})

    # Creating Country 2 Element
    # Setting the text and attributes directly
    obj.country = XmlElement()
    obj.country[1].name = 'Singapore'
    obj.country[1].rank = XmlElement()
    obj.country[1].rank.text = 4
    obj.country[1].year = XmlElement()
    obj.country[1].year.text = 2011
    obj.country[1].gdppc = XmlElement()
    obj.country[1].gdppc.text = 59900
    obj.country[1].neighbor = XmlElement()
    obj.country[1].neighbor[0].name = 'Malaysia'
    obj.country[1].neighbor[0].direction = 'N'

    obj.save_as(countries_xml)
    print(f'Generated {countries_xml}')
