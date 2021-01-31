#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"
tableau = arcpy.Array()
Qc = arcpy.Point(-71.22734082248334, 46.83023275891952)
tableau.add(Qc)

TR = arcpy.Point(-72.5432162679157, 46.34571909128457)
tableau.add(TR)

Mt = arcpy.Point(-73.56851992399947, 45.50345631685294)
tableau.add(Mt)

sr = arcpy.SpatialReference(4326) #WGS84

geomPolyligne = arcpy.Polyline(tableau, sr)
arcpy.CopyFeatures_management(geomPolyligne, "ligneMtQc")












