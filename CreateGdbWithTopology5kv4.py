import arcpy
""" arcpy.env.workspace 
rutaActualGdb = arcpy.env.workspace
rutaActualGdb = rutaActualGdb.replace('//','/')
 """

#variables a modificar
#las urls siempren deben ir con slash asi '/' y no asi '\'
nombrePorDefectoTopologia = "topo" 
nombrePorDefectoGdb = "topo.gdb"
FolderParaGuardarNuevaGdb = "D:/Compaida/compartida/PROY_5K_2020/VERACRUZ_2020/PROCESOS/asig_9"
rutaActualGdb = "D:/Compaida/compartida/PROY_5K_2020/VERACRUZ_2020/PROCESOS/asig_9/Asignacion_9_veracruz.gdb"
zone = "14"





#duda
#script que envie y me imprima la ws workspace only
#que si la carpeta siempre debe de estar un nivel abajo





#NO MODIFICAR NINGUNA FUNCION PLEASE

#comida3 = "C://Users//armando//Documents//__pycache__"
def quitaDobleSlashNormal(cadena):
  cadena = cadena.replace('//','/')
  print(cadena)
  return cadena

#comida1 = r"C:\Users\armando\Documents\__pycache__"
def quitaSlashInversa(cadena):
  cadena = cadena.replace('\\','/')
  print(cadena)
  return cadena

#comida2 = r"C:\\Users\\armando\Documents\\__pycache__"
def quitaDobleSlashInversa(cadena):
  cadena = cadena.replace("\\\\",'/')
  print(cadena)
  return cadena  

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

def agregarReglas(Topo,FCPLin,FCLPol,rulesPL):
  if( len(FCPLin) == len(FCLPol) ):
    for j in range(0,len(FCPLin)):
      for k in range(0,len(rulesPL)):
        arcpy.AddRuleToTopology_management(Topo,rulesPL[k],FCPLin[j],"S1",FCLPol[j],"S2")
  else:
    print("no se puede agregar reglas disparejas")

def creandoTopologiaBasica(gdb,nameTopo,listaFc,fc1,fc2,reglas):
  nameTopo = crearNombreDeTopologia(nameTopo,listaFc)  
  url_Topo = creoTopologia(gdb,nameTopo)
  for i in range(0,len(listaFc)):
    arcpy.AddFeatureClassToTopology_management(url_Topo,listaFc[i],1,1)
  agregarReglas(url_Topo,fc1,fc2,reglas)
  arcpy.ValidateTopology_management(url_Topo)

def TopologiaAuxiliar(gdb,nameTopo,nameAux,listaAux,fclass1,fclass2,rules):
    nameTopo = nameTopo+nameAux
    urlTopo = creoTopologia(gdb,nameTopo)
    for i in range(0,len(listaAux)):
      arcpy.AddFeatureClassToTopology_management(urlTopo,listaAux[i],1,1)
    agregarReglas(urlTopo,fclass1,fclass2,rules)
    arcpy.ValidateTopology_management(urlTopo)

def creaGdbConDatasets(folderpath,nameGdb, version,FeaturesDataSets,dirGdb,spatialReference):
    arcpy.CreateFileGDB_management(folderpath, nameGdb, version)
    for i in range(0,len(FeaturesDataSets)):
        arcpy.CreateFeatureDataset_management(dirGdb,FeaturesDataSets[i],spatialReference)

def createNewName(lista):
  nuevaLista = []
  for i in range(0,len(lista)):
    nuevaLista.append(lista[i]+"_"+str(1))
  return nuevaLista

def getNewsFeaturesClass(ListaFeatureClass):
  namesFeatureClassL = []
  for valor in ListaFeatureClass:
    aux = valor.split("/")
    namesFeatureClassL.append(aux[len(aux)-1])   
  return namesFeatureClassL

def importandoClasesAgdb(ListFeatureClassLinea,CurrentFeaturesClass,namesFeatureClassL):
  """ print("\n\n","importandoClasesAgdb().valor3 = ",namesFeatureClassL,"\n")
  print("importandoClasesAgdb().valor2 = ",CurrentFeaturesClass,"\n")
  print("importandoClasesAgdb().valor1 = ",ListFeatureClassLinea,"\n\n")
 """
  for a in range(0,len(ListFeatureClassLinea)):
    arcpy.FeatureClassToFeatureClass_conversion(ListFeatureClassLinea[a],CurrentFeaturesClass,namesFeatureClassL[a])
    
