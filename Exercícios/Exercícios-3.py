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

# for i in numeros:
#     if numeros[i] > 10:
#         print(numeros[i])


# 10. Leia 6 números e:

# some valores das posições 0, 2, 4...

# numeros = []
# soma = 0

# for i in range(6):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if i % 2 == 0:
#         soma += numeros[i]

# print(soma)

# 11. 👉 Leia 6 números e:

# some os valores das posições:

# nums = []
# impares = 0

# for i in range(6):
#     n = int(input("Insira um número: "))
#     nums.append(n)

#     if i % 2 != 0:
#         impares += i

# print(impares)

# 12. Leia 6 números:

# calcule a média
# mostre apenas os números maiores que a média

# num = []
# soma = 0
# media = 0

# for i in range(6):
#     n = int(input("Insira um número: "))
#     num.append(n)

#     soma = sum(num)
#     media = soma / len(num)

# print(f"Soma: {soma}")
# print(f"Média: {media}")

# for n in num:
#     if n > media:
#         print(f"Números acima da média: {n}")

# 12. Leia 6 números:

# diga quais números aparecem mais de uma vez

# num = []
# repetidos = []

# for i in range(6):
#     n = int(input("Insira um número: "))
#     num.append(n)

# for i in range(len(num)):
#     contador = 0
#     for j in range(len(num)):
#         if num[i] == num[j]:
#             contador += 1

#     if contador > 1:
#         if num[i] not in repetidos:
#             repetidos.append(num[i])

# print(f"Números repetidos: {repetidos}")
# print(f"Lista: {num}")

# 13. Leia 4 números e mostre:
# num[i] com num[j]

# num = []

# for i in range(4):
#     n = int(input("Insira um número: "))
#     num.append(n)

# for i in range(len(num)):
#     for j in range(len(num)):
#         print(f"{num[i]} com {num[j]}")

# 14. Leia 5 números e mostre:

# Número 2 aparece 2 vezes
# Número 3 aparece 1 vez

# num = []
# repetidos = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     num.append(n)

# for i in range(len(num)):
#     contador = 0
#     for j in range(len(num)):
#         if num[i] == num[j]:
#             contador += 1

#     if num[i] not in repetidos:
#         repetidos.append(num[i])

#         print(f"Número {num[i]} aparece {contador} vezes")

#15. Modifique seu código para mostrar apenas:

# números que aparecem mais de 1 vez

# num = []
# repetidos = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     num.append(n)

# for i in range(len(num)):
#     contador = 0
#     for j in range(len(num)):
#         if num[i] == num[j]:
#             contador += 1

        
#     if contador > 1:
#         if num[i] not in repetidos:
#             repetidos.append(num[i])
#             print(f"O número {num[i]} aparece mais de uma vez.")
    
# 16. Mostrar apenas números que aparecem 1 vez

# num = []
# repetidos = []
# unicos = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     num.append(n)

# for i in range(len(num)):
#     contador = 0
#     for j in range(len(num)):
#         if num[i] == num[j]:
#             contador += 1

        
#     if contador > 1:
#         if num[i] not in repetidos:
#             repetidos.append(num[i])
#             print(f"O número {num[i]} aparece mais de uma vez.")
#     elif contador == 1:
#         if num[i] not in unicos:
#             unicos.append(num[i])
#             print(f"O número {num[i]} aparece apenas uma vez.")

# 17. qual número mais se repete

num = []
repetidos = []
unicos = []
maior = 0
mais_repete = None

for i in range(5):
    n = int(input("Insira um número: "))
    num.append(n)

for i in range(len(num)):
    contador = 0
    for j in range(len(num)):
        if num[i] == num[j]:
            contador += 1

        
    if contador > 1:
        if maior < contador:
            maior = contador
            mais_repete = num[i]

        if num[i] not in repetidos:
            repetidos.append(num[i])
            print(f"O número {num[i]} aparece mais de uma vez.")
    
    elif contador == 1:
        if num[i] not in unicos:
            unicos.append(num[i])
            print(f"O número {num[i]} aparece apenas uma vez.")

if mais_repete is not None:
    print(f"O número {mais_repete} apareceu mais vezes ({maior}).")
else:
    print("Nenhum número se repete.")

    
