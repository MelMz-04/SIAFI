''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.10.4 en windows 10 versión 21H1'''
import numpy as np
print("1. Generar una tupla que contenga las 5 vocales del abecedario")
abc = ('a','e','i','o','u')
print(abc)

print("\n2. Generar una tupla que contenga las demás letras (consonantes del abecedario)")
dario = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
print(dario)

print("\n3. Generar una tupla que contenga las dos tuplas anteriores")
con = (abc,dario)
print(con)

print("\n4. Generar una tupla que contenga las dos tuplas anteriores pero transformadas en lista (la tupla tendrá como items dos listas, la de vocales y la de consonantes)")
jun = list(abc)
tas = list(dario)
tup = (jun,tas)
print(tup)

print("\n5. Desempaquetar esta última tupla y mediante el desempaquetado, sumar los iterables para después generar una lista con todas las letras del abecedario, ordenarla y transformarla en tupla")
x,y = tup
alfabeto = (sorted(x+y))
print(alfabeto)
'''x=[]
for i in tup:
  if tup.index(i)<len(tup):
    x = x+i
alfabeto = (sorted(x))
print(alfabeto)'''

print("\n6. Comparar la tupla generada en el ejercicio 5 con la generada en el ejercicio 3, ¿Qué resulta?")
print("La tupla del ejercicio 3 es igual al del ejercicio 5:", con == alfabeto)

print("""\n7. Dada la tupla:
  \t([1,"b",4,-99,10+1j,"b","c",True,"z","hola",1,-999,-5,1-1j,False],[],[],[])
  \t7.1 Manejar las listas de la tupla de tal manera que en la primera aparezcan puros números, en la segunda puras cadenas, en la tercera números complejos y en la última los booleanos.
  \t7.2 Tratar de ordenar las listas y generar una tupla con la concatenación de cada una de las listas de la tupla.""")
tup = ([1,"b",4,-99,10+1j,"b","c",True,"z","hola",1,-999,-5,1-1j,False],[],[],[])
a,b,c,d = tup
for i in a:
  if type(i) == bool:
    d.append(i)
    a.remove(i)
  if i == True:
    a.remove(i)
for i in a:
  if type(i) == str:
    b.append(i)
    a.remove(i)
  if type(i) == complex:
    c.append(i)
    a.remove(i)
for i in a:
  if type(i) == str:
    b.append(i)
    a.remove(i)
for i in a:
  if type(i) == str:
    b.append(i)
    a.remove(i)
print(c)
a = sorted(a)
b = sorted(b)
c = np.sort_complex(c)
d = sorted(d)
tupla = a,b,c,d
print(tupla)