import random
#ejemplo 1

A = []
for x in range(10):
  A.append(random.randint(0,10))
print(A)

#ejemplo 2
A = []
random.seed(10)
for x in range(10):
  A.append(random.randint(0,10))
print(A)
random.seed(10)
for x in range(10):
  A.append(random.randint(0,10))
print(A)

#ejemplo 3
A = [random.randint(0,10) for x in range(10)]
print(A)
print(random.choice(A))

#ejemplo 4
A = [random.randint(0,10) for x in range(10)]
print(A)
print(random.sample(A,3))

#ejemplo 5
A = [random.randint(0,10) for x in range(10)]
print(A)
random.shuffle(A)
print(A)