# 🔹 1. Mostrar matriz

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j])

# 2. 👉 Mostre assim:

# 1 2 3
# 4 5 6

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()

# 3. Crie uma matriz 3x3 pedindo valores:

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# 4. Depois de criar a matriz do exercício 3, mostre no formato:

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()

# 5. 👉 Some todos os valores da matriz
# ❌ sem usar sum()

# matriz = []
# soma = 0

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()

# for i in range (len(matriz)):
#     for j in range(len(matriz[i])):
#         soma += matriz[i][j]

# print(soma)

#6. Encontre o maior valor da matriz

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()
# print()

# maior = matriz[0][0]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#          if matriz[i][j] > maior:
#             maior = matriz[i][j]
# print(maior)

#7. Conte quantos números pares existem na matriz

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()
# print()

# pares = 0

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] % 2 == 0:
#             pares += 1
# print(pares)

#8. Mostre todos os valores da matriz que são maiores que 10

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()
# print()

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] > 10:
#             print(matriz[i][j])

#9 Peça um número ao usuário e conte quantas vezes ele aparece na matriz

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         valor = int(input(f"Insira o Valor [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print()
# print()

# contador = 0
# numero = int(input("Informe um número: "))

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if numero == matriz[i][j]:
#             contador += 1

# print(f"O número {numero} aparece {contador} vezes na matriz")
