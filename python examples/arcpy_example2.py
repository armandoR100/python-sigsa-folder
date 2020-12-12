dataSet = ['C:/Users/arboles','C:/Users/hidrologia','C:/Users/vias']
featuresClass = ['C:/Users/arboles/arbl','C:/Users/hidrologia/hdl','C:/Users/vias/viasl']
rule = "Must Not Intersect (Line)"

def CreateTopology_management(dataset,name,tolerancia):
    print("CREO topologia '"+name+"' en el dataset'"+dataset+"'")

def AddFeatureClassToTopology(topology,featureclass,rankx,rankz):
    print("AGREGO topologia '"+topology+"' con el feature class'"+featureclass+"'")

def AddRuleToTopology(topology,rule,featureclass,subtype,featureclass2,subtype2):
    print("CREO_REGLA '"+rule+"' en la topologia '"+topology+"' y con fc "+featureclass)
    #subtype=BlockLines
  
def ValidateTopology(in_topology):
    print("VALIDO topologia '"+in_topology+"'")
  
for pos, v in enumerate(featuresClass):
    name = "topo_"+str(pos)
    CreateTopology_management(dataSet[pos], name ,1)
    newRutaTopologia = dataSet[pos]+"/"+name
    AddFeatureClassToTopology(newRutaTopologia, featuresClass[pos] ,1,1)
    AddRuleToTopology(newRutaTopologia, rule ,"Level1A","","","")
    ValidateTopology(newRutaTopologia)
    print("")