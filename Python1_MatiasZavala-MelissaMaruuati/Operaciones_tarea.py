''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''

print("1. Pedir al usuario dos números y sumarlos")
print("Escribe dos números para sumar: ")
a, b = input(), input()
print(int(a)+int(b))

print("\n2. Pedir al usuario dos números y restarlos")
print("Escribe dos números para restar: ")
a, b = input(), input()
print(int(a)-int(b))

print("\n3. Pedir al usuario dos cadenas y concatenarlas")
print("Escribe dos palabras")
a = input("Primera palabra: ")
b = input("Segunda palabra: ")
print(a+" "+b)

print("\n4. Pedir al usuario una cadena y repetirla 5 veces")
c = input("Escribe una palabra: ")
c = c + " "
print(c*5)

print("\n5. Pedir al usuario un número y mostrar si es múltiplo de dos (sin condiciones)")
x = input("Escribe un número: ")
print("Es múltiplo de 2",int(x)%2==0)

print("\n6. Pedir al usuario dos números y mostrar si son iguales")
print("Escribe dos números")
a, b = input(), input()
print("Los números son iguales",a==b)

print("\n7. Pedir al usuario dos números y mostrar si la raiz del primero es mayor a la raiz del segundo")
print("Escribe dos números")
a, b = int(input()), int(input())
print("La raíz de a es mayor que b",a>b)

print("\n8. Pedir al usuario dos números a y b, y mediante pitagoras encontrar una c que sea la raiz de \nla suma de a y de b al cuadrado")
print("Escribe dos números")
a, b = int(input()), int(input())
c= (a+b)**(0.5)
print("Por teorema de pitágoras c es igual a",c)

print("\n9. Pedir al usuario dos números y mostrar si el cubo del primer número y el cubo del segundo número es mayor a 0")
print("Escribe dos números")
a, b = int(input()), int(input())
print("a^3 y b^3 son mayor a 0", (int(a**3)&int(b**3))>0)

print("\n10. Pedir al usuario 3 números a, b y c, y usando la formula general encontrar las raices de un \npolinomio de tipo ax^2+bx+c=0.")
print("Escribe 3 números")
a, b, c = int(input()), int(input()), int(input())
r1 = (-b+(((b**2)-(4*a*c))**(0.5)))/(2*a)
r2 = (-b+(((b**2)-(4*a*c))**(0.5)))/(2*a)
print("Las raíces del polinomio son : ",str(r1),"y",str(r2))

print("11. Pedir dos nombres, y determinar si el segúndo nombre tiene más letras que la primera")
print("Escribe dos nombres: ")
nom1, nom2 = input("Nombre 1: "), input("Nombre 2: ")
print("El segundo nombre tiene más letras que el primer nombre", len(nom2)>len(nom1))

print("\n12. Pedir un número y mostrar si este es multiplo de 2 y mayor a 10")
x = input("Escribe un número: ")
print("Es múltiplo de 2 y mayor que 10",(int(x)%2==0)&(int(x)>10))

print("\n13. Pedir un número y mostrar si este es al menos múltiplo de 2 o de 3")
x = input("Escribe un número: ")
print("Es múltiplo de 2 o de 3",(int(x)%2==0)|(int(x)%3==0))

print("14. Pedir una oración al usuario e indicar si la letra <<x>> se encuentra dentro de la oración")
a = input("Escribe una oración: ")
print("La letra x esta en la oración",'x' in(a))

print("\n15. Indicar si la palabra <<programación>> se encuentra dentro de esa cadena'''")
a = input("Escribe una oración: ")
print("La letra x esta en la oración",'programación' in(a))