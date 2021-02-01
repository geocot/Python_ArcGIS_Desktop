#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
with arcpy.da.SearchCursor("carre", "SHAPE@XY") as curseur:
    for ligne in curseur:
        print(ligne[0]) #Retourne le centroide de l'objet
