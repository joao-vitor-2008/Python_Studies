import numpy as np

matrizWithNp = np.eye(3)

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
# print(matriz)
for k in range(len(matriz)):
    print(matriz[k])
print()
print(matrizWithNp)
