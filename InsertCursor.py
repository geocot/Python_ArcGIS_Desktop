#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
champs = ['PAYS', 'CAPITALES']
curseur = arcpy.da.InsertCursor("paysCaptiales", champs)

curseur.insertRow(("Canada", "Ottawa"))