def validaNombresFcSeanLinePolig(FCLineas):
  FCTypeLine = []
  for i in range(0,len(FCLineas)):
    if FCLineas[i]=="ARBSL":  
      FCTypeLine.append(FCLineas[i]+"_"+str(1))
    elif FCLineas[i]=="CONSL":
      FCTypeLine.append(FCLineas[i]+"_"+str(1))
    elif FCLineas[i]=="CULTL":
      FCTypeLine.append(FCLineas[i]+"_"+str(1))
    elif FCLineas[i]=="HIDRL":
      FCTypeLine.append(FCLineas[i]+"_"+str(1))
    elif FCLineas[i]=="MANZL":
      FCTypeLine.append(FCLineas[i]+"_"+str(1))
  urlsFcLP = FCTypeLine
  return urlsFcLP

def validaNombresFcSeanPoligLine(FCPoligonos):
  FCTypePolygone = []
  for j in range(0,len(FCPoligonos)):
    if FCPoligonos[j]=="ARBSP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
    elif FCPoligonos[j]=="CONSP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
    elif FCPoligonos[j]=="CULTP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
    elif FCPoligonos[j]=="CONSP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
    elif FCPoligonos[j]=="HIDRP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
    elif FCPoligonos[j]=="MANZP":
      FCTypePolygone.append(FCPoligonos[j]+"_"+str(1))
  urlsFcLP = FCTypePolygone
  return urlsFcLP

def validateZoneSpatialReference(zonaReference):
  if zonaReference == "14":
    spatialReference = "PROJCS['WGS_1984_UTM_Zone_14N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-99.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
  elif zonaReference == "15":
    spatialReference = "PROJCS['WGS_1984_UTM_Zone_15N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
  elif zonaReference == "16":
    spatialReference = "PROJCS['WGS_1984_UTM_Zone_16N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
  else:
    spatialReference = "0"  
  return spatialReference    

