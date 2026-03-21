def mostrar_menu():
    print("\n=======================")
    print("   SISTEMA - ALUNOS    ")
    print("=======================\n")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Quantidade de alunos")
    print("4 - Buscar aluno")
    print("5 - Remover aluno")
    print("6 - Média das idades")
    print("7 - Maior idade")
    print("8 - Menor idade")
    print("0 - Sair")

def cadastrar_aluno(alunos):
    nome = ler_nome()
    idade = ler_idade()
    alunos.append({"nome": nome, "idade": idade})
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("Alunos cadastrados:")
        for aluno in alunos:
            print(f"- {aluno['nome']}, {aluno['idade']} anos")

def mostrar_quantidade(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print(f"Quantidade de alunos: {len(alunos)}")

def buscar_aluno(alunos):
    nome_busca = input("Digite o nome do aluno: ").strip().lower()
    encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca:
            print(f"Aluno encontrado: {aluno['nome']}, {aluno['idade']} anos.")
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")

def remover_aluno(alunos):
    busca_remover = input("Digite o nome do aluno:").strip().lower()
    encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower() == busca_remover:
            print(f"O Aluno {aluno['nome']} foi removido com sucesso!")
            alunos.remove(aluno)
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.") 

def mostrar_media(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        soma = 0
        for aluno in alunos:
            soma += aluno['idade']

        media = soma / len(alunos)
        print(f"Média das idades: {media:.2f}")

def maior_idade(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        maior = alunos[0]['idade']

        for aluno in alunos:
            if aluno['idade'] > maior:
                maior = aluno['idade']
        
        print(f"A maior idade registrada é: {maior}")

def menor_idade(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        menor = alunos[0]['idade']
        for aluno in alunos:
            if aluno['idade'] < menor:
                menor = aluno['idade']
            
        print(f"A menor idade registrada é: {menor}")

def ler_nome():
    while True:
        nome = input("1 - Digite o nome do Aluno: ").strip()
        if nome == "":
            print("Digite um nome válido!")
        else:
            return nome

def ler_idade():
    while True: 
        try:
            idade = int(input("2 - Insira a idade do Aluno: "))
            if idade < 0:
                print("Digite uma idade válida!")
            else:
                return idade
        except:
            print("Digite um número válido!")

def tentar_novamente():
    print("Insira uma opção válida!")
    
    while True:
        tentar = input("Deseja tentar novamente (S/N)? Informe: ").strip().lower()
        print()
        
        if tentar == "s":
            return True
        elif tentar == "n":
            return False
        else:
            print("Responda apenas com 'S' ou 'N'.")
            print("Sistema encerrado com sucesso...")

def main():
    alunos = []    
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção (0 a 8):"))
            print()
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            cadastrar_aluno(alunos)
        elif opcao == 2:
            listar_alunos(alunos)
        elif opcao == 3:
            mostrar_quantidade(alunos)
        elif opcao == 4:
            buscar_aluno(alunos)
        elif opcao == 5:
            remover_aluno(alunos)
        elif opcao == 6:
            mostrar_media(alunos)
        elif opcao == 7:
            maior_idade(alunos)
        elif opcao == 8:
            menor_idade(alunos)
        elif opcao == 0:
            print("Sistema encerrado com sucesso...")
            break
        else: 
            if not tentar_novamente():
                break
main()