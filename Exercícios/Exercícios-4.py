# 1. Mostrar elementos

# # 👉 Leia 5 números e mostre todos:

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# print(numeros)

# 2. Mostrar ao contrário

# 👉 Leia 5 números e mostre:

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# print(numeros[::-1])

# 3. Somar elementos

# 👉 Leia 5 números e mostre:

# numeros = []
# soma_total = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     soma_total += n

# print(soma_total)

# 4. Contar pares

# 👉 Mostre quantos números pares existem

# numeros = []
# pares = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if numeros[i] % 2 == 0:
#         pares += 1

# print(f"Existem {pares} números pares na lista!")

# 5. Maior número

# 👉 Mostre o maior número da lista

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# maior = numeros[i]
# for i in range(len(numeros)):
#     if numeros[i] > maior:
#         maior = numeros[i]

# print("O maior número é:", maior)

# 6. Menor número

# 👉 Mostre o menor número

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# menor = numeros[i] 
# for i in range(len(numeros)):
#     if numeros[i] < menor:
#         menor = numeros[i]

# print("O menor número é:", menor)

#7. Quantos maiores que 10

# 👉 Conte quantos números são > 10

# numeros = []
# maiores_que_10 = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

#     if numeros[i] > 10:
#         maiores_que_10 += 1

# print(f"Exatamente {maiores_que_10} são maiores que 10!")

# 8. Separar pares e ímpares

# 👉 Crie duas listas:

# pares
# ímpares

# numeros = []
# pares = []
# impares = [] 

# for i in range(5):
#     n = int(input("Insira um número:"))
#     numeros.append(n)

#     if numeros[i] % 2 == 0:
#         pares.append(numeros[i])
#     else:
#         impares.append(numeros[i])

# print(f"Pares: {pares}")
# print(f"Ímpares: {impares}")

# 9. Comparar todos com todos

# 👉 Mostre:

# num[i] com num[j]

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     for j in range(len(numeros)):
#         print(f"{numeros[i]} com {numeros[j]}")

# 10. Contar repetições

# 👉 Mostre:

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     contador = 0
#     for j in range(len(numeros)):
#         if numeros[i] == numeros[j]:
#             contador += 1
            
# if contador > 1:
#      print(f"Número {numeros[i]} aparece {contador} vezes")
# else:
#     print("Nenhum número se repete")

# 11. Mostrar repetidos

# 👉 Mostre apenas números repetidos

# numeros = []
# repetidos = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     contador = 0
#     for j in range(len(numeros)):
#         if numeros[i] == numeros[j]:
#             contador += 1

#     if contador > 1:
#          if numeros[i] not in repetidos:
#              repetidos.append(numeros[i])

# print(f"Repetidos: {repetidos}")
            
# 🔹 12. Mostrar únicos

# 👉 Mostre apenas números que aparecem uma vez

# numeros = []
# uma_vez = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     contador = 0
#     for j in range(len(numeros)):
#         if numeros[i] == numeros[j]:
#             contador += 1

#     if contador == 1:
#         if numeros[i] not in uma_vez:
#             uma_vez.append(numeros[i])

# print(f"Aparece apenas uma vez: {uma_vez}")

# 🔹 13. Encontrar o mais repetido

# 👉 Ex:

# [2, 3, 2, 4, 2]

# → 2 aparece mais vezes

# numeros = []
# repetidos = []
# mais_repete = None
# maior = 0

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     contador = 0
#     for j in range(len(numeros)):
#         if numeros[i] == numeros[j]:
#             contador += 1

#     if contador > 1:
#         if maior < contador:
#             maior = contador
#             mais_repete = numeros[i]
#             if numeros[i] not in repetidos:
#                 repetidos.append(numeros[i])


# print(f"Repetidos: {repetidos}")
# print(f"Mais repete: {mais_repete}")

# 🔹 14. Simular cadeiras (mini cinema)

# 👉 Lista com 0 e 1:

# 0 = livre
# 1 = ocupado

# 👉 Mostre:

# quantas livres
# quantas ocupadas

# cadeiras = [0, 1, 0, 0, 1]
# livres = 0
# ocupadas = 0

# for i in range(len(cadeiras)):
#     if cadeiras[i] == 0:
#         livres += 1
#     else:
#         ocupadas += 1

# print(f"Livres: {livres} | Ocupadas: {ocupadas}")

# 15. Trocar valores

# 👉 Dada uma lista:

# [1, 2, 3, 4]

# 👉 vire:

# [4, 3, 2, 1]

# lista = [1, 2, 3, 4]

# for i in range(len(lista)):
#     for j in range(len(lista)):
#         if lista[i] > lista[j]: 
#             temp = lista[i]
#             lista[i] = lista[j]
#             lista[j] = temp

# print(lista)

# 🔹 16. Sistema simples

# 👉 Faça um menu:

# 1 - Adicionar número
# 2 - Mostrar lista
# 3 - Mostrar maior
# 4 - Mostrar repetidos
# 0 - Sair

# 💥 Isso mistura TUDO

def menu():
    print("MENU")
    print("----------\n")
    print("1 - Add número")
    print("2 - Mostrar lista")
    print("3 - Mostrar maior")
    print("4 - Mostrar repetidos")
    print("0 - Sair")

def add_numero(num):
    n = int(input("- Insira um número na lista:"))
    num.append(n)

    print(f"Número {n} adicionado com sucesso!")

def mostrar_lista(num):
    print(f"- Lista completa: {num}")

def mostrar_maior(num):
    maior = 0
    i = 0
    for i in range(len(num)):
        if num[i] > maior:
            maior = num[i]

    print(f"O maior número da lista é: {maior}")

def mostrar_repetidos(num):
    repetidos = [] 
    i = 0

    for i in range(len(num)):
        contador = 0
        for j in range(len(num)):
            if num[i] == num[j]:
                contador += 1
        
        if contador > 1:
            if num[i] not in repetidos:
                repetidos.append(num[i])

    print(f"Números que se repetem: {repetidos}")

num = []

def main():
    while True:
        menu()
        try:
            opcao = int(input("- Insira uma opção:"))
        except ValueError:
            print("Insira apenas números!")

        match opcao:
            case 1:
                add_numero(num)
            case 2:
                mostrar_lista(num)
            case 3:
                mostrar_maior(num)
            case 4:
                mostrar_repetidos(num)
            case 0:
                print("Encerrando o sistema...")
                break
            case _:
                print("Insira uma opçãoi válida!")
                break
main()
