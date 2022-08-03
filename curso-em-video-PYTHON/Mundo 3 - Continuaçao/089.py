ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('quer continuar?: '))
    if resp in 'Nn':
        break
print('---------')
print(ficha)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print("-"*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]>8}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')