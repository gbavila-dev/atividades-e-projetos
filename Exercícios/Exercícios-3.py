# 1. Leia 5 números e mostre a lista completa

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# print(numeros)

# 2. Leia 5 números e mostre a soma

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# soma = sum(numeros)
# print(soma)

# 3. Leia 5 números e mostre: o maior valor

# numeros = []
# maior = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if n > maior:
#         maior = n

# print(maior)

# 4. Leia 6 números e conte quantos são pares

# numeros = []
# pares = 0

# for i in range(6):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for n in numeros:
#     if n % 2 == 0:
#         pares += 1

# print(pares)

# 5. Leia 5 números e mostre:
# Posição 0 → valor
# Posição 1 → valor

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     print(f"Posição {i+1}: {numeros[i]}")

# 6. Leia 6 números e conte quantos são negativos

# numeros = []
# negativos = 0

# for i in range(6):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if numeros[i] < 0:
#         negativos += 1

# print(negativos)

# 7. Leia 5 números e:

# troque valores negativos por 0

# numeros = []
# negativos = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if numeros[i] < 0:
#         numeros[i] = 0

# print(numeros)

# 8. Leia 5 números e crie uma nova lista com o dobro

# numeros = []
# dobro = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)
#     dobro.append(n*2)

# print(numeros)
# print(dobro)

# 9. Leia 6 números e:

# mostre apenas os maiores que 10

# numeros = []

# for i in range(6):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for n in numeros:
#     if numeros[i] > 10:
#         print(numeros[i])
#     else:
#         print("Não possui números maiores que 10")

# 10. Leia 6 números e:

# some valores das posições 0, 2, 4...

numeros = []
soma = 0
posicao = 0

for i in range(6):
    n = int(input("Insira um número: "))
    numeros.append(n)

    if i % 2 == 0:
        soma += numeros[i]

print(soma)