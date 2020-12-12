import arcpy
arcpy.env.workspace 
rutaActualGdb = arcpy.env.workspace
rutaActualGdb = rutaActualGdb.replace('//','/')

print(rutaActualGdb)