import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries.xml')
    countries_mod_xml = os.path.join(filepath, 'countries_mod.xml')
    if os.path.isfile(countries_mod_xml):
        os.remove(countries_mod_xml)
    classy = ClassyXml(countries_xml)

    # Create a USA country element
    usa = XmlElement(attributes={'name': 'USA'})
    usa.rank = XmlElement(text=2)
    usa.year = XmlElement(text=2012)
    usa.gdppc = XmlElement(text=12345)
    usa.neighbor = XmlElement(attributes={'name': 'Canada', 'direction': 'N'})
    usa.neighbor = XmlElement(attributes={'name': 'Mexico', 'direction': 'S'})

    # Add the USA country element the ClassyXml countries
    classy.country = usa

    classy.save_as(countries_mod_xml)
    print(f'Modified {countries_xml} and saved to {countries_mod_xml}')
