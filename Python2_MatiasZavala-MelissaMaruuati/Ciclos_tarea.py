''' Autor: Melissa Maruuati Matias Zavala
    Hecho con python 3.9 en windows 10 versión 21H1'''

print("1. Realizar un programa para encontrar los primeros 20 números primos")
x=1
i=1
while i <=20:
  x+=1
  #print("i",i)
  if (x==2 or x==3 or x==5 or x==7) or (x%3!=0 and x%2!=0 and x%5!=0 and x%7!=0):
    print(x)
    i+=1

print("\n2. Realizar un programa que te regrese el factorial de un número n")
f=int(input("Escribe hasta que factorial deseas calcular: "))
a=1
for i in range(1,f+1,1):
    a=a*i
print("El resultado de tu factorial es: "+str(a))

print("\nRealiza un programa con el que podamos almacenar información de alumnos. Desde un menú se podrán realizar operaciones  de creación de alumno, actualización de alumno, eliminación de alumno y generación de reportes (tablas). Los datos de los alumnos seran nombres, apellidos, número de cuenta, fecha de nacimiento y carrera. El programa no detendrá su ejecución hasta que el usuario indique en el menú principal una salida con una de las opciones")
