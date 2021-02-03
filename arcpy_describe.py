import arcpy
arcpy.env.workspace = "c:/temp/Donnees.gdb"
arcpy.env.overwriteOutput = True

infos = arcpy.Describe("villes")
print(infos.shapeType)
print(infos.hasZ)
print(infos.fields)