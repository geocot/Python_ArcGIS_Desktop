#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")
arcpy.mapping.ExportToPDF(mxd, "C:/temp/amerique.pdf")


