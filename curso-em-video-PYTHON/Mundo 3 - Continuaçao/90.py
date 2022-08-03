aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7 :
    aluno['situacao'] = 'Aprovado'
elif 5<= aluno['media'] <7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')