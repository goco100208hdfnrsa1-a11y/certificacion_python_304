promedio=float(input("ingresa el promedio:"))
if promedio>=0:
    print("ese promedio es muy bajo")
elif promedio>5 and promedio<=7:
    print("tu promedio es  bajo")
elif promedio>7  and promedio<=9:
    print("tu promedio es  normal")
elif promedio>9 and promedio <=10:
    print("tu promedio es excelente")
else:
    print("Ese promedio no existe")