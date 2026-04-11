print("\n====================")
print("CADASTRAR GABARITO")
print("====================\n")

gabarito = []
alunos = []
nota_final = []

for i in range(5):
    respostas = input(f"Questão {i+1}: ")
    gabarito.append(respostas)

for j in range(3):
    nota_aluno = 0

    print("\n====================")
    print(f"ALUNO {j+1}")
    print("====================\n")

    nome = input("Nome do aluno: ")
    alunos.append(nome)

    for c in range(5):
        resposta = input(f"Questão {c+1}: ")
        
        if resposta == gabarito[c]:
            nota_aluno += 2
   
    nota_final.append(nota_aluno)

print("\n====================")
print("NOTAS FINAIS")
print("====================\n")

for h in range(3):
    print(f"{alunos[h].capitalize()}: {nota_final[h]}")

print("\n====================")
print("MÉDIA DA TURMA")
print("====================\n")

media = sum(nota_final) / len(alunos)
print(f"Média da turma: {media:.2f}")