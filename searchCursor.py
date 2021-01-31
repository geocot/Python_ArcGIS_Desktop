#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"

curseur = arcpy.da.SearchCursor("villes", ['NAME', 'POPULATION'])

for ligne in curseur:
    print(ligne)
    
"""
Peut-être remplacé par 
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"

with arcpy.da.SearchCursor("villes", ['NAME', 'POPULATION']) as curseur

for ligne in curseur:
    print(ligne)
"""



