#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

mxd = arcpy.mapping.MapDocument("C:/temp/amerique.mxd")
arcpy.mapping.ExportToPDF(mxd, "C:/temp/amerique.pdf")


"""
Avec une liste de fichier MXD.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy

arcpy.env.workspace = "c:/temp"

# Copy each file with a .csv extension to a dBASE file
for fichier_MXD in arcpy.ListFiles("*.mxd"):
    mxd = arcpy.mapping.MapDocument(fichier_MXD)
    arcpy.mapping.ExportToPDF(mxd, fichier_MXD + ".pdf")


"""