import numpy as np
# Christian garcia jimenez 
# ejemplos de numpy numerical python 
print("-- Espaciado lineamente en array -- 0068")
arre = np.linspace(start=0, stop=1, num=5)
print(arre)
print("--  matrix identidad en 20 array -- 0068")
matrix = np.eye(3)
print(matrix)
print("--  generar numeros al azar(aleatorio) en  20 array -- 0068")
nomale = np.random.random((3, 4)) # genera 12 numeros alaeatorios
print(nomale)
print("genera 9 numeros alaeatorios entre 0 y 1")
nomale = np.random.random((3, 3)) # genera 12 numeros alaeatorios
print(nomale)
# como generar 9 números aleatorios aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3x3
print("generar 9 números aleatorios aleatorios comprendidos entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Christian garcia Jimenez nc=n 0068")