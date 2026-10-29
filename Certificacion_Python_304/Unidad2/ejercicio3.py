letras=[['A','B','C','D','E','F','G'],
        ['H','I','J','K','L','M','N'],
        ['Ñ','O','P','Q','R','S','T'],
        ['U','V','W','X','y','z',''],]
filas=4
columnas=7
for i in range(filas):
    for j in range(columnas):
       print(f"[{i}][{j}]= {letras[i][j]}")
