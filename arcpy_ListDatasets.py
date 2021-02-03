import arcpy
arcpy.env.workspace = "c:/temp/Donnees.gdb"
arcpy.env.overwriteOutput = True

listes = arcpy.ListDatasets()
for d in listes:
    print(d)