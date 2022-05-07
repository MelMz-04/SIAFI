''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.10.4 en windows 10 versión 21H1'''
    
print("1. Generar una lista vacia")
a = []
print(a)

print("2. Generar una lista mediante una cadena")
cad = "hola"
list = [cad]
print(list)

print("3. Generar una lista con 10 números y mostrar los items con indices pares (incluyendo el cero)")
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
  if list.index(i)%2 == 0:
    print(i)

print("3. Generar una lista con 10 números y mostrar los items con indices pares (incluyendo el cero)")
a = [1,2,3,4,5,6,7,8,9,10]
b = [56,29,80,32,20,17,62,94,46,72]
a += b
for i in a:
  if a.index(i)%2 == 0:
    print(i)

print("""5. Generar una lista con 5 números, imprimirla y  realizar lo siguiente (usar input):
  \tGenerar una copia de la lista original
  \tAgregarle un número, mostrar la lista
  \tAgregarle un número al inicio de la lista, mostrar la lista
  \tAgregarle una cadena en el indice que el usuario desee, mostrar la lista
  \tUsar el método remove para eliminar el primer número que el usuario insertó, mostrar la lista
  \tUsar el método pop para eliminar el último item de la lista y mostrarlo, mostrar la lista
  \tUsar el comando del y la función len() para eliminar la mitad de la lista, mostrar la lista
  \tA la lista añadirle los elementos de la lista copia que generamos al principio, mostrar la lista
  \tPedirle al usuario un número y mostrar cuantas veces aparece este número en la lista y mostrarlo
  \tRevertir el orden de la lista, mostrar la lista
  \tOrdenar la lista, mostrarla
  \tLimpiar o vaciar la lista""")
l = []
for i in range(5):
  x = int(input("Escribe un número entero: "))
  l.append(x)
print(l)

b = l.copy()
print(b)

x = int(input("Escribe un número entero: "))
l.append(x)
print(l)

x = int(input("Escribe un número entero: "))
l.insert(0,x)
print(l)

y = input("Escribe una palara: ")
x = int(input("Escribe un número donde insertar la palabra arriba de "+ str(int(len(l)/2))+": "))
l.insert(x,y)
print(l)

x = l[0]
l.remove(x)
print(l)

tam = len(l)
eliminado = l.pop(tam-1)
print(l, eliminado)

del l[int(tam/2):]
print(l)

l.extend(b)
print(l)

x = int(input("Escribe el número que quieres ver repetido: "))
print(l.count(x))

l.reverse()
print(l)

l.sort()
print(l)

l.clear()
print(l)