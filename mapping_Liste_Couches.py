#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")

for lyr in arcpy.mapping.ListLayers(mxd):
    try:
        print("Le nom est {} et la source est {}".format(lyr.name, lyr.dataSource))
    except:#Ce n'est pas toutes les couches qui ont une information de source disponible via dataSource
        pass


