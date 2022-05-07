''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''
    
print("1. Guardar en la variable A un número dado por el usuario")
A = input("Escribe un número: ")

print("\n2. Imprimir el valor de la variable A")
print("El valor de tu número es: ",A)

print("\n3. Imprimir el tipo de dato de la variable A")
print(type(A))

print("\n4. Guardar en la variable B un nombre e imprimirlo")
B = input("Escribe un nombre: ")
print("Escribiste el nombre: ",B)

print("\n5. Pedir dos palabras, guardarlas en la variable nombre1 y nombre2 \nrespectivamente, e imprimirlos separados por comas")
print("Escribe 2 palabras")
nombre1, nombre2 =input(), input() 
print("Tus palabras son:", end=" ")
print(nombre1, nombre2, sep=", ")

print("\n6. Pedir un número y guardarlo en la variable x, después transformar \nen un número flotante esta variable e imprimir su tipo de dato con la función type()")
x = float(input("Escribe un número: "))
print(type(x))

print("\n7. Pedir un número y guardarlo en la variable x ya transformado en un número flotante")
x = float(input("Escribe un número: "))
print(x)