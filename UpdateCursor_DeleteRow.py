#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
champs = ['PAYS', 'CAPITALES']
with arcpy.da.UpdateCursor("paysCaptiales", champs) as curseur:
    for ligne in curseur:
        if ligne[1] < 100000:
             curseur.deleteRow()











