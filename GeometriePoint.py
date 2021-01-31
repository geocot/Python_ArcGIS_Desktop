#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"

point = arcpy.Point(-71.22734082248334, 46.83023275891952)
sr = arcpy.SpatialReference(4326) #WGS84

geomPoint = arcpy.PointGeometry(point, sr)
#On pourait utiliser une liste de points géométriques
arcpy.CopyFeatures_management(geomPoint, "points")










