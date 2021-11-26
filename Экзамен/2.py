import random
a= int(input("Введите значение="))
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
g= 1
for i in a:
    b.append(random.randint(15))
print(b[0], b[-1])
for i in b:
    g*=i
print (g)
