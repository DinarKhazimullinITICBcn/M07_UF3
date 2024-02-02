import xml.etree.ElementTree as ET 
p = ET.Element('students')
for i in range(5) :
    c = ET.SubElement(p, 'student')
    a = ET.SubElement(c, 'name')
    a = ET.SubElement(c, 'surname')
    a = ET.SubElement(c, 'email')
    a = ET.SubElement(c, 'dni')
