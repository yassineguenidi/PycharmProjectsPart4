# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

chemin = "C:/Users/yassi/Desktop/1ere IDSD/S2/XML/ex1.xml"
arbreXML = ET.parse(chemin)
tronc = arbreXML.getroot()
print(tronc)