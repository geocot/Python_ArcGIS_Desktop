#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")

for lyr in arcpy.mapping.ListLayers(mxd):
    print(lyr.name)


