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

# filmes = {"Harry Potter e a Pedra Filosofal", "A Múmia"}

# def menu():
#     print("1 - Adicionar filme")
#     print("2 - Remover filme")
#     print("3 - Mostrar filme")
#     print("4 - Verificar filme")
#     print("5 - Quantidade filmes")
#     print("0 - Sair")

# def add_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     filmes.add(f)

#     print(f"{f} adicionado com sucesso!")
#     print()

# def remover_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     if f in filmes:
#         filmes.remove(f)
#     else:
#         print("Este filme não existe!")

#     print(f"{f} removido com sucesso!")
#     print()

# def mostrar_filmes(filmes):
#     contador = 0
#     for filme in filmes:
#         contador += 1
#         print(f"{contador} - Filme: {filme}")
#     print()

# def verificar_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     if f in filmes:
#         print("Este filme existe!")
#     else:
#         print("Este filme não existe!")
#     print()

# def quantidade_filmes(filmes):
#     print(f"Quantidade: {len(filmes)}")
#     print()

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira a opção:"))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue    

#         match opcao:
#             case 1:
#                 add_filme(filmes)
#             case 2:
#                 remover_filme(filmes)
#             case 3:
#                 mostrar_filmes(filmes)
#             case 4:
#                 verificar_filme(filmes)
#             case 5:
#                 quantidade_filmes(filmes)
#             case 0: 
#                 print("Saindo do sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 28 — Dicionários
# ==================================================


# filme = {}

# def menu():
#     print("1 - Cadastrar filme")
#     print("2 - Mostrar informações")
#     print("3 - Alterar informações")
#     print("4 - Remover informações")
#     print("5 - Verificar informações")
#     print("0 - Sair")

# def cadastrar_filme(filme):
#     n = input("Digite o nome do filme: ")
#     a = input("Digite o ano de lançamento: ")
#     g = input("Digite o genero do filme: ")

#     filme['Nome'] = n
#     filme['Ano'] = a
#     filme['Gênero'] = g

# def mostrar_info(filme):
#     for chave, valor in filme.items():
#         print(f"- {chave}: {valor}")

# def alterar_info(filme):
#     while True:
#         novo_n = input("Deseja alterar o nome do filme? (S/N): ").upper()
#         if novo_n == "S":
#             novo_n = input("Digite o nome do filme: ")
#             filme['Nome'] = novo_n

#             print("Nome alterado com sucesso!")
#             print()

#         novo_a = input("Deseja alterar o ano do filme? (S/N): ").upper()
#         if novo_a == "S":
#             novo_a = input("Digite o ano de lançamento: ")
#             filme['Ano'] = novo_a

#             print("Ano de lançamento alterado com sucesso!")
#             print()

#         novo_g = input("Deseja alterar o gênero do filme? (S/N): ").upper()
#         if novo_g == "S":
#             novo_g = input("Digite o gênero do filme: ")
#             filme['Gênero'] = novo_g

#             print("Gênero alterado com sucesso!")
#             print()

#         continuar = input("Deseja continuar alterando? (S/N)").upper()
#         if continuar == "S":
#             continue
#         else:
#             break

# def remover_info(filme):
#     while True:
#             r_n = input("Deseja remover o nome do filme? (S/N): ").upper()
#             if r_n == "S":
#                 if 'Nome' in filme:
#                     del filme['Nome']
    
#                 print("Nome removido com sucesso!")
#                 print()
    
#             r_a = input("Deseja remover o ano do filme? (S/N): ").upper()
#             if r_a == "S":
#                 if 'Ano' in filme:
#                     del filme['Ano']
    
#                 print("Ano de lançamento removido com sucesso!")
#                 print()
    
#             r_g = input("Deseja remover o gênero do filme? (S/N): ").upper()
#             if r_g == "S":
#                 if 'Gênero' in filme:
#                     del filme['Gênero']
    
#                 print("Gênero removido com sucesso!")
#                 print()
    
#             continuar = input("Deseja remover algo a mais? (S/N)").upper()
#             if continuar == "S":
#                 continue
#             else:
#                 break

# def verificar_info(filme):
#     verificar = input("Digite a informação que deseja verificar:")
#     if verificar in filme:
#         print("Esta informação existe!")
#     else:
#         print("Esta informação não existe!")

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira a opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_filme(filme)
#             case 2:
#                 mostrar_info(filme)
#             case 3:
#                 alterar_info(filme)
#             case 4:
#                 remover_info(filme)
#             case 5:
#                 verificar_info(filme)
#             case 0:
#                 print("Encerrando o sistema...")
#                 break
# main()