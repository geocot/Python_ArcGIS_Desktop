#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
mxd = arcpy.mapping.MapDocument("C:/Temp/Donnees_Gouv/prj2.mxd")
lyr = arcpy.mapping.ListLayers(mxd)[1]
print(lyr)
print(lyr.symbologyType)
if lyr.symbologyType == "UNIQUE_VALUES":
    lyr.symbology.valueField = "MUS_CO_DES"
    lyr.symbology.addAllValues()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.saveACopy("C:/Temp/Donnees_Gouv/prj3.mxd")
