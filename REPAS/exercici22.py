import xml.etree.ElementTree as ET
p = ET.Element('students')
informacio = [["John", "Mary", "Alice", "Bob", "Charlie"],["Smith", "Johnson", "Williams", "Brown", "Davis"],["john.smith@example.com", "mary.johnson@example.com", "alice.williams@example.com", "bob.brown@example.com", "charlie.davis@example.com"],["12345678A", "23456789B", "34567890C", "45678901D", "56789012E"]]
for i in range(5):
    c = ET.SubElement(p, 'student')
    aName = ET.SubElement(c, 'name')
    aName.set('nom', informacio[0][i])
    aSurname = ET.SubElement(c, 'surname')
    aSurname.set('cognom', informacio[1][i])
    aEmail = ET.SubElement(c, 'email')
    aEmail.set('email', informacio[2][i])  
    aDNI = ET.SubElement(c, 'dni')
    aDNI.set('dni', informacio[3][i])
tree = ET.ElementTree(p)
tree.write('students.xmls')
ET.dump(p)
