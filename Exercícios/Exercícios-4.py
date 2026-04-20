# 1. Mostrar elementos

# # 👉 Leia 5 números e mostre todos:

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# print(numeros)

# 2. Mostrar ao contrário

# numeros = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros) - 1, -1, -1):
#     print(numeros[i])

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

# maior = numeros[0]
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

# menor = numeros[0] 
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
# mostrados = []

# for i in range(5):
#     n = int(input("Insira um número: "))
#     numeros.append(n)

# for i in range(len(numeros)):
#     contador = 0
#     for j in range(len(numeros)):
#         if numeros[i] == numeros[j]:
#             contador += 1
            
#     if contador > 1 and numeros[i] not in mostrados:
#         print(f"Número {numeros[i]} aparece {contador} vezes")
#         mostrados.append(numeros[i])

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

#         if numeros[i] not in repetidos:
#             repetidos.append(numeros[i])

# if mais_repete == None:
#     print("Nenhum número aparece mais vezes")
# else:
#     print(f"O número {mais_repete} aparece mais vezes")

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

# for i in range(len(lista) // 2):
#     temp = lista[i]
#     lista[i] = lista[len(lista) - 1 - i]
#     lista[len(lista) - 1 - i] = temp

# print(lista)

# 🔹 16. Sistema simples

# 👉 Faça um menu:

# 1 - Adicionar número
# 2 - Mostrar lista
# 3 - Mostrar maior
# 4 - Mostrar repetidos
# 0 - Sair

# 💥 Isso mistura TUDO

# def menu():
#     print()
#     print("MENU")
#     print("----------\n")
#     print("1 - Add número")
#     print("2 - Mostrar lista")
#     print("3 - Mostrar maior")
#     print("4 - Mostrar repetidos")
#     print("0 - Sair")

# def add_numero(num):
#     n = int(input("- Insira um número na lista:"))
#     num.append(n)

#     print(f"Número {n} adicionado com sucesso!")

# def mostrar_lista(num):
#     print(f"- Lista completa: {num}")

# def mostrar_maior(num):
#     if len(num) == 0:
#         print("Lista vazia!")
#         return
#     else:
#         maior = num[0]

#         for i in range(len(num)):
#             if num[i] > maior:
#                 maior = num[i]

#         print(f"O maior número da lista é: {maior}")

# def mostrar_repetidos(num):
#     repetidos = [] 
#     i = 0

#     for i in range(len(num)):
#         contador = 0
#         for j in range(len(num)):
#             if num[i] == num[j]:
#                 contador += 1
        
#         if contador > 1:
#             if num[i] not in repetidos:
#                 repetidos.append(num[i])

#     print(f"Números que se repetem: {repetidos}")

# num = []

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("- Insira uma opção:"))
#             print()

#         except ValueError:
#             print("Insira apenas números!")
#             continue

#         match opcao:
#             case 1:
#                 add_numero(num)
#             case 2:
#                 mostrar_lista(num)
#             case 3:
#                 mostrar_maior(num)
#             case 4:
#                 mostrar_repetidos(num)
#             case 0:
#                 print("Encerrando o sistema...")
#                 break
#             case _:
#                 print("Insira uma opção válida!")
# main()

# Desafio
# num = []

# def menu():
#     print()
#     print("==================")
#     print("SISTEMA - NÚMEROS")
#     print("==================")
#     print("1 - Adicionar número")
#     print("2 - Mostrar lista")
#     print("3 - Mostrar maior e menor")
#     print("4 - Mostrar repetidos")
#     print("5 - Mostrar únicos")
#     print("6 - Mostrar média")
#     print("7 - Mostrar lista invertida")
#     print("0 - Sair")

# def adicionar_numero(num):
#     n = int(input("- Insira um número: "))
#     num.append(n)

# def mostrar_lista(num):
#     print(f"Lista: {num}")

# def maior_e_menor(num):
#     if len(num) == 0:
#         print("Lista vazia!")
#         return
    
#     maior = num[0]
#     menor = num[0]

#     for i in range(len(num)):
#         if num[i] > maior:
#                 maior = num[i]

#         if num[i] < menor:
#             menor = num[i]

#     print(f"Maior número da lista: {maior}")
#     print(f"Menor número da lista: {menor}")

# def mostrar_repetidos(num):
#     repetidos = []

#     for i in range(len(num)):
#         contador = 0
#         for j in range(len(num)):
#             if num[i] == num[j]:
#                 contador += 1
        
#         if contador > 1:
#             if num[i] not in repetidos:
#                 repetidos.append(num[i])

#     print(f"Números repetidos: {repetidos}")

# def mostrar_unicos(num):
#     unicos = []

#     for i in range(len(num)):
#         contador = 0
#         for j in range(len(num)):
#             if num[i] == num[j]:
#                 contador += 1

#         if contador == 1:
#             if num[i] not in unicos:
#                 unicos.append(num[i])

#     print(f"Números que não repetem: {unicos}")

# def mostrar_media(num):

#     if len(num) == 0:
#         print("A lista está vazia!")
#         return

#     soma = sum(num)
#     media = soma / len(num)

#     print(f"A média da lista é: {media:.2f}")

# def mostrar_lista_invertida(num):
#     if len(num) == 0:
#         print("Lista vazia!")
#         return

#     print("Lista invertida: ", end="")

#     for i in range(len(num) - 1, -1, -1):
#         print(num[i], end=" ")
        
#     print()

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("- Digite uma opção: "))   
#             print()         

#         except ValueError:
#             print("Insira apenas números!")
#             continue

#         match opcao:
#             case 1:
#                 adicionar_numero(num)
#             case 2:
#                 mostrar_lista(num)
#             case 3:
#                 maior_e_menor(num)
#             case 4:
#                 mostrar_repetidos(num)
#             case 5:
#                 mostrar_unicos(num)
#             case 6:
#                 mostrar_media(num)
#             case 7:
#                 mostrar_lista_invertida(num)
#             case 0:
#                 print()
#                 print("Você saiu do sistema, volte sempre!")
#                 break
#             case _:
#                 print("Insira um valor válido!")
# main()