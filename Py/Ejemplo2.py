#Utilizamos funciones input para introducir valores por el teclado
sueldo=int(input("introduce el sueldo:"))
#condicional if 
if sueldo>3000:
    print("El usuario tiene que pagar un porcentage en impuestos")
if sueldo<=3000: #operador de comparacion
    print("El usuario esta exento de declarar su renta")

if sueldo>6000 and sueldo<10000: #Operador logico se tienen que cumplir las dos condiciones
    print("El usuario tiene que pagar una bonificacion de 1000 pesos")
if sueldo==20000 or sueldo==30000: #operador logico solo se tiene que cumplir una de las dos condiciones
    print("El usuario paga un 10 por ciento de su sueldo")
