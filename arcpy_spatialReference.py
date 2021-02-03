import arcpy
arcpy.env.workspace = "c:/temp/Donnees.gdb"
arcpy.env.overwriteOutput = True

fcs = arcpy.ListFeatureClasses("vi*")
for fc in fcs:
    rs = arcpy.Describe(fc).spatialReference
    print(rs.name)