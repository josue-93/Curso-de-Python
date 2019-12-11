print("datos de la primera persona")

#Para cargar por teclado una cadena de caracteres utilizamos la FUNCIÓN input
#Las variables pueden tener muchas funciones aquí tienes una la utilizamos para almacenar el valor introducido por teclado
nombre1=input("ingrese nombre del producto:")
precio1=int(input("ingrese un precio:"))
nombre2=input("ingrese nombre del producto:")
precio2=int(input("ingrese un precio:"))

#Esta es una constante
BONIFICACION = 20
#operadores estas comillas son para poner comentarios mas largos de una linea """
#Para comentarios de una linea utilizamos estos signos #
#Suma los dos precios y los resultados los ponemos en una variable
precio_compra_total = precio1 + precio2 #Operador aritmetico 
#comparamos si el precio1 es mayor o igual a precio2
comparar = precio1>=precio2 #Operador comparacion
logico = (precio1 < precio2 and precio1 == precio2) # operador logico

cabecera="resultado del producto {0}. y del producto. {1}.:"
# contatenamos las cadenas de texto de varias formas aqui tenemos una con las funcion format
print (cabecera.format(nombre1, nombre2))
print ("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print (comparar)
#contatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print ("la suma de los dos productos es:" + str(precio_compra_total))
print ("precio1 < precio2 and precio1 == precio2")
print (logico)
#Veamos el poder de asignacion aqui abajo
precio_compra_total += BONIFICACION #Operador de asignacion
print ("al precio total le incrementamos su valor que tiene la constante:" + str(precio_compra_total))
