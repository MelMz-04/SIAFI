#aritméticos
A = 5
B = 2
print("A=",A)
print("B=",B)
print("suma: ",A+B)
print("resta: ",A-B)
print("multiplicación: ",A*B)
print("división: ",A/B)
print("modulo: ",A%B)
print("exponente: ",A**B)
print("división entera: ",A//B)

#comparación
A = 10
B = 5
print("A=",A)
print("B=",B)
print("A==B: ",A==B)
print("A!=B: ",A!=B)
print("A>B: ",A>B)
print("A<B: ",A<B)
print("A>=B: ",A>=B)
print("A<=B: ",A<=B)

#lógicos
A = True
B = False
print("A=",A)
print("B=",B)
print("A and B: ",A and B)
print("A or B: ",A or B)
print("not A:", not A)

#pertenencia
'''sirven para saber si dos variables 
referencia a la misma estructura'''
A = [1,2,3,4,5]
B = A 
C = A.copy()
print("A=",A)
print("B=",B)
print("C=",C)
print("A is B: ",A is B)
print("A is C: ",A is C)
print("A is not C: ",A is not C)

#inclusión, si algo pertenece a una estructura
A = [1,2,3,4,5]
B = 1
print("A=",A)
print("B=",B)
print("B in A: ",B in A)
print("B not in A:", B not in A)

#reducciones para asignaciones
A = B = C = D = E = F = G = 10
print("A+=1: ",A+=1)
print("B-=1: ",B-=1)
print("C*=1: ",C*=1)
print("D/=1: ",D/=1)
print("E%=1: ",E%=1)
print("F**=1: ",F**=1)
print("G//=1: ",G//=1)