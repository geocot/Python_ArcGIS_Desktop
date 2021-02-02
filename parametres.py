#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy, sys
arcpy.env.overwriteOutput = 1
FC = sys.argv[1]
desc = arcpy.Describe(FC)
arcpy.AddMessage("La reference spatiale est : " + desc.spatialReference.name)
