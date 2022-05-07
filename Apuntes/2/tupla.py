#ejemplo 1
#con o sin parentesis
A = (1,2,3,4)
print(A)
A = 1,2,3,4
print(A)
#de un solo elemento
A = (1,)
print(A)
A = 1,
print(A)
print(type(A))
#con un iterable
A = ("hola")
print(A)
A = tuple([1,2,3,4,5])
print(A)
#vacias
A = ()
print(A)
A = tuple()

#ejemplo 2
A = ([1,2],[3,4])
print(A)
print(A[0].append(10))
print(A[0].reverse())
print(A[1].clear())

#ejemplo 3
A = (1,2,3,4,5)
print(A)
print(A[1])

#ejemplo 4
A = (1,2,3,4,5)
print(A)
print(A[1:4])

#ejemplo 5
A = (1,2,3,4,5)
print(A)
print(A[-1])

#ejemplo 6
lista = [1,2,3,4,5]
print(lista)
tupla = tuple(lista)
print(tupla)
lista = list(tupla)
print(lista)

#ejemplo 7
A = (1,2,3,4,5)
print(A)
print("La tupla tiene ",len(A)," elementos")
print("Función max: ",max(A))
print("Función min: ",min(A))
print("Función sorted: ",sorted(A))

#ejemplo 8
A = (1,2,3,4,5)
print(A)
print(1 in A)

#ejemplo 9
A = (1,2)
B = (3,4)
print(A)
print(B)
print(A+B)

#ejemplo 10
tupla = ([1,3,5,7],[0,2,4,6],[1,2,3,5,7,11])
print(tupla)
x,y,z=tupla
print(x)
print(y)
print(z)