'''#ejemplo 1
x = 10
y = 3.1416
z = 10+10j

print("x: ",type(x))
print("y: ",type(y))
print("z: ",type(z))

#ejemplo 2
numero_cientifico = 21.23E-4+12e10j
print("número cientifico: ",numero_cientifico)

#ejemplo 3
x = 10
print("x pasado de entero a flotante")
xfloat=float(x)
print(xfloat," es: ",type(xfloat))
y=3.1416
print("y pasado de flotante a entero")
yint= int(y)
print(yint,"es: ",type(yint))

#ejemplo 4
x = 10
y = 3.1416
print("x e y pasados como complejos")
print(complex(x))
print(complex(y))
print(complex(x,y))

#ejemplo 5
z = 10+10j
print(z)
print("parte real: ",z.real)
print("parte imaginaria: ",z.imag)
print("parte real como entera: ",int(z.real))
print("parte imaginaria como flotante",float(z.imag))

#ejemplo 6
print("casteo de cadenas a valores numericos y biseversa")
print("cadena a número")
x = "10+10j"
print(x)
print(complex(x))
print(type(complex(x)))
print("número a cadena")
y = 10+10j
print(y)
print(str(y))
print(type(str(y)))

#ejemplo 7
print("conjugado de números complejos y magnitud")
z = 10+10j
print(z)
print("magnitud: ",abs(z))
print("conjugado: ",z.conjugate())
'''