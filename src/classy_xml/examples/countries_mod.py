import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries.xml')
    countries_mod_xml = os.path.join(filepath, 'countries_mod.xml')
    if os.path.isfile(countries_mod_xml):
        os.remove(countries_mod_xml)
    obj = ClassyXml(countries_xml)

    obj.country = XmlElement()
    obj.country[-1].name = 'USA'
    obj.country[-1].rank = XmlElement()
    obj.country[-1].rank.text = 2
    obj.country[-1].year = XmlElement()
    obj.country[-1].year.text = 2012
    obj.country[-1].gdppc = XmlElement()
    obj.country[-1].gdppc.text = 12345
    obj.country[-1].neighbor = XmlElement()
    obj.country[-1].neighbor[0].name = 'Canada'
    obj.country[-1].neighbor[0].direction = 'N'
    obj.country[-1].neighbor = XmlElement()
    obj.country[-1].neighbor[1].name = 'Mexico'
    obj.country[-1].neighbor[1].direction = 'S'

    obj.save_as(countries_mod_xml)
    print(f'Modified {countries_xml} and saved to {countries_mod_xml}')
