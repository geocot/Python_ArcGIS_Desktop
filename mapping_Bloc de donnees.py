#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")
#bd est bloc de données
for bd in arcpy.mapping.ListDataFrames(mxd):
    print("Le nom est {}, la rotation est {} et l'échelle est {}".format(bd.name, bd.rotation, bd.scale))

