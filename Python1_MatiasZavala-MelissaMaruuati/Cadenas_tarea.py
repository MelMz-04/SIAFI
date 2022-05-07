''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''
    
print("1. Crear una cadena de tipo parrafo con un poema")
poema = """
\t <<Dolor>> 
\tAlfonsina Stormi\n
Quisiera esta tarde divina de octubre
pasear por la orilla lejana del mar;
que la arena de oro, y las aguas verdes,
y los cielos puros me vieran pasar.

Ser alta, soberbia, perfecta, quisiera,
como una romana, para concordar
con las grandes olas, y las rocas muertas
y las anchas playas que ciñen el mar.

Con el paso lento, y los ojos fríos
y la boca muda, dejarme llevar;
ver cómo se rompen las olas azules
contra los granitos y no parpadear;
ver cómo las aves rapaces se comen
los peces pequeños y no despertar;
pensar que pudieran las frágiles barcas
hundirse en las aguas y no suspirar;
ver que se adelanta, la garganta al aire,
el hombre más bello, no desea amar…

Perder la mirada, distraídamente,
perderla y que nunca la vuelva a encontrar:
y, figura erguida, entre cielo y playa,
sentirme el olvido perenne del mar.
"""
print(poema)

print("\n2. Crear una cadena de tipo parrafo con un haiku, usar caracteres especiales y el caracter de scape para darle formato ")
haiku = "\t    Pasó el ayer,\n\tpasó también el hoy;\n\t se va la primavera\n\t\t\"Yosa Buson\""
print(haiku)

print("\n3. Crear una cadena de tipo parrafo con un poema y mediante slicing imprimir el primer verso")
poema = """
\t <<No te preocupes>> 
\t\tAnónimo\n
No te preocupes, aquí estoy
que yo también he sufrido
así que sé lo que has perdido
y te acompaño en estas penas
lo mismo que nos hemos reído
pues para eso es un amigo
no temas;
no me voy.
"""
print("Primer verso:\n",poema[35:62],sep="")

print("\n4. Crear una cadena de tipo parrafo con un poema y mediante slicing e indices negativos imprimir el último verso")
poema = """
\t <<Amor desarraigado>> 
\tCarmen Matute\n
AMOR DESARRAIGADO
Bajo el ala de la noche
que deja
su huella imprecisa
bajo la sombra
del corazón repudiado
rumores de vidrio
rozan el sueño esquivo.

En esa hora que rezuma olvida,
en esa hora secreta y desgarrada,
la piel que me contiene
se llena de nostalgia y latidos.

Desarraigado
el amor
acaricia
la entreabierta herida
que sangra.
"""
print("El último verso es:\n",poema[-12:-1],sep="")

print("\n5. Pedir una palabra")
p = input("Escribe una palabra: ")
print(p)

print("\n6. Pedir una oración")
o = input("Escribe una oración: ")
print(o)

print("\n7. Pedir varias oraciones y crear un parrafo")
print("Escribe 3 oraciones")
or1, or2, or3 = input("Primera: "), input ("Segunda: "), input("Tercera: ")
print("\nTus oraciones quedan:",or1, or2, or3, sep="\n")

print("\n8. Pedir una oración y determinar la cantidad de caracteres (contando espacios) que tiene")
o = input("Escribe una oración: ")
print("Tu oración tiene: ", len(o), "carácteres ")

print("\n9. Pedir una oración y determinar si la letra x se encuentra en la oración")
o = input("Escribe una oración: ")
print("La letra x se encuentra en la oración",'x' in(o))

print("\n10. Crear una oración e imprimirla asegurando que no existen espacios al inicio y al final de la oración, imprimirla en mayúsculas y en minúsculas")
oracion = " La luna esta preciosa esta noche "
print(oracion.strip().upper())
print(oracion.strip().lower())

print("\n11. Pedir una oración y cambiar todos los espacios por guiones bajos")
o = input("Escribe una oración: ")
print(o.replace(" ","_"))

print("\n12. Pedir una oración y cambiar los primeros 3 espacios por puntos")
o = input("Escribe una oración: ")
print(o.replace(" ",".",3))

print("\n13. Pedir los datos de 3 alumnos (nombre, apellido, edad y carrera) e \nimprimirlos de forma que se pueda ver una tabla")
print("Escribe los siguientes datos de 3 alumnos (nombre, apellido, edad y carrera)")
datos = "Nombre, Apellido, Edad, Carrera"
a1 = input("Alumno 1: ")
a2 = input("Alumno 2: ")
a3 = input("Alumno 3: ")

print(datos.split(sep=','),a1.split(sep=','), a2.split(sep=','), a3.split(sep=','), sep="\n")