#ejemplo 1
lista = list()
print(lista)
lista = []
print(lista)
lista = ["hola",1,2,3.426,True,[]]
print(lista)
#podemos generar listas a partir de objetos iterables
lista = list("hola")
lista = list((1,2,3,4))
lista = list({1,2,3,4})
lista = list([1,2,3,4])

#ejemplo 2
lista = [1,2,3,4,5]
print(lista)
lista[2] = 0
print(lista)

#ejemplo 3
lista = [0,1,2,3,4,5,6,7,8,9]
print(lista)
print("lista[2:8]: ",lista[2:8])
print("lista[2:8:2]: ",lista[2:8:2])

#ejemplo 4
lista = [1,2,3,4,5]
print(lista)
lista.append(10)
print(lista)

#ejemplo 5
lista = [1,2,3,4,5]
print(lista)
lista.insert(3,10)
print(lista)
#indice negativo
lista.insert(-3,11)
print(lista) 
#fuera del rango
lista.insert(100,12)
print(lista)
#fuera del rango y negativo
lista.insert(-100,13)
print(lista)

#ejemplo 6
lista = [1,2,3,4,5,5,5]
print(lista)
#remueve el primero en encontrar
lista.remove(5)
print(lista)
#remove de items mediante autoreferencia
lista.remove(lista[2])
print(lista)
#indica un error en caso de no encontrar el item
lista.remove(10)
print(lista)


#ejemplo 7
lista = [1,2,3,4,5]
print(lista)
a = lista.pop()
print(lista)
print("Elemento que se sacó: ",a)

#ejemplo 8
lista = [0,1,2,3,4,5,6,7,8,9]
print(lista)
del lista[0]
print(lista)
#del con slicing
del lista[2:8:2]
print(lista)

#ejemplo 9
A = [1,2,3,4,5]
B = A.copy()
A.append(6)
B.pop()
print(A)
print(B)

#ejemplo 10
lista = [1,2,3,4,5]
print(lista)
lista.extend([6,7,8,9])
print(lista)
#podemos extender la lista mediante una concatenación
lista += [10,11,12,13]

#ejemplo 11
lista = [1,2,3,4,5]
print(lista)
lista.clear()
print(lista)

#ejemplo 12
lista = [1,2,3,4,5,5,5,5]
print(lista)
print("se encontraron: ",lista.count(5)," veces el 5")

#ejemplo 13
lista = [1,2,3,4,5]
print(lista)
print("El número 1 se encuentra en el indice ",lista.index(1))
print("El número 3 se encuentra en el indice ",lista.index(3))
print("El número 5 se encuentra en el indice ",lista.index(5))

#ejemplo 14
lista = [1,2,3,4,5]
print(lista)
print("lista volteada: ",lista.reverse())

#ejemplo 15
lista = [1,2,3,4,5]
print(lista)
print("Ordenamiento básico")
print(lista.sort())
print("Ordemaniento inverso")
print(lista.sort(reverse=True))
print("Ordenamiento por función")
def f1(lista):
  return len(lista)
print("se ordena por medio del tamaño de la palabra")
lista = ["manzana","fresa","pera","mango","platano"]
print(lista)
print(lista.sort(reverse=True,key=f1))

#ejemplo 16
lista = [3,5,7,8,4,3,2,5,7,8,3,1,0]
print(lista)
print("Función max: ",max(lista))
print("Función min: ",min(lista))
print("Función sorted: ",sorted(lista))
