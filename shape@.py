#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
with arcpy.da.SearchCursor("carre", "SHAPE@") as curseur:
    for ligne in curseur:
        print(ligne[0].firstPoint.X) #Retourne la coordonnées X du premier point
