import arcpy
arcpy.env.workspace = "c:/temp/"
image = arcpy.Raster("ancien_Drummondville.tif")

print(image.extent)