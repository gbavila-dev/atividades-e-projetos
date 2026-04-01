import math 

def menu():
    print("\n===========================")
    print("      MINI CALCULADORA       ")
    print("===========================\n")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Elevar")
    print("6 - Raíz Quadrada")
    print("7 - Bhaskara")
    print("0 - Sair")

def somar():
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        adicao = num1 + num2

        print(f"{num1} + {num2} = {adicao}")
    except ValueError:
        print("Apenas números são permitidos!")

def subtrair():
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        subtracao = num1 - num2

        print(f"{num1} - {num2} = {subtracao}")
    except ValueError:
        print("Apenas números são permitidos!")

def multiplicar():
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        multiplicacao = num1 * num2

        print(f"{num1} * {num2} = {multiplicacao}")
    except ValueError:
        print("Apenas números são permitidos!")


def dividir():
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        if num2 == 0:
            print("Não é possível dividir por zero.")
            return
        
        divisao = num1 / num2
        print(f"{num1} / {num2} = {divisao}")
    except ValueError:
        print("Apenas números são permitidos!")

def elevar():
    try:
        num1 = float(input("Insira o número a ser elevado: "))
        num2 = float(input("Insira o expoente: "))
        elevacao = math.pow(num1, num2)

        print(f"{num1} ^ {num2} = {elevacao}")
    except ValueError:
        print("Apenas números são permitidos!")

def raiz():
    try:
        num1 = float(input("Insira o número qude deseja tirar a raíz: "))
        raiz_q = math.sqrt(num1)

        print(f"√{num1} = {raiz_q}")
    except ValueError:
        print("Apenas números são permitidos!")

def bhaskara():
    try:
        a = float(input("Insira o valor de 'A':"))
        b = float(input("Insira o valor de 'B':"))
        c = float(input("Insira o valor de 'C':"))

        if a == 0:
            print("O valor de A não pode ser 0.")
            return

        delta = ((math.pow(b,2)) - (4*a*c))
        print(f"Delta = {delta}")

        if delta < 0:
            print("Delta negativo. Não existem raízes reais.")
            return

        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
    except ValueError:
        print("Apenas números são permitidos!")

def main():

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opcção (0 a 7): "))
            print()
        except ValueError:
            print("Apenas números são permitidos!")
            continue

        match opcao:
            case 1:
                somar()
            case 2:
                subtrair()
            case 3:
                multiplicar()
            case 4:
                dividir()
            case 5:
                elevar()
            case 6:
                raiz()
            case 7:
                bhaskara()
            case 0:
                print("Sistema encerrado, volte sempre!")
                break
            case _:
                print("Opção inválida!")
main()