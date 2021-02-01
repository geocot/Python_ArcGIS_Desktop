#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
ptGeom = arcpy.PointGeometry(arcpy.Point(-73, 45), arcpy.SpatialReference(4326))
with arcpy.da.UpdateCursor("points", "SHAPE@") as curseur:
    for ligne in curseur:
        ligne[0] = ptGeom #Change tous les points avec la même coordonnée

        curseur.updateRow(ligne)
