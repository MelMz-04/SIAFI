''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''
    
print("1. Mediante la función input() pedir un número al usuario, transformarlo en número entero, flotante y complejo")
a = input("Escribe un número: ")
print(int(a))
print(float(a))
print(complex(a))

print("\n2. Pedir al usuario un número entero para la variable x, transformar e imprimir esta x como número flotante y complejo")
x = int(input("Escribe un número: "))
print("Número flotante: ",float(x),"\nNúmero complejo: ",complex(x))

print("\n3. Pedir al usuario un número flotante para la variable x, transformar e imprimir esta x como número entero y complejo.")
x= float(input("Escribe un número con decimal: "))
print("Transformando a entero y complejo respectivamente: ",int(x),",",complex(x))

print("\n4. Pedir al usuario un número complejo para la variable x, imprimir la parte real y la parte imaginaria de este número complejo")
x = complex(input("Escribe un número complejo (Ejemplo-> 5+10j): "))
print("Su parte real es:",int(x.real), "y su parte imaginara: ",float(x.imag))

print("\n5. Pedir dos números para las variables A y B, usando la notación cientifica, y crear un número complejo con la variable B como \nparte real y la variable A como imaginaría, imprimir el número")
print("Escribe 2 números complejos")
A,B= complex(input("Primer número: ")), complex(input("Segundo número: "))
print("El número formado por ambos es: ", int(A.real),"+",int(B.imag),"j",sep="")