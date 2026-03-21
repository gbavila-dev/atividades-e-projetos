# 1. Peça 5 números ao usuário e mostre qual é o maior número digitado.

# maior = int(input("Digite um número: "))

# for i in range(4):
#     num = int(input("Digite um número: "))
#     if num > maior:
#         maior = num

# print("O maior número digitado é:", maior)

# 2. Peça 5 números e mostre o menor número.

# menor = int(input("Digite um número: "))

# for i in range(4):
#     num1 = int(input("Digite um número: "))
#     if num1 < menor:
#         menor = num1
# print("O menor número digitado é:", menor) 

# 3. Peça vários números ao usuário até ele digitar 0.
# Depois, mostre a média dos números digitados (sem contar o 0).
# soma = 0
# contador = 0

# while True:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         break 

#     soma += num
#     contador += 1

#     if contador == 0:
#         print("Nenhum número foi digitado.")
#     else: 
#         media = soma / contador
# print("Média:", media)

#4. Peça 10 números e informe quantos são pares.

# par = 0

# for i in range(10):
#     num = int(input("Digite um número: "))

#     if num % 2 == 0:
#         par += 1
# print("Qtd de pares: ",par)

#5. Crie um sistema com:

# usuário correto: admin

# senha correta: 1234

# Continue pedindo até acertar.

# usuario_c = "admin"
# senha_c = "1234"

# while True:
#     usuario = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha de usuário: ")

#     if usuario == usuario_c and senha == senha_c:
#         print("Parabéns! Login efetuado com sucesso.")
#         break
#     else: 
#         r = input("Informações de login incorretas. Deseja tentar novamente? [S/N]:").strip().lower()
#         if r == "n":
#             break

# 6. usuario_c = "admin"
# Crie um programa que:

# permita adicionar números a uma lista

# depois mostre:

# todos os números

# maior número

# menor número

# lista = []

# for i in range(3):
#     n = float(input("Digite um número: "))
#     lista.append(n)
# print(f"Números da lista:",lista)
# print(f"Maior número: {max(lista)}")
# print(f"Menor número: {min(lista)}")

#7. Peça vários números e depois peça um número para buscar.
# Informe se ele está na lista ou não.

# lista = []

# for i in range(5):
#     num = int(input("Digite um número:"))
#     lista.append(num)
# busca = int(input("Insira um número que deseja buscar:"))

# if busca in lista:
#     print("Número encontrado!")
# else: 
#     print("Esse número não existe na lista.")

#8. Peça números ao usuário, mas não permita números duplicados na lista.

# numeros = []

# for i in range(3):
#     num = int(input("Insira um número: "))

#     if num in numeros:
#         print("Número duplicado não é permitido!")
#     else:
#         numeros.append(num)

# print("Lista final:", numeros)

#9. Crie um menu que permita:

# adicionar número

# remover número

# listar números

# numeros = []

# while True:
#     print("------------------")
#     print("NUMEROS")
#     print("------------------")
#     print("1 - Adicionar número")
#     print("2 - Remover número")
#     print("3 - Listar números")
#     print("0 - Sair")

#     opcao = int(input("Escolha uma opção (0 a 3): "))

#     if opcao == 1:
#         n = int(input("Digite um número: "))
#         numeros.append(n)

#         print(f"Número {n} adicioando com sucesso!")

#     elif opcao == 2:
#         i = int(input("Digite um número a ser removido: "))
    
        # if i in numeros:
        #     numeros.remove(i)
        #     print(f"Número {i} removido com sucesso!")
        # else:
        #     print("Número não encontrado na lista.")

#     elif opcao == 3:

#         if len(numeros) == 0:
#             print("Nenhum número cadastrado.")
#         else:
#             print("Números:")
#             for n in numeros:
#                 print(f"- {n}")

#     elif opcao == 0:
#         print("Saindo sistema...")
#         break

#     else:
#        print("Insira uma opção válida!")

#10. NA PAGINA DO PROJETO 2!!!!