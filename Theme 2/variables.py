nombre = input("ingresa tu nombre: ")
ventas = input("cuanto vendiste?: ")

ventas = int(ventas)
comision = round(ventas * 0.13,2)

print(f" hola {nombre} tu comision es de : {comision}")