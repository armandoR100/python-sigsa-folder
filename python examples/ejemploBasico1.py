import arcpy 

def crearNombreDeTopologia(nombreT,lista):
  nombre = getLastValueOfList(lista) 
  nuevoNombre = nombreT+"_"+nombre[0]
  return nuevoNombre 

def getLastValueOfList(lista):
  listaNueva = []
  for i,valor in enumerate(lista):
    aux = valor.split("/")
    v = aux[len(aux)-2]
    listaNueva.append(v)
  return listaNueva

def unirConOtraLista(valor,lista):    
  ListaNueva = []
  for i in range(0,len(lista)):
    ListaNueva.append(valor+"/"+lista[i])
  return ListaNueva

def unirListaConLista(lista1,lista2):
  nuevaLista = []
  for i in range(0,len(lista1)):
    nuevaLista.append(lista1[i])
  for j in range(0,len(lista2)):
    nuevaLista.append(lista2[j])
  return nuevaLista

def creoTopologia(gdb,nombreDeTopologia):
  arcpy.CreateTopology_management(gdb,nombreDeTopologia,1)
  urlTopology = gdb+"/"+nombreDeTopologia
  return urlTopology

def agregoClase(Topologia,featureClasses):
  arcpy.AddFeatureClassToTopology_management(Topologia,featureClasses,1,1)

def agregarReglas(Topo,FCPLin,FCLPol,rulesPL):
  if( len(FCPLin) == len(FCLPol) ):
    for j in range(0,len(FCPLin)):
      for k in range(0,len(rulesPL)):
        arcpy.AddRuleToTopology_management(Topo,rulesPL[k],FCPLin[j],"S1",FCLPol[j],"S2")
  else:
    print("no se puede agregar reglas disparejas")

def validoTopologia(Topo):
  arcpy.ValidateTopology_management(Topo)

def creandoTopologiaBasica(gdb,nameTopo,listaFc,fc1,fc2,reglas):
  nameTopo = crearNombreDeTopologia(nameTopo,listaFc)  
  url_Topo = creoTopologia(gdb,nameTopo)
  for i in range(0,len(listaFc)):
    agregoClase(url_Topo,listaFc[i])
  agregarReglas(url_Topo,fc1,fc2,reglas)
  validoTopologia(url_Topo)

def creandoTopologiaAuxiliares(gdb,nameTopo,listaAux,fclass1,fclass2,rules):
  nameTopo = crearNombreDeTopologia(nameTopo,fclass1)  
  urlTopo = creoTopologia(gdb,nameTopo)
  for i in range(0,len(listaAux)):
    agregoClase(urlTopo,listaAux[i])
  agregarReglas(urlTopo,fclass1,fclass2,rules)
  validoTopologia(urlTopo)

#basico
nameGdb = "version.gdb"
UrlGdb ="C:/Unit"+"/"+nameGdb
#secundarios 
nombrePorDefectoTopologia = "topologia"
dataSets = ["LINEAS","POLIGONOS","PUNTOS","LINE-POL","POL-LINE"]
UrlsDataSet = unirConOtraLista(UrlGdb,dataSets)
#featuresClass
FCLineas = ["alti","arbl","infl","viasl"]
FCPoligonos = ["arbp","infp","consp"]
FCPuntos = ["cotas","arbs","infs"]
FCLinePolig = ["arbl","consl","hidrl","manzl","terrl"]
FCPoligLine = ["arbp","consp","hidrp","manzp","terrp"]
urlsFCLineales = unirConOtraLista(UrlsDataSet[0],FCLineas)
urlsFCPoligonales = unirConOtraLista(UrlsDataSet[1],FCPoligonos)
urlsFCPuntuales = unirConOtraLista(UrlsDataSet[2],FCPuntos)
urlsFCPoligonalesLineales = unirConOtraLista(UrlsDataSet[3],FCLinePolig)
urlsFCLinealesPoligonales = unirConOtraLista(UrlsDataSet[4],FCPoligLine)
listaFeatureClassUnidaAuxiliares_LP_PL = unirListaConLista(urlsFCPoligonalesLineales,urlsFCLinealesPoligonales)
#rules
rulesLineas = ["no-insertar(LINE)","No intersecarse(LINE)","No pseudonodos(LINE)"]
rulesPoligonos = ["tolerancia cluster(POL)","No superponerse(POL)","No huecos(POL)"]
rulesPuntos = ["Debe coincidir con(PUNTO)"]
rulesPoligonosLineas = ["no auxiliar(POL-LINE)","no falta(POL-LINE)"]
rulesLineasPoligonos = ["no dangles(LINE-Pol)"]

#lineas  
creandoTopologiaBasica(UrlGdb,nombrePorDefectoTopologia,urlsFCLineales,urlsFCLineales,urlsFCLineales,rulesLineas)
#Poligonales
creandoTopologiaBasica(UrlGdb,nombrePorDefectoTopologia,urlsFCPoligonales,urlsFCPoligonales,urlsFCPoligonales,rulesPoligonos)
#Puntos
creandoTopologiaBasica(UrlGdb,nombrePorDefectoTopologia,urlsFCPuntuales,urlsFCPuntuales,urlsFCPuntuales,rulesPuntos)
#PolygoneTolines
creandoTopologiaAuxiliares(UrlGdb,nombrePorDefectoTopologia,listaFeatureClassUnidaAuxiliares_LP_PL,urlsFCPoligonalesLineales,urlsFCLinealesPoligonales,rulesPoligonosLineas)
#linesToPolygone
creandoTopologiaAuxiliares(UrlGdb,nombrePorDefectoTopologia,listaFeatureClassUnidaAuxiliares_LP_PL,urlsFCLinealesPoligonales,urlsFCPoligonalesLineales,rulesLineasPoligonos)
