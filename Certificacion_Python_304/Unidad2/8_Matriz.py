#Creamos una Matriz
numeros=[
    [1,2,3],#fila 0
    [2,3,4],#fila 1
    [5,6,7]#fila 2
]
#Obtenido el numero de filas
filas=len(numeros)#filas=3
#Obtenido el numero de columnas
columnas=len(numeros[1])
#Ciclo externo para indices de las filas(i)
for i in range(filas):
    #Ciclo imterno pra los indices de las columnas
    for j in range(columnas):
      print(f"[{i}][{j}]= {numeros[i][j]}")