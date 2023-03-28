import os
from classy_xml import ClassyXml, XmlElement

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries_gen.xml')
    if os.path.isfile(countries_xml):
        os.remove(countries_xml)
    obj = ClassyXml(countries_xml)

    obj.country = XmlElement()
    obj.country[0].name = 'Liechtenstein'
    obj.country[0].rank = XmlElement()
    obj.country[0].rank.text = 1
    obj.country[0].year = XmlElement()
    obj.country[0].year.text = 2008
    obj.country[0].gdppc = XmlElement()
    obj.country[0].gdppc.text = 141100
    obj.country[0].neighbor = XmlElement()
    obj.country[0].neighbor[0].name = 'Austria'
    obj.country[0].neighbor[0].direction = 'E'
    obj.country[0].neighbor = XmlElement()
    obj.country[0].neighbor[1].name = 'Switzerland'
    obj.country[0].neighbor[1].direction = 'W'

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

    obj.country = XmlElement()
    obj.country[2].name = 'Panama'
    obj.country[2].rank = XmlElement()
    obj.country[2].rank.text = 68
    obj.country[2].year = XmlElement()
    obj.country[2].year.text = 2011
    obj.country[2].gdppc = XmlElement()
    obj.country[2].gdppc.text = 13600
    obj.country[2].neighbor = XmlElement()
    obj.country[2].neighbor[0].name = 'Costa Rica'
    obj.country[2].neighbor[0].direction = 'W'
    obj.country[2].neighbor = XmlElement()
    obj.country[2].neighbor[1].name = 'Colombia'
    obj.country[2].neighbor[1].direction = 'E'

    obj.save()
    print(f'Generated {countries_xml}')
