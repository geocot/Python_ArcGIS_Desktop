#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:/Temp/donnees.gdb"

soustypes = arcpy.da.ListSubtypes("villes")
for stcode, stdict in list(soustypes.items()):
    print("code: ", stcode, " nom: ",  stdict['Name'], " defaut: ", stdict['Default'])

"""
Retourne ceci:
('code: ', 0, ' nom: ', u'Villes', ' defaut: ', True)
('code: ', 1, ' nom: ', u'Grande ville', ' defaut: ', False)
"""




