#definimos el workspace como el dataset
wks=arcpy.env.workspace=r"C:\ArpyAvan\Unidad2\Ejercicio2.gdb\Topologia"
arcpy.env.overwriteOutput = True
#Creamos La topología, recordar que estra vacía tanto de entidades como de reglas
arcpy.CreateTopology_management(wks,"Topology",0.0001)
desc=arcpy.Describe(Wks)
# esta es una forma rapida de insertar las features clas dentro de la topoLogia
# con chiLdren obtenemos la lista de sub elementos del WKS que iteraremos con
#(recordar que las entidades a validar han de estar en el mismo dataset que la Topologia creada)
for features in desc.children:
    ftype=features.dataType
    name=features.name
    if ftype=="FeatureClass":
    arcpy.Add FeatureClassToTopology_management("Topology",name ,l)
#insertamos las reglas de topologia
arcpy.Add RuleToTopology_management("Topology","Must Not Have Gaps (Area)","Level1A")
#por ultimo validamos la topologia
arcpy.ValidateTopology_management("Topology")