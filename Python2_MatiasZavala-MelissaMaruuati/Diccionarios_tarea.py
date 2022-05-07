print("1. Generar un diccionario de números primos, donde la llave sea su posición y los valores los números primos (al menos 10)")
d = {}
x=1
i=1
while i <=20:
  x+=1
  #print("i",i)
  if (x==2 or x==3 or x==5 or x==7) or (x%3!=0 and x%2!=0 and x%5!=0 and x%7!=0):
    d[i]=x
    i+=1
print(d)

print("\n2. Pedirle al usuario su nombre completo, quitar los espacios de la cadena (usar método replace) enumerar las letras y generar un diccionario")
nom = input("Escribe tu nombre completo: ")
nom = nom.replace(" ","")
print(nom)
d = {}
for i in range(len(nom)):
  d[i] = nom[i]
print(d)

print("\n3. Generar un diccionario para 5 palabras traducidas en 2 o 3 idiomas distintos, usar listas y la función zip()")
esp = ["Hola","Gracias","Buenas noches","Computadora","Inteligencia artificial"]
ing = ["Hello","Thank you","Good Night","Computer","Artificial intelligence"]
jap = ["こんにちは","ありがとうございました","こんばんは","コンピューター","人工知能"]
dic = dict(zip(esp,(zip(ing, jap))))
print(dic)

print("\n4. Ocupar la notación de diccionarios anidados para generar una tabla con estas palabras y sus traducciones")
print("\t  Español, (Inglés, Japonés)")
for i in dic:
  print("Palabra: "+i+" ",dic[i])

print("\n5. Generar una lista con el nombre de 10 personas y otra con sus carreras, ocupar la función enumerate() para generar un diccionario de personas y la función zip() para generar un diccionario de carreras por medio de nombres de personas")
nom = []
carr = []
for i in range (2):
  x,y = input("Escribe un nombre: ") , input("Escribe la carrera: ")
  print("")
  nom.append(x)
  carr.append(y)
dic = dict(enumerate(nom,1))
print(dic)
carreras = dict(zip(nom, carr))
print(carreras)

print("""6. Generar un diccionario vacio
  \t6.1 Agregarle un item que contenga como llave True y que tenga como valor una lista de las posibles formas en que se pueda escribir si (SI,si,Si,etc)
  \t6.2 Agregarle un item que contenga como llave False y que tenga como valor una lista de las posibles formas en que se pueda escribir no \n\t (No, no, NO, nop, etc)
  \t6.3 Pedirle al usuario una palabra. Usar operadores de pertenencia para checar si se encuentra en las posibles formas de si 
  \t6.4 Usar operadores de pertenencia para checar si se encuentra en las posibles formas de no""")
dic = {}
dic[True] = ["SI","si","Si","sI","sip","Sip","SIp","SIP","sIp","sIP","siP"]
dic[False] = ["No","no","NO","nO","nop","Nop","NOp","NOP","nOp","nOP", "noP"]
x = input("Escribe una palabra: ")
print("Se encuentra en True: ", x in dic[True])
print("Se encuentra en False: ", x in dic[False])