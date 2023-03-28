import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries_gen.xml')
    if os.path.isfile(countries_xml):
        os.remove(countries_xml)
    classy = ClassyXml()

    # Creating Liechtenstein Element
    # Setting the text and attributes using the XmlElement arguments
    liechtenstein = XmlElement(attributes={'name': 'Liechtenstein'})
    liechtenstein.rank = XmlElement(text=1)
    liechtenstein.year = XmlElement(text=2008)
    liechtenstein.gdppc = XmlElement(text=141100)
    liechtenstein.neighbor = XmlElement(
        attributes={'name': 'Austria', 'direction': 'E'})
    liechtenstein.neighbor = XmlElement(
        attributes={'name': 'Switzerland', 'direction': 'W'})

    # Creating Singapore Element
    # Setting the text and attributes directly
    singapore = XmlElement()
    singapore.name = 'Singapore'
    singapore.rank = XmlElement()
    singapore.rank.text = 4
    singapore.year = XmlElement()
    singapore.year.text = 2011
    singapore.gdppc = XmlElement()
    singapore.gdppc.text = 59900
    singapore.neighbor = XmlElement()
    singapore.neighbor[0].name = 'Malaysia'
    singapore.neighbor[0].direction = 'N'

    # Add the countries to ClassyXml
    classy.country = liechtenstein
    classy.country = singapore

    classy.save_as(countries_xml)
    print(f'Generated {countries_xml}')
