'''
#ejemplo 1
frutas = ["manzana","fresa","kiwi"]
for x in frutas:
  print("La fruta es: ",x)


#range
A = list(range(20,0,-5))
print(A)
print(range(20,0,-5))

#ejemplo 2
frutas = ["manzana","fresa","kiwi"]
for i in range(3):
  print(frutas[i])

for i in range(0,3):
  print(frutas[i])

for i in range(0,3,2):
  print(frutas[i])

for i in range(0,101,5):
  print(i) 
#ejemplo 3

letras = list("Abraham Lazaro")

for x in letras:
  if x == "a":
    continue
  print(x)

for x in letras:
  if x == " ":
    break
  print(x)
'''
#ejemplo 4
letras = "abecedario"
for x in letras:
  print(x)
else:
  print("Se terminó el ciclo")
'''
#ejemplo 5
letras = list("otorrinolaringologo")
vocales = list("aeiou")
vocales_en_letras = []
i = 0
while i<len(letras):
  print("Letra ",i+1,": ",letras[i])
  if letras[i] in vocales and letras[i] not in vocales_en_letras:
    vocales_en_letras.append(letras[i])
  print("es vocal") if (letras[i] in vocales) else print("es una consonante")
  i+=1
else:
  print("termina el ciclo")
  print(vocales_en_letras)

#list compehension
A = [x for x in range(0,20,1)]
print(A)

#reversed
A = [x for x in range(0,20,2)]
print(A)
print(type(A))
print(reversed(A))
print(type(reversed(A)))

B = range(20,0,-2)
print(type(B))
print(type(reversed(B)))

C = tuple(x for x in range(1,5))
print(type(C))
prit(type(reversed(C)))
'''