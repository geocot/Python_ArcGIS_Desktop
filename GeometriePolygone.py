#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
tableau = arcpy.Array()
Pt1 = arcpy.Point(-73, 45)
tableau.add(Pt1)

Pt2 = arcpy.Point(-73, 46)
tableau.add(Pt2)

Pt3 = arcpy.Point(-72, 46)
tableau.add(Pt3)

Pt4 = arcpy.Point(-72, 45)
tableau.add(Pt4)

sr = arcpy.SpatialReference(4326) #WGS84

geomPolygone = arcpy.Polygon(tableau, sr)
arcpy.CopyFeatures_management(geomPolygone, "carre")

