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

#Export chaque fichier .mxd en fichier PDF 
for fichier_MXD in arcpy.ListFiles("*.mxd"):
    mxd = arcpy.mapping.MapDocument(fichier_MXD)
    arcpy.mapping.ExportToPDF(mxd, fichier_MXD + ".pdf")
"""