carrito=[]
n_productos=int(input("Ingresa el numero de prductos"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu carrito")
    carrito.append(producto)
print("Lista creada correcta mente")
carrito[0]="barritas"
print(carrito[0])
print(carrito[1])
print(carrito)