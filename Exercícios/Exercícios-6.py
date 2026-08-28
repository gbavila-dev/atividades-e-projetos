#1

# par_impar = int(input("Insira um número: "))

# if par_impar % 2 == 0:
#     print("O número é par!")
# else:
#     print("O número é ímpar!")

# 2

# num_1 = int(input("Insira um número: "))
# num_2 = int(input("Insira um número: "))
# num_3 = int(input("Insira um número: "))

# if num_1 > num_2 and num_1 > num_3:
#     print(f"O número {num_1} é maior!")
# elif num_2 > num_1 and num_2 > num_3:
#     print(f"O número {num_2} é maior!")
# elif num_3 > num_1 and num_3 > num_2:
#     print(f"O número {num_3} é maior!")

#3 

# nota_1 = float(input("Insira uma nota: "))
# nota_2 = float(input("Insira uma nota: "))
# nota_3 = float(input("Insira uma nota: "))

# media = (nota_1 + nota_2 + nota_3) / 3
# print(f"A média é: ", media)

# if media >= 7:
#     print("Aprovado")
# elif media > 5:
#     print("Recuperação")
# elif media < 5:
#     print("Reprovado")

#4

# contagem_reg = int(input("Insira um número: "))
# print(contagem_reg)

# while contagem_reg > 0:
#     contagem_reg = contagem_reg - 1
#     print(contagem_reg)

# 5
# soma = 0
# quantidade = 0

# while True:
#     n = int(input("Digite um número: "))
#     if n == 0:
#         break

#     quantidade += 1
#     soma += n

# media = soma / quantidade

# print(f"Quantidade: {quantidade}")
# print(f"Soma: {soma}")
# print(f"Média: {media}")

# 6

# n_tabuada = int(input("Insira um número: "))

# for i in range(0, 10):
#     print(f"{n_tabuada} x {i+1} = ", n_tabuada*(i+1))

# 7 

# n = int(input("Insira um número: "))
# primo = True

# for i in range(2, n):
#     if n % i == 0:
#         primo = False

# if primo == True:
#     print(f"{n} é primo!")
# else:
#     print(f"{n} não é primo!")

# 8 

# n = int(input("Insira um número: "))
# resultado = 1

# for i in range(1, n + 1):
#     resultado = resultado * i

# print(resultado)

#9

# n = int(input("Digite quantos números deseja inserir:"))
# numeros = []
# soma = 0

# for i in range(n):
#     inserir = int(input(f"Número {i+1}: "))
#     numeros.append(inserir)

#     soma += numeros[i]

#     if i == 0:
#         maior = inserir
#         menor = inserir

#     if inserir > maior:
#         maior = inserir

#     if menor > inserir:
#         menor = inserir

# media = soma / len(numeros)
# print(soma)
# print(media)
# print(maior)
# print(menor)

#10 

numeros = [10, 5, 8, 10, 3, 10, 7, 5, 2]

n = int(input("Digite o número que deseja procurar: "))
contador = 0

for i in range(len(numeros)):
    if n == numeros[i]:
        contador += 1

print(f"O número {n} aparece {contador} vezes.")
