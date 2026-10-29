numero=int(input("ingresa un numero del 1 al 10:"))

if numero >= 1 and numero <= 10:
    print("tabla de multiplicar del", numero)

    for i in range(1,11):
        resultado = numero * i
        print(numero,"x", i, "=",resultado)
else:
        print("Error:El numero debe estar entre 1 y 10")