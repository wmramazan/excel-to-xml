from lxml import etree as ET

langs = [
    "en",
    "it",
    "de",
    "es",
    "fr",
    "nl",
    "pl",
    "pt",
    "tr"
]

input = ET.parse('input.xml')
input_root = input.getroot()

for lang in langs:
    root = ET.parse(lang + '.xml').getroot()
    xml = ET.Element('resources')

    for elem in input_root.getchildren():
        name = elem.attrib['name']
        string = root.find("./string[@name = '" + name + "']")
        if string is not None:
            ET.SubElement(xml, 'string', name = name).text = string.text
        
    tree = ET.ElementTree(xml)
    tree.write(lang + '_split.xml', encoding='UTF-8', method='xml', pretty_print = True)