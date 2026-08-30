# ==================================================
# REVISÃO DE PYTHON
# ==================================================

# ==================================================
# QUESTÃO 26 — TUPLAS
# ==================================================

# filmes = ("Harry Potter e o Cálice de Fogo", "O Exorcista", "Obsessão", "O Iluminado", "Matrix")

# def menu():
#     print("1 - Mostrar filmes")
#     print("2 - Primeiro filme")
#     print("3 - Último filme")
#     print("4 - Quantidade de filmes")
#     print("0 - Sair")

# def mostrar_filmes(filmes):
#     for i in range (len(filmes)):
#         print(f"{i+1} - Filme: {filmes[i]}")

# def primeiro_filme(filmes):
#     print(f"Primeiro filme: {filmes[0]}")

# def ultimo_filme(filmes):
#     print(f"Último filme: {filmes[-1]}")

# def quantidade_filmes(filmes):
#     print(f"Quantidade: {len(filmes)}")
        

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Selecione uma opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue 

#         match opcao:
#             case 1:
#                 mostrar_filmes(filmes)
#             case 2:
#                 primeiro_filme(filmes)
#             case 3:
#                 ultimo_filme(filmes)
#             case 4:
#                 quantidade_filmes(filmes)
#             case 0:
#                 print("Saindo do sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 27 — SETS
# ==================================================

filmes = {"Harry Potter e a Pedra Filosofal", "A Múmia"}

def menu():
    print("1 - Adicionar filme")
    print("2 - Remover filme")
    print("3 - Mostrar filme")
    print("4 - Verificar filme")
    print("5 - Quantidade filmes")
    print("0 - Sair")

def add_filme(filmes):
    f = str(input("Insira o nome do filme: "))
    filmes.add(f)

    print(f"{f} adicionado com sucesso!")
    print()

def remover_filme(filmes):
    f = str(input("Insira o nome do filme: "))
    if f in filmes:
        filmes.remove(f)
    else:
        print("Este filme não existe!")

    print(f"{f} removido com sucesso!")
    print()

def mostrar_filmes(filmes):
    contador = 0
    for filme in filmes:
        contador += 1
        print(f"{contador} - Filme: {filme}")
    print()

def verificar_filme(filmes):
    f = str(input("Insira o nome do filme: "))
    if f in filmes:
        print("Este filme existe!")
    else:
        print("Este filme não existe!")
    print()

def quantidade_filmes(filmes):
    print(f"Quantidade: {len(filmes)}")
    print()

def main():
    while True:
        menu()
        try:
            opcao = int(input("Insira a opção:"))
            print()
        except ValueError:
            print("Insira um valor válido!")
            continue    

        match opcao:
            case 1:
                add_filme(filmes)
            case 2:
                remover_filme(filmes)
            case 3:
                mostrar_filmes(filmes)
            case 4:
                verificar_filme(filmes)
            case 5:
                quantidade_filmes(filmes)
            case 0: 
                print("Saindo do sistema...")
                break
main()