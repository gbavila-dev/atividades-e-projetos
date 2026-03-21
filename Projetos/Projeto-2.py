alunos = []

while True:
    print("=======================")
    print("   SISTEMA - ALUNOS    ")
    print("=======================\n")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Mostrar quantidade de alunos")
    print("4 - Buscar aluno pelo nome")
    print("5 - Remover aluno pelo nome")
    print("6 - Mostrar média das idades")
    print("7 - Mostrar a maior idade registrada")
    print("8 - Mostrar a menor idade registrada")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção (0 a 8):"))
    except:
        print("Digite apenas números!\n")
        continue

    if opcao == 1:
        nome = input("1 - Digite o nome do Aluno: ")
        while True: 
            try:
                idade = int(input("2 - Insira a idade do Aluno: "))
                if idade < 0:
                    print("Digite uma idade válida!\n")
                else:
                    break
            except:
                print("Digite um número válido!\n")
        alunos.append({"nome": nome, "idade": idade})

    elif opcao == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.\n")
        else:
            print("Alunos cadastrados:")
            for aluno in alunos:
                print(f"- {aluno['nome']}, {aluno['idade']} anos")

    elif opcao == 3:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.\n")
        else:
            print(f"Quantidade de alunos: {len(alunos)}")

    elif opcao == 4:
        busca = input("Digite o nome do aluno: ").strip().lower()
        encontrado = False
        for aluno in alunos:
            if aluno['nome'].lower() == busca:
                print(f"Aluno encontrado: {aluno['nome']}, {aluno['idade']} anos.")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.\n")

    elif opcao == 5:
        busca_r = input("Digite o nome do aluno:").strip().lower()
        encontrado = False
        for aluno in alunos:
            if aluno['nome'].lower() == busca_r:
                print(f"O Aluno: {aluno['nome']}, foi removido com sucesso!\n")
                alunos.remove(aluno)
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.\n") 

    elif opcao == 6:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.\n")
        else:
            soma = 0
        
            for aluno in alunos:
                soma += aluno['idade']

            media = soma / len(alunos)
            print("Média das idades: ", media)
    
    elif opcao == 7:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.\n")
        else:
            maior = alunos[0]['idade']

            for aluno in alunos:
                if aluno['idade'] > maior:
                    maior = aluno['idade']
        
            print(f"A maior idade registrada é: {maior}")

    elif opcao == 8:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.\n")
        else:
            menor = alunos[0]['idade']
            for aluno in alunos:
                if aluno['idade'] < menor:
                    menor = aluno['idade']
            
            print(f"A menor idade registrada é: {menor}\n")


    elif opcao == 0:
        print("Sistema encerrado com sucesso...\n")
        break

    else: 
        print("Insira uma opção válida!")
        tentar = input("Deseja tentar novamente? [S/N]\n").strip().lower()
        
        if tentar == "n":
            break
        elif tentar == "s":
            continue
        else: 
            print("Responda apenas com 'S' ou 'N'.")
            break