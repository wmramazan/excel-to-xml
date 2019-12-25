import pandas as pd
from lxml import etree as ET

langs = {
    "en": "English",
    "it": "Italian",
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "tr": "Turkish"
}

excel = pd.read_excel('lang.xlsx')
labels = excel['Label']

for key, value in langs.items():
    data = excel[value]
    xml = ET.Element('resources')

    for i in range(len(labels)):
        string = ET.SubElement(xml, 'string', name = labels[i]).text = data[i]

    tree = ET.ElementTree(xml)
    tree.write(key + '.xml', encoding='UTF-8', method='xml', pretty_print = True)