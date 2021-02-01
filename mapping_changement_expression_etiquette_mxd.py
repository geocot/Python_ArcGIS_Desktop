#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = 1
mxd = arcpy.mapping.MapDocument("C:/Temp/Donnees_Gouv/prj2.mxd")
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "Munic_CA":
        if lyr.supports("LABELCLASSES"):
            if lyr.showLabels:
                print "Layer name: " + lyr.name
                for lblClass in lyr.labelClasses:
                    if lblClass.showClassLabels:
                        lblClass.expression = '"Nom: " + [MUS_NM_MUN]'
mxd.saveACopy("C:/Temp/Donnees_Gouv/prjL.mxd")