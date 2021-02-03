import arcpy
arcpy.env.workspace = "c:/temp/Donnees.gdb"
arcpy.env.overwriteOutput = True

infos = arcpy.Describe(arcpy.env.workspace)
print(infos.domains)
print(infos.workspaceType)