''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''
    
print("1. Imprimir una cadena de <<hola mundo>>")
print("hola mundo")

print("\n2. Imprimir dos números")
x, y = (4,7)
print(x,y, sep=', ')
nom = "Melissa Matias"

print("\n3. Imprimir dos números y una cadena que represente tu nombre")
print(x,y, nom, sep=", ")

print("\n4. Imprimir 5 números separados por asteriscos *")
a, b, c = (22, 68, 35)
print(a,b, c, x,y, sep="*")

print("\n5. Imprimir 3 números en 3 funciones print() diferentes, pero la salida de los 3 números debe aparecer en una sola línea")
print(a, end=" ")
print(b, end=" ")
print(c)

print("\n6. Imprimir tu nombre y despues imprimir tu edad en funciones print() distintas pero la salida debe aparecer con un\nguión bajo separando los datos:  Abraham Lázaro_21")
age=19
print(nom, end=" _")
print(19)

print("\n7. Imprimir 3 números en 3 líneas distintas usando solo una función print()")
print(a,b,c,sep="\n")