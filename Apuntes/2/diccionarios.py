
#referencia lo que son items
#ejemplo 1
a = {}
print(a)
a = {1:"fresa",2:"manzana"}
print(a)
#constructor con iterables
a = dict()
print(a)
a = dict(1="fresa",2="manzana")
print(a)
a = dict(zip([1,2],["fresa","manzana"]))
print(a)
a = dict([(1,"fresa"),(2,"manzana")])
print(a)

#ejemplo 2
dic = {}
dic[1] = "fresa"
dic[2] = "manzana"
print(dic)

#ejemplo 3
dic = {1:"fresa",2:"manzana"}
print(dic.values())

#ejemplo 4
dic = {1:"fresa",2:"manzana"}
print(dic.values())

#ejemplo 5
dic = {1:"fresa",2:"manzana"}
print(dic.items())

#ejemplo 6
dic = {1:"fresa",2:"manzana"}
print(dic.pop(1))
print(dic)

#ejemplo 7
dic = {1:"fresa",2:"manzana"}
print(dic.popitem())
print(dic)

#ejemplo 8
dic = {1:"fresa",2:"manzana"}
print("Función len: ",len(dic))
print(1 in dic)
print("Función max: ",max(dic))
print("Función min: ",min(dic))
print("Función sorted: ",sorted(dic))

#ejemplo 9
llaves=[1,2,3,4,5]
dic = dict.fromkeys(llaves)
print(dic)
dic = dict.fromkeys(llaves,"a")
print(dic)
dic = dict.fromkeys(llaves,[])
print(dic)
dic[1].append(1)
print(dic)

#ejemplo 10
A = {1:1,2:4,3:9}
A.update({4:16,5:25})
print(A)
A.update([(6,36),(7,49)])
print(A)
A.update(((8,64),(9,81)))
print(A)

#ejemplo 11
A = ["fresas","manzanas","peras","platanos","uvas"]
B = [1,2,3,4,5]
print(A)
print(B)
print(dict(enumerate(A,10)))
print(dict(zip(A,B)))

#ejemplo 12
dic = {1:"fresa",2:"manzana"}
print(dic)
dic2 = dic.copy()
print(dic.clear())
print(dic2)