def CreateGdbAndCreateTopology(nombreGdbNueva,DirCarpetaGdbNueva,nombreTopo,rutaActualGdb,zonaReferencia):
    version = "CURRENT"
    nameGdb = nombreGdbNueva
    folderpath = DirCarpetaGdbNueva
    UrlGdb = folderpath+"/"+nameGdb
    dataSets = ["LINEAS","POLIGONOS","PUNTOS","AUX"] 
    UrlsDataSet = unirConOtraLista(UrlGdb,dataSets)
    ws = rutaActualGdb
    ListFeatureClassLinea = [
        ws+"/"+"ALTIMETRIA"+"/"+"ALTI" ,
        ws+"/"+"ARBOLES"+"/"+"ARBSL" ,
        ws+"/"+"CONS"+"/"+"CONSL" , 
        ws+"/"+"CULT"+"/"+"CULTL" , 
        ws+"/"+"HIDR"+"/"+"HIDRL" , 
        ws+"/"+"INFR"+"/"+"INFRL" , 
        ws+"/"+"MANZ"+"/"+"MANZL" , 
        ws+"/"+"OTRS"+"/"+"OTRSL" , 
        ws+"/"+"VIAS"+"/"+"VIASL"
    ]
    ListFeatureClassPolig = [
        ws+"/"+"ARBOLES"+"/"+"ARBSP" ,
        ws+"/"+"CONS"+"/"+"CONSP" , 
        ws+"/"+"CULT"+"/"+"CULTP" , 
        ws+"/"+"HIDR"+"/"+"HIDRP" , 
        ws+"/"+"MANZ"+"/"+"MANZP"  
    ]
    ListFeatureClassPunto = [
        ws+"/"+"ALTIMETRIA"+"/"+"COTAS" ,
        ws+"/"+"ARBOLES"+"/"+"ARBSS" ,
        ws+"/"+"CONS"+"/"+"CONSS" , 
        ws+"/"+"CULT"+"/"+"CULTS" , 
        ws+"/"+"HIDR"+"/"+"HIDRS" , 
        ws+"/"+"INFR"+"/"+"INFRS" , 
        ws+"/"+"MANZ"+"/"+"MANZS" , 
        ws+"/"+"OTRS"+"/"+"OTRSS" 
    ]
    ListFeatureClassAux = [
        ws+"/"+"ARBOLES"+"/"+"ARBSL" ,
        ws+"/"+"CONS"+"/"+"CONSL" , 
        ws+"/"+"CULT"+"/"+"CULTL" , 
        ws+"/"+"HIDR"+"/"+"HIDRL" , 
        ws+"/"+"MANZ"+"/"+"MANZL" , 
        ws+"/"+"ARBOLES"+"/"+"ARBSP",
        ws+"/"+"CONS"+"/"+"CONSP" , 
        ws+"/"+"CULT"+"/"+"CULTP" , 
        ws+"/"+"HIDR"+"/"+"HIDRP" , 
        ws+"/"+"MANZ"+"/"+"MANZP"  
    ]
    nameTopo = nombreTopo
    rulesLine = ["Must Not Overlap (Line)","Must Not Intersect (Line)","Must Not Have Dangles (Line)","Must Not Self-Overlap (Line)","Must Not Self-Intersect (Line)"]
    rulesPoly = ["Must Not Overlap (Area)","Must Not Have Gaps (Area)"]
    rulesPoint = ["Must Be Disjoint (Point)"]
    rulesLP = ["Must Be Covered By Boundary Of (Line-Area)","Must Be Inside (Line-Area)"]
    rulesPL = ["Boundary Must Be Covered By (Area-Line)"]
    #validateSpatialReference
    spatialReference = validateZoneSpatialReference(zonaReferencia)
    #create gdb
    creaGdbConDatasets(folderpath,nameGdb,version,dataSets,UrlGdb,spatialReference)
    #URLS IMPORTADOS Lines
    nombresFcL = getNewsFeaturesClass(ListFeatureClassLinea)    
    dirLinealFC = unirConOtraLista(UrlsDataSet[0],nombresFcL)
    #URLS IMPORTADOS Polygone
    nombresFcPol = getNewsFeaturesClass(ListFeatureClassPolig)    
    dirPolyFC = unirConOtraLista(UrlsDataSet[1],nombresFcPol)
    #URLS IMPORTADOS Points
    nombresFcPun = getNewsFeaturesClass(ListFeatureClassPunto)    
    dirPuntoFC =  unirConOtraLista(UrlsDataSet[2],nombresFcPun)
    #URLS IMPORTADOS LINE-POLYGONE
    nombresFC_LP = validaNombresFcSeanLinePolig(nombresFcL)
    nombresFC_PL = validaNombresFcSeanPoligLine(nombresFcPol)
    listUnionsNames = getNewsFeaturesClass(ListFeatureClassAux)
    #cambiando nombre
    listUnionsNames = createNewName(listUnionsNames)
    urlsFC_LP = unirConOtraLista(UrlsDataSet[3],nombresFC_LP)
    urlsFC_PL = unirConOtraLista(UrlsDataSet[3],nombresFC_PL)
    listUnionsURLS = unirListaConLista(urlsFC_LP,urlsFC_PL)
    """ print("listUnionsNames = ",listUnionsNames)
    print("urlsFC_LP = ",urlsFC_LP)
    print("urlsFC_pl = ",urlsFC_PL)
     """
    print("listUnionsURLS = ",listUnionsURLS)
    #IMPORTS
    importandoClasesAgdb(ListFeatureClassLinea,UrlsDataSet[0],nombresFcL)
    importandoClasesAgdb(ListFeatureClassPolig,UrlsDataSet[1],nombresFcPol)
    importandoClasesAgdb(ListFeatureClassPunto,UrlsDataSet[2],nombresFcPun)
    importandoClasesAgdb(ListFeatureClassAux,UrlsDataSet[3],listUnionsNames)
    #lineas
    creandoTopologiaBasica(UrlGdb,nameTopo,dirLinealFC,dirLinealFC,dirLinealFC,rulesLine)
    #Poligonales
    creandoTopologiaBasica(UrlGdb,nameTopo,dirPolyFC,dirPolyFC,dirPolyFC,rulesPoly)
    #Puntos
    creandoTopologiaBasica(UrlGdb,nameTopo,dirPuntoFC,dirPuntoFC,dirPuntoFC,rulesPoint)
    #LINE-POLYGONE
    TopologiaAuxiliar(UrlGdb,nameTopo,"_LP",listUnionsURLS,urlsFC_LP,urlsFC_PL,rulesLP)
    #POLYGONE-LINE
    TopologiaAuxiliar(UrlGdb,nameTopo,"_Pl",listUnionsURLS,urlsFC_PL,urlsFC_LP,rulesPL)


CreateGdbAndCreateTopology(nombrePorDefectoGdb,FolderParaGuardarNuevaGdb,nombrePorDefectoTopologia,rutaActualGdb,zone)
