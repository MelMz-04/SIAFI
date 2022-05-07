'''
#ejemplo 1
z = "hola mundo"
print(z)
z = """hola
mundo
que tal?"""
print(z)

#ejemplo 2
a = "\t es una tabulación"
b = "\n es un salto de linea"
c = "\" es una comilla"
print(a)
print(b)
print(c)

#ejemplo 3
z = "hola_mundo"
print(z)
print(z[4])

#ejemplo 4
print("slicing toma 3 valores, inicio, fin y paso")
print("z:",z)
print("z[2:]: ",z[2:])
print("z[2:5]: ",z[2:5])
print("z[:5]: ",z[:5])
print("z[1:8:2]: ",z[1:8:2])
print("z[::2]: ",z[::2])

#ejemplo 5
sli = slice(1,100,2)
print(sli)
c1 = "hola_mundo, como estan?"
c2 = "muy bien, que hace el programa?"
print(c1)
print(c2)
print("c1 con slice: ",c1[sli])
print("c2 con slice: ",c2[sli])

#ejemplo 6
z = "hola_mundo"
print("z[-1]: ",z[-1])
print("z[-8:-1:2]: ",z[-8:-1:2])

#ejemplo 7
z = "hola_mundo"
print("tamaño de la cadena: ",len(z))

#ejemplo 8
z = "hola_mundo"
if "hola" in z:
  print("si esta \"hola\" en la cadena")
if "hola" not in z:
  print("no esta \"hola\" en la cadena")


#ejemplo 9
cadena = "    Hola Mundo    "
print(cadena.strip())
print(cadena.upper())
print(cadena.lower())
print(cadena.strip().lower())

#ejemplo 10
cadena = "Hola mundo"
print("reemplazando la letra o por x")
print(cadena.replace("o","x"))
print("reemplazando la letra o por x una sola vez")
print(cadena.replace("o","x",1))

#ejemplo 11
cadena = "Lazaro,Abraham,21"
print("Separación por comas:")
print(cadena.split(","))
print("Separación por comas 1 vez:")
print(cadena.split(",",1))

#ejemplo 12
a = "hola mundo {}".format("Abraham")
print(a)

#ejemplo 13
b = "Este {} es un programa utilizando {}"
print(b.format("programa","format"))

#ejemplo 14
b = "Este {1} es un programa utilizando {0}"
print(b.format("format","programa"))

#ejemplo 15
nombre = "Luis"
c = """{alumno} es el mejor programador, 
como {prof}, practicando podra volverse {0}"""
print(c.format("un buen programador",alumno=nombre,prof="Lazaro"))

#ejemplo 16
d = """El número {0:d} es entero 
{1:f} es un flotante,
{2:.2f} es el mismo pero solo con dos decimales.
{3:.0f} también es un flotante pero sin decimales, 
{4:s}"""
print(d.format(100,100.123456678,100.123456678,100.123456678,"hola"))

#ejemplo 17
e = "{0:b} es binario".format(100)
print(e)

#ejemplo 18
f = "{0:o} es octal".format(100)
print(f)

#ejemplo 18.1
f = "{0:x} es hexadecimal".format(100)
print(f)

#ejemplo 19
n1 = "Paco"
a1 = "Perez"
e1 = 20
template = "{0:^20},{1:<20} tiene {2:>5}"
print(template.format(n1,a1,e1))

template = "{0:*^20},{1:-<20} tiene {2:+>5}"
print(template.format(n1,a1,e1))
'''
#ejemplo 20
template = "|{0:^20s}|{1:^20s}|{2:^6}|\n"
separacion = "|{0:-^48}|\n".format("")
cadenaImprimible = template.format("nombre","apellido","edad")
cadenaImprimible += separacion
cadenaImprimible += template.format("Abraham","Lázaro",21)
cadenaImprimible += template.format("Sofia","Pilloni",20)
cadenaImprimible += template.format("Marco","Jeronimo",27)
print(cadenaImprimible)
