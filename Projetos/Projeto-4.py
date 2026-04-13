def menu():
    print("\n===================")
    print("SISTEMA - CINEMA")
    print("===================\n")
    print("1 - Mostrar cadeiras")
    print("2 - Reservar cadeiras")
    print("3 - Cancelar reserva")
    print("4 - Mostrar livres")
    print("0 - Sair")   

def mostrar_cadeiras(cadeiras):
    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            print(f"Cadeira {i+1}: Livre")
        elif cadeiras[i] == 1:
            print(f"Cadeira {i+1}: Ocupada")

def reservar_cadeira(cadeiras):
    try:
        cadeira = int(input("Insira o número da cadeira (1 a 8): "))
        posicao = cadeira - 1

        if posicao >= 0 and posicao < len(cadeiras):
            if cadeiras[posicao] == 0:
                cadeiras[posicao] = 1
                print("Cadeira reservada com sucesso!")
            else:
                print("Essa cadeira já está reservada, selecione outra.")
        else:
            print("Número da cadeira inválido!")
    except ValueError:
        print("Insira apenas números!")

def cancelar_reserva(cadeiras):
    try:
        cadeira = int(input("Insira o número da cadeira (1 a 8): "))
        posicao = cadeira - 1

        if posicao >= 0 and posicao < len(cadeiras):
            if cadeiras[posicao] == 1:
                cadeiras[posicao] = 0
                print("Reserva cancelada com sucesso!")
            else:
                print("Essa cadeira não está ocupada.")
        else:
            print("Número da cadeira inválido!")
    except ValueError:
        print("Insira apenas números!")
    
def mostrar_livres(cadeiras):
    contador = 0
    
    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            contador += 1

    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            print(f"Cadeira {i+1}: Livre")        
    print()
    print(f"{contador} cadeiras estão livres!")


cadeiras = [0, 0, 0, 0, 0, 0, 0, 0]
def main():
    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            print()
        except ValueError:
            print("Insira apenas números!")
            continue

        match opcao:
            case 1:
                mostrar_cadeiras(cadeiras)
            case 2:
                reservar_cadeira(cadeiras)
            case 3:
                cancelar_reserva(cadeiras)
            case 4: 
                mostrar_livres(cadeiras)
            case 0:
                print("Desligando o sistema...")
                break
            case _:
                print("Opção inválida!")
main()