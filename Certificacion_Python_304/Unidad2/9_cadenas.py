cadena1= 'Hola'
cadena2='mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repeticiones
eco="ja"*3
print(eco)
tu_nombre='oscar'
print(tu_nombre.upper())
print(tu_nombre.lower())
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#for,ato de cadenas (F-string)
edad=16
nombre='oscar'
mensaje=f"Hola , me llamo {nombre} y tengo {edad} años"
print(mensaje)
texto= "¡Feliciddes por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
oracion="aprender python es divetido"
if"java"in oracion:
    print("encontrado")
else:
 print("no esta")
 nlista="oscar"
 print(nlista.isalpha())
 print(nlista.isdigit())