# ==================================================
# REVISÃO DE PYTHON
# ==================================================

# ==================================================
# QUESTÃO 01 — PAR OU ÍMPAR
# ==================================================

par_impar = int(input("Insira um número: "))

if par_impar % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")


# ==================================================
# QUESTÃO 02 — MAIOR DE TRÊS NÚMEROS
# ==================================================

num_1 = int(input("Insira um número: "))
num_2 = int(input("Insira um número: "))
num_3 = int(input("Insira um número: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"O número {num_1} é maior!")
elif num_2 > num_1 and num_2 > num_3:
    print(f"O número {num_2} é maior!")
elif num_3 > num_1 and num_3 > num_2:
    print(f"O número {num_3} é maior!")


# ==================================================
# QUESTÃO 03 — MÉDIA E SITUAÇÃO DO ALUNO
# ==================================================

nota_1 = float(input("Insira uma nota: "))
nota_2 = float(input("Insira uma nota: "))
nota_3 = float(input("Insira uma nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média é: ", media)

if media >= 7:
    print("Aprovado")
elif media > 5:
    print("Recuperação")
elif media < 5:
    print("Reprovado")


# ==================================================
# QUESTÃO 04 — CONTAGEM REGRESSIVA
# ==================================================

contagem_reg = int(input("Insira um número: "))

print(contagem_reg)

while contagem_reg > 0:
    contagem_reg = contagem_reg - 1
    print(contagem_reg)


# ==================================================
# QUESTÃO 05 — SOMA E MÉDIA ATÉ DIGITAR 0
# ==================================================

soma = 0
quantidade = 0

while True:
    n = int(input("Digite um número: "))

    if n == 0:
        break

    quantidade += 1
    soma += n

media = soma / quantidade

print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media}")


# ==================================================
# QUESTÃO 06 — TABUADA
# ==================================================

n_tabuada = int(input("Insira um número: "))

for i in range(0, 10):
    print(f"{n_tabuada} x {i+1} = ", n_tabuada*(i+1))


# ==================================================
# QUESTÃO 07 — NÚMERO PRIMO
# ==================================================

n = int(input("Insira um número: "))

primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False

if primo == True:
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo!")


# ==================================================
# QUESTÃO 08 — FATORIAL
# ==================================================

n = int(input("Insira um número: "))

resultado = 1

for i in range(1, n + 1):
    resultado = resultado * i

print(resultado)


# ==================================================
# QUESTÃO 09 — SOMA, MÉDIA, MAIOR E MENOR
# ==================================================

n = int(input("Digite quantos números deseja inserir:"))

numeros = []

soma = 0

for i in range(n):
    inserir = int(input(f"Número {i+1}: "))
    numeros.append(inserir)

    soma += numeros[i]

    if i == 0:
        maior = inserir
        menor = inserir

    if inserir > maior:
        maior = inserir

    if menor > inserir:
        menor = inserir

media = soma / len(numeros)

print(soma)
print(media)
print(maior)
print(menor)


# ==================================================
# QUESTÃO 10 — CONTAR OCORRÊNCIAS
# ==================================================

numeros = [10, 5, 8, 10, 3, 10, 7, 5, 2]

n = int(input("Digite o número que deseja procurar: "))
contador = 0

for i in range(len(numeros)):
    if n == numeros[i]:
        contador += 1

print(f"O número {n} aparece {contador} vezes.")


# ==================================================
# QUESTÃO 11 — SEPARAR PARES E ÍMPARES
# ==================================================

numeros = [12, 7, 4, 9, 15, 20, 8, 3, 10]

pares = []
impares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

print("Pares: ", pares)
print("Ímpares: ", impares)


# ==================================================
# QUESTÃO 12 — MAIOR E SEGUNDO MAIOR
# ==================================================

numeros = [15, 8, 32, 4, 27, 19, 32, 10]
maior = numeros[0]
segundo_maior = numeros[0]

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]

    if numeros[i] < maior and numeros[i] > segundo_maior:
        segundo_maior = numeros[i]

print(maior)

print(segundo_maior)


# ==================================================
# QUESTÃO 13 — DISTRIBUIÇÃO DE NOTAS
# ==================================================

valor = int(input("Digite o valor de saque: "))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor= valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2

print(f"- 100: {notas100}")
print(f"- 50: {notas50}")
print(f"- 20: {notas20}")
print(f"- 10: {notas10}")
print(f"- 5: {notas5}")
print(f"- 2: {notas2}")


# ==================================================
# QUESTÃO 14 — SISTEMA DE LOGIN
# ==================================================

usuario_correto = "admin"
senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    usuario = str(input("Insira o nome de usuário: "))

    senha = str(input("Insira a senha do login: "))

    if usuario != usuario_correto or senha != senha_correta:
        tentativas -= 1

        print("Usuário ou senha incorretos!")

        print("Tentativas restantes: ", tentativas)

        if tentativas == 0:
            print("Usuário bloqueado!")

    else:
        print("Usuário logado com sucesso!")

        break


# ==================================================
# QUESTÃO 15 — PERCORRER MATRIZ
# ==================================================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end = " ")
    print()


# ==================================================
# QUESTÃO 16 — SOMA DA MATRIZ
# ==================================================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
print(soma)


# ==================================================
# QUESTÃO 17 — MAIOR ELEMENTO DA MATRIZ
# ==================================================

matriz = [
    [12, 5, 8],
    [23, 4, 17],
    [9, 31, 6]
]

maior = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
print(maior)


# ==================================================
# QUESTÃO 18 — DIAGONAL PRINCIPAL
# ==================================================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    print(matriz[i][i])


# ==================================================
# QUESTÃO 19 — CALCULADORA COM FUNÇÕES
# ==================================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def main():
    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
            print()

        except ValueError:
            print("Insira um valor válido!")
            continue

        match opcao:
            case 1:
                numero1 = int(input("Número 1: "))
                numero2 = int(input("Número 2: "))
                resultado = somar(numero1, numero2)

                print(resultado)
                print()

            case 2:
                numero1 = int(input("Número 1: "))
                numero2 = int(input("Número 2: "))
                resultado = subtrair(numero1, numero2)

                print(resultado)
                print()

            case 3:
                numero1 = int(input("Número 1: "))
                numero2 = int(input("Número 2: "))
                resultado = multiplicar(numero1, numero2)

                print(resultado)
                print()

            case 4:
                numero1 = int(input("Número 1: "))
                numero2 = int(input("Número 2: "))
                resultado = dividir(numero1, numero2)

                print(resultado)
                print()

            case 0:
                print("Encerrando sistema...")
                break

main()


# ==================================================
# QUESTÃO 20 — FUNÇÃO PARA VERIFICAR NÚMERO PRIMO
# ==================================================

def eh_primo(numero):

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

resultado = eh_primo(9)
print(resultado)


# ==================================================
# QUESTÃO 21 — FUNÇÃO PARA CALCULAR MÉDIA
# ==================================================

numeros = [10, 13, 15, 16, 23, 70]

def calcular_media(numeros):

    soma = 0
    media = 0

    for i in range(len(numeros)):
        soma += numeros[i]

    media = soma / len(numeros)

    return media

resultado = calcular_media(numeros)
print(resultado)


# ==================================================
# QUESTÃO 22 — FUNÇÃO PARA CONTAR OCORRÊNCIAS
# ==================================================

numeros = [10, 5, 8, 10, 3, 10, 7, 5, 2]

def contar_numero(numeros, n):

    contador = 0

    for i in range(len(numeros)):

        if n == numeros[i]:
            contador += 1

    return contador

resultado = contar_numero(numeros, 5)
print(resultado)


# ==================================================
# QUESTÃO 23 — FUNÇÃO PARA ENCONTRAR O MAIOR
# ==================================================

numeros = [10, 5, 8, 10, 3, 10, 90, 7, 5, 2]

def maior_numero(numeros):

    maior = numeros[0]

    for i in range(len(numeros)):

        if numeros[i] > maior:
            maior = numeros[i]

    return maior

resultado = maior_numero(numeros)
print(resultado)


# ==================================================
# QUESTÃO 24 — FUNÇÃO PARA ENCONTRAR O MENOR
# ==================================================

numeros = [10, 5, 8, 10, 3, 10, 90, 7, 5, 2]

def menor_numero(numeros):

    menor = numeros[0]

    for i in range(len(numeros)):

        if numeros[i] < menor:
            menor = numeros[i]

    return menor

resultado = menor_numero(numeros)
print(resultado)


# ==================================================
# QUESTÃO 25 — FUNÇÃO PARA FILTRAR NÚMEROS PARES
# ==================================================

numeros = [10, 5, 8, 10, 3, 10, 90, 7, 5, 2]

def criar_pares(numeros):

    pares = []

    for i in range(len(numeros)):

        if numeros[i] % 2 == 0:
            pares.append(numeros[i])

    return pares

resultado = criar_pares(numeros)
print(resultado)