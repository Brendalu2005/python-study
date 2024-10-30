import os 
os.system ('cls')
estudantes = []
aluno = {}

limite = int(input("insira a quantidade de alunos: "))

for i in range(limite):
    aluno['nome'] = str(input("Insira o nome: "))
    aluno['média'] = float(input(f"Insira a média de {aluno['nome']} : "))

    if aluno['média'] >= 7:
        aluno['situação'] = 'aprovado'
    elif 5 <= aluno['média']<= 7:
        aluno['situação'] = 'recuperação'
    else:
        aluno['situação'] = 'reprovado'
    
    estudantes.append(aluno.copy())


#print(alunos)
#mostra apenas o ultimo adicionado
for a in estudantes:
    for k, v in a.items():
        print(f"{k} é {v}")
