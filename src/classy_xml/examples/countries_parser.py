import os
from classy_xml import ClassyXml

if __name__ == '__main__':
    filepath = os.path.split(__file__)[0]
    countries_xml = os.path.join(filepath, 'countries.xml')
    obj = ClassyXml(countries_xml)

    print(len(obj.country))                     # Output: 2

    print(obj.country[0].name)                  # Output: 'Liechtenstein'
    print(obj.country[0].rank.text)             # Output: '1'
    print(obj.country[0].year.text)             # Output: '2008'
    print(obj.country[0].gdppc.text)            # Output: '141100'
    print(len(obj.country[0].neighbor))         # Output: 2
    print(obj.country[0].neighbor[0].name)      # Output: 'Austria'
    print(obj.country[0].neighbor[0].direction)  # Output: 'E'
    print(obj.country[0].neighbor[1].name)      # Output: 'Switzerland'
    print(obj.country[0].neighbor[1].direction)  # Output: 'W'

    print(obj.country[1].name)                  # Output: 'Singapore'
    print(obj.country[1].rank.text)             # Output: '4'
    print(obj.country[1].year.text)             # Output: '2011'
    print(obj.country[1].gdppc.text)            # Output: '59900'
    print(len(obj.country[1].neighbor))         # Output: 1
    print(obj.country[1].neighbor.name)         # Output: 'Malaysia'
    print(obj.country[1].neighbor.direction)    # Output: 'N'
