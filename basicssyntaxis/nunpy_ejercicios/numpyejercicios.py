import numpy as np

# import pandas as pd


# a= np.array([1, 2, 3])

# print(type(a))
# print(a.shape)
# print(a[2])


# a[0]=100
# a[1]+=1000
# a[2]-=1000
# print(a)
# print(a.shape)


b=np.array([[1,2,3],[1,2,3]])
print(type)
print(b)

b[1,2]+=100
print(b)

# a=np.zeros((4,5))
# print(a)
# print(a.shape)

b=np.ones((3,4))
print(b)

c=np.eye(4)
print(c)

d=np.full((5,5),8)
print(d)

print("Aleatorios")
e=np.random.random((3,3))
print(e)

# f=np.random.choice([1,10],size=(3,4),p=[0.3,0.7])
# print(f)

print("================================")
g=np.random.randint(11,100,(3,4))
print(g)

print("=================================")
submatricg=g[0:2, 0:2]
print(submatricg)

print("=================================")
h=np.random.randint(11,20,(5,4))
print(h)

print("=================================")
submatriz=h[-2:, -2:]
print(submatriz)

print("=================================")
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)

filter=(a>2)
print(filter)
print(a[filter])

print("=================================")
print("MARTIZ 7X7")
a = np.array([
    [ 5, 12, 35, 42, 59, 63, 77],
    [10, 22, 40, 55, 61, 72, 80],
    [18, 33, 46, 58, 60, 70, 85],
    [20, 37, 45, 50, 62, 74, 90],
    [25, 41, 47, 53, 66, 78, 92],
    [30, 44, 54, 57, 69, 82, 95],
    [36, 48, 52, 59, 71, 88,100]
])
print("Matriz original:")
print(a)
print("Forma de la matriz:", a.shape)

# Filtro: valores entre 40 y 60
filtro = (a >= 40) & (a <= 60)

print("\nMatriz de filtro (True si está entre 40 y 60):")
print(filtro)

# Extraer valores que cumplen la condición
valores_filtrados = a[filtro]

print("\nValores entre 40 y 60:")
print(valores_filtrados)


#Matrices

x=np.array([[1,2],[3,4]])
y=np.array([[10,20],[30,40]])
print(x)
print(y)
print(x.shape)
print(y.shape)

print(x+y)
print(np.add(x,y))
print(x*y)
print(np.dot(x,y))

#generar matriz radom
print("***********************************")
g=np.random.randint(11,100,(3,4))
print(g)

#Sumar matrices
print("***********************************")
print(np.sum(g,axis=0))
print(np.sum(g,axis=1))

#Suma total de matriz
print(" ============== valor total =================")
print(np.sum(g))


#
print(np.array([[1,2],[3,4]]))
print(x)
print(x.T)


#Concatenar matrices vertical y horizontal
print("===== Concatenar matrices vertical y horizontal =====")
print("Vertical")
newmatrix=np.vstack((x,y))
print(newmatrix)
print(newmatrix.shape)
print("Horizontal")
newmatrix=np.hstack((x,y))
print(newmatrix)
print(newmatrix.shape)


print("Concatenar con concatenate")
c=np.concatenate((x,y),axis=1)
print(c)
print(c.shape)
