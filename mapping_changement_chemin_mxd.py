#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")

mxd.findAndReplaceWorkspacePaths(r"C:\temp\donnees.gdb",r"C:\temp\donnees2.gdb", True) #True fait une validation
#Si la validation n'est pas bonne, le changement n'est pas effectué.
mxd.saveACopy(r"C:\temp\amerique2.mxd")
