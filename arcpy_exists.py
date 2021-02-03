import arcpy
arcpy.env.workspace = "c:/temp"
arcpy.env.overwriteOutput = True

if arcpy.Exists("villes.shp"):
    print("La donnee existe")
else:
    print("Oups! donnee absente")