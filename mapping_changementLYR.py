#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
lyrFile = arcpy.mapping.Layer(r"C:\temp\villes.lyr")
for lyr in arcpy.mapping.ListLayers(lyrFile):
    if lyr.name.lower() == "villes":
        lyr.showLabels = True
        lyr.saveACopy(r"C:\temp\villesavecetiquettes.lyr")
        
        