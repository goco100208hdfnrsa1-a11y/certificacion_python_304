mapa=[
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#Rrecorriendo la matriz en siclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):
     for j in range(columnas):
         #verificamos si encontramos el tesoro
             if mapa[i][j]=="X":
              print(f"Mapa encontrado en la pasicion = [i][j]")