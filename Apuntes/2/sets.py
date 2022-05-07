#ejemplo 1
conjunto = set()
print(conjunto)
conjunto = {1,2,3,4,5,6,7}
print(conjunto)
conjunto = set([1,1,1,1,2,3,3,4])
print(conjunto)
conjunto = set("abecedario")
print(conjunto)
conjunto = set({1:"fresa",2:"manzana"})
print(conjunto)

#ejemplo 2
conjunto = {1,2,3,4,5,6,7}
print(conjunto)
conjunto.add(10)
print(conjunto)
conjunto.add(10)
print(conjunto)

#ejemplo 3
conjunto = {1,2,3,4,5,6,7}
print(conjunto)
conjunto.update({0,9,8,7,6,5,4})
print(conjunto)

#ejemplo 4
conjunto = {1,2,3,4,5,6,7}
print(conjunto)
conjunto.remove(1)
print(conjunto)
conjunto.remove(1)
print(conjunto)

#ejemplo 5
conjunto = {1,2,3,4,5,6,7}
print(conjunto)
conjunto.discard(1)
print(conjunto)
conjunto.discard(1)
print(conjunto)

#ejemplo 6
A = {1,2,3,4,5}
B = {7,6,5,4,3}
print(A)
print(B)
print(A.difference(B))
print(B.difference(A))

#ejemplo 7
A = {1,2,3,4,5}
B = {7,6,5,4,3}
print(A)
print(B)
print(A.intersection(B))
print(B.intersection(A))

#ejemplo 8
A = {1,2,3,4,5}
B = {7,6,5,4,3}
print(A)
print(B)
print(A.union(B))

#ejemplo 9
A = {1,2,3,4,5}
B = {4,3}
print(A)
print(B)
print(B.issubset(A))

#ejemplo 10
A = {1,2,3,4,5}
B = {4,3}
print(A)
print(B)
print(A.issuperset(B))

#ejemplo 7
A = {1,2,3,4,5}
B = {7,6,5,4,3}
print(A)
print(B)
print(A | B)
print(A & B)
print(A - B)

#ejemplo 12
A = {1,2,3,4,5}
print("Función len: ",len(A))
print(1 in A)
print("Función max: ",max(A))
print("Función min: ",min(A))
print("Función sorted: ",sorted(A))
del A