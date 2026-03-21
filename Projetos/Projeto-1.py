def mostrar_menu():
    print("-----------------")
    print("MENU")
    print("-----------------")
    print("1: Cadastrar número")
    print("2: Mostrar números cadastrados")
    print("3: Mostrar soma dos números")
    print("0: Sair")

def cadastrar_numero(numeros):
    n = float(input("Insira um número a ser cadastrado: "))
    numeros.append(n)

def numeros_cadastrados(numeros):
    if len(numeros) == 0:
        print("Nenhum número cadastrado.")
    else:
        print(f"Números cadastrados: ")
        for n in numeros:
            print(f"- {n}")

def mostrar_soma(numeros):
    if len(numeros) == 0:
        print("Nenhum número cadastrado.")
    else:
        total = sum(numeros)
        print(f"A soma total dos números é: {total}")

def main():
    numeros = []
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            cadastrar_numero(numeros)
        elif opcao == 2:
            numeros_cadastrados(numeros)
        elif opcao == 3:
            mostrar_soma(numeros)
        elif opcao == 0:
            print("Você saiu do sistema com êxito.")
            break
        else:
            print("Digite uma opção válida.")
main()