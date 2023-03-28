import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries.xml')
    countries_mod_xml = os.path.join(filepath, 'countries_mod.xml')
    if os.path.isfile(countries_mod_xml):
        os.remove(countries_mod_xml)
    obj = ClassyXml(countries_xml)

    # Add a USA country element
    obj.country = XmlElement(attributes={'name': 'USA'})
    obj.country[-1].rank = XmlElement(text=2)
    obj.country[-1].year = XmlElement(text=2012)
    obj.country[-1].gdppc = XmlElement(text=12345)
    obj.country[-1].neighbor = XmlElement(
        attributes={'name': 'Canada', 'direction': 'N'})
    obj.country[-1].neighbor = XmlElement(
        attributes={'name': 'Mexico', 'direction': 'S'})

    obj.save_as(countries_mod_xml)
    print(f'Modified {countries_xml} and saved to {countries_mod_xml}')
