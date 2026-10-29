tabla=[
    ["nombre","edad","calificacion"],
    ["sintia",16,8.0],
    ["valeria",16,8.0],
    ["maria",16,8.0],
    ["ulices",16,8.0],
    ["mariel",16,8.0],
    ["sherlyn",16,8.0],
    ["jorge",16,8.0],
    ["capi",16,8.0],
    ["ximena",16,8.0],
    ["ximena2",16,8.0]

]
filas=len(tabla)
columnas=len(tabla[0])
buscar=input("introduce el nombre")
for i in range(filas):
     for j in range(columnas):
         #verificamos si encontramos el tesoro
              if tabla[i][j]== buscar:
               print(f"nombre encontrado: (buscar)")
               print(f"Mapa encontrado en la pasicion = [{i}][{j}]")