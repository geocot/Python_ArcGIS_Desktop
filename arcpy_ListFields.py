import arcpy
arcpy.env.workspace = "c:/temp/Donnees.gdb"
arcpy.env.overwriteOutput = True

champs = arcpy.ListFields("villes")
for champ in champs:
    print("Le nom du champ est {} et le type est {}".format(champ.name, champ.type)