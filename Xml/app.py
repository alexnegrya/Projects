from xml.etree import ElementTree
from xml.etree.ElementTree import Element
import xml.dom.minidom

# Tree initialization (in memory)
root = Element('person')
name = Element('name')
age = Element('age')
root.append(name)
root.append(age)

# Get and remember user input
name.text = input('Enter your name: ')
age.text = input('Enter your age: ')

# Save data (not pretty) in xml local file
ElementTree.ElementTree(root).write('person.xml', xml_declaration=True,
    encoding='utf-8')

# Get and prettyfy data from xml file
dom = xml.dom.minidom.parse('person.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml = dom.toprettyxml()

# Save pretty data in xml file
file = open('person.xml', 'w')
file.write(pretty_xml)
file.close()
