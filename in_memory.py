#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
#Création de la référence spatiale
referenceSpatiale = arcpy.SpatialReference(4326)
#Création d'une classe d'entités avec l'outil
arcpy.CreateFeatureclass_management("in_memory", "pt_collecte", "POINT", spatial_reference=referenceSpatiale)
#Création d'un point
ptGeom = arcpy.PointGeometry(arcpy.Point(-71,46), referenceSpatiale)
#Création d'un champ avec l'outil
arcpy.AddField_management("in_memory/pt_collecte", "nom", "TEXT", field_length=20)
#Ajout d'un enregistrement avec UpdateCursor
curseur = arcpy.da.InsertCursor("in_memory/pt_collecte", ['SHAPE@', 'nom'])
curseur.insertRow([ptGeom, "Quebec"])
#Copy la classe d'entités de la mémoire vers le disque dur
arcpy.CopyFeatures_management("in_memory/pt_collecte", "C:/Temp/donnees.gdb/pt_collecte")
