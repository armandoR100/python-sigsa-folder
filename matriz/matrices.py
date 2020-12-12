import random

def CreateSpaceMatrice(tam_ren, tam_col):
    matriz = []
    for i in range(tam_ren):
        matriz.append([0] * tam_col)
    return matriz

def crear_matriz_alea(f,c):
    matriz = CreateSpaceMatrice(f, c)
    for i in range(f):
        for j in range(c):
            matriz[i][j] = random.randint(0, 1)
    return matriz

def getSideLeft(matriz):
    posBarraIzquierda = []
    columna = 1
    for fila in range(len(matriz)):
        if(matriz[fila][columna] == 0):
            pos = [fila,columna]
            posBarraIzquierda.append(pos)   
    return posBarraIzquierda

def getSideUp(matriz):
    posBarraArriba = []
    fila = 1
    for columna in range(len(matriz)):
        if(matriz[fila][columna] == 0):
            pos = [fila,columna]  
            posBarraArriba.append(pos)           
    return posBarraArriba

def getSideRight(matriz):
    posBarraDerecha = []
    columna = len(matriz)-2
    for fila in range(len(matriz)):
        if(matriz[fila][columna] == 0):
            pos = [fila,columna]
            posBarraDerecha.append(pos)   
    return posBarraDerecha

def getSideDown(matriz):
    posBarraDerecha = []
    fila = len(matriz)-2
    for columna in range(len(matriz)):
        if(matriz[fila][columna] == 0):
            pos = [fila,columna]
            posBarraDerecha.append(pos)   
    return posBarraDerecha

def muestraEntradasCeros(PosIzq,PosDer,PosArriba,Posdebajo):
    print("PosIzq = ",PosIzq)
    print("PosDer = ",PosDer)
    print("PosArriba = ",PosArriba)
    print("Posdebajo = ",Posdebajo)        

def muestra_matriz(matrice):
    print("MATRIZ",len(matrice)," X ",len(matrice[0]) )
    for ren in range(len(matrice)):
        for col in range(len(matrice[0])):
            print(f'[{matrice[ren][col]}]', end=" ")
        print("")
  
def marco(matrice,num):
    matriz = matrice
    for i in range(0,len(matriz)):
        matriz[i][0] = num
        matriz[0][i] = num
        matriz[i][len(matriz)-1] = num
        matriz[len(matriz)-1][i] = num
    return matriz 

def movesValidatePos(i,j,matriz):
    if matriz[i][j] == 0:
        return True
    else:
        return False

def movesValidateAllPos(i,j,matriz):
    derecha = movesValidatePos(i,j+1,matriz)
    izquierda = movesValidatePos(i,j-1,matriz)
    arriba = movesValidatePos(i-1,j,matriz)
    abajo = movesValidatePos(i+1,j,matriz)
    listValida =[derecha,izquierda,arriba,abajo]
    return listValida

def moveDerecha(i,j,matriz,listValida):
    if listValida[0] == True:
        j = j+1
        poSave = [i,j]
        print("(0) mov hacia derecha matriz[i][j] =",i,j)
        return poSave
    else:
        poSave = [i,j]
        return poSave

def moveIzquierda(i,j,matriz,listValida):
    if listValida[1] == True:
        j = j-1
        poSave = [i,j]
        print("(1) mov hacia izquierda matriz[i][j] =",i,j)
        return poSave
    else:
        poSave = [i,j]
        return poSave

def moveArriba(i,j,matriz,listValida):
    if listValida[2] == True:
        i = i-1
        poSave = [i,j]
        print("(2) mov hacia arriba matriz[i][j] =",i,j)
        return poSave
    else:
        poSave = [i,j]
        return poSave

def moveAbajo(i,j,matriz,listValida):
    if listValida[3] == True:
        i = i-1
        poSave = [i,j]
        print("(3) mov hacia abajo matriz[i][j] =",i,j)
        return poSave
    else:
        poSave = [i,j]
        return poSave

def continuaDerecha(listValida,bandera,i,j,matriz):
    if listValida[0] == True:
        print("continua")
        bandera = "continua"
        pos_nueva = moveDerecha(i,j,matriz,listValida)
        i = pos_nueva[0]
        j = pos_nueva[1]
        listValida = movesValidateAllPos(i,j,matriz)
        print("pos_inicial_derecha=",pos_nueva," ,listavalida=",listValida)
    else:
        bandera = "no_continua"
        print("no continua a la derecha")    
    
def moves(pos,matriz):
    i = pos[0]   
    j = pos[1] 
    listValida = movesValidateAllPos(i,j,matriz)
    print("\npos_inicial m[i][j]=",i,j," ,listavalida=",listValida)
    
    pos_nueva = moveDerecha(i,j,matriz,listValida)
    i = pos_nueva[0]
    j = pos_nueva[1]
    listValida = movesValidateAllPos(i,j,matriz)
    print("pos_inicial_derecha=",pos_nueva," ,listavalida=",listValida)
    
    bandera = "continua"
    
    if bandera == "continua":
        continuaDerecha(listValida,bandera,i,j,matriz)

    
    # #derecha
    # if matriz[i][j+1] ==  0:
    #     print("--> 0 derecha")
    # else:
    #     print("1 derecha")
    #     #izquierda
    #     if matriz[i][j-1] == 0:
    #     	print("--> 0 izquierda")
    #     else:
    #         print("1 izquierda")
    #         #abajo
    #         if matriz[i+1][j] == 0: 
    #             print("--> 0 down")
    #         else:
    #             print("1 down")
    #             #arriba
    #             if matriz[i-1][j] == 0:
    #                 print("--> 0 up")
    #             else:
    #                 print("1 up")
  	    
         	
      	
 
renglon = 9     
columna = 9
matriceNueva = marco(crear_matriz_alea(renglon,columna),1)
#muestra_matriz(matriceNueva)

PosIzq = getSideLeft(matriceNueva)
PosArriba = getSideUp(matriceNueva)
PosDer = getSideRight(matriceNueva)
Posdebajo = getSideDown(matriceNueva)
muestraEntradasCeros(PosIzq,PosDer,PosArriba,Posdebajo)
#for i in range(0,len(PosIzq)):
#    movDerecha(PosIzq[i])

matriceNueva =  [[1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1, 0, 1, 1, 1], 
                 [1, 0, 0, 1, 1, 1, 1, 1, 1], 
                 [1, 0, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 0, 1, 1, 1, 1, 1, 1, 1], 
                 [1, 1, 1, 1, 1, 1, 1, 1, 1]]
muestra_matriz(matriceNueva)
PosIzq =  [[3, 1], [7, 1], [2, 5]]


moves(PosIzq[0],matriceNueva)
