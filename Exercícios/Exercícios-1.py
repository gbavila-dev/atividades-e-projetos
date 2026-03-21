#1. Peça um número ao usuário e informe se ele é par ou ímpar.

# n = int(input("Insira um número: "))

# if n % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

#2. Peça a idade de uma pessoa e informe se ela é:
# maior de idade
# menor de idade

# idade = int(input("Insira sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade.")

#3. Peça a nota de um aluno (0 a 10) e informe:
#aprovado (nota ≥ 7)
#recuperação (nota entre 5 e 6)
#reprovado (nota < 5)

# nota = int(input("Insira a nota do aluno (0 a 10): "))

# if nota >= 7:
#     print("Aluno aprovado.")
# elif nota >= 5:
#     print("Aluno em recuperação.")
# else:
#     print("Aluno reprovado.")

#4. Mostre os números de 1 até 10 usando repetição.

# i = 0

# while i < 10:
#     i += 1
#     print(i)

# for i in range(1, 11):
#     print(i)

#5. Peça 5 números ao usuário e mostre a soma total.

# i = 0
# soma = 0

# for i in range(5):
#     num = int(input(f"Insira um número: "))
#     soma += num
# print("A soma total é: ", soma)

# i = 0
# soma = 0

# while i < 5:
#     num = int(input(f"Insira um número: "))
#     i += 1
#     soma += num
# print("A soma total é: ", soma)

# 6. Peça uma senha ao usuário e continue pedindo até que ele digite a senha correta.

# n = 0
# senha = 1234

# while n != senha:
#     n = int(input("Digite a senha correta: "))

#     if n != senha:
#         print("Tente novamente.")
#     else:
#         print("Parabéns!")

#7. Peça um número e mostre a tabuada dele de 1 até 10.

# numero = int(input("Digite o número que deseja saber a tabuada: "))

# for i in range(1, 11):
#     mult = numero * i
#     print(f"{numero} x {i}: {mult}")

#8. Mostre uma contagem de 10 até 1 e depois exiba “Fim”.

# i = 10

# while i > 0:
#     print(i)
#     i -= 1
# print("Fim")

# for i in range(10, 0, -1):
#     print(i)
# print("Fim")  

#9. Peça um número ao usuário. Se for negativo, continue pedindo até que ele digite um número positivo.

# n = -1

# while n < 0:
#     n = int(input("Insira um número: "))

#10. Crie um menu com as opções:

# 1: Mostrar mensagem “Olá”

# 2: Mostrar “Você escolheu a opção 2”

# 0: Sair

# O programa deve continuar rodando até o usuário escolher sair.

# while True:
#     print("-----------------")
#     print("MENU")
#     print("-----------------")
#     print("1: Mostrar mensagem “Olá”")
#     print("2: Mostrar “Você escolheu a opção 2”")
#     print("0: Sair")

#     opcao = int(input("Escolha uma opção: "))

#     if opcao == 1:
#         print("Olá.")
#     elif opcao == 2:
#         print("Você escolheu a opção 2.")
#     elif opcao == 0:
#         print("Você saiu do sistema!")
#         break
#     else:
#         print("A opção tem que ser válida, tente novamente.")