from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input(f'qual ano de nascimento sr(a) {pessoa["nome"]}'))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input(f'Cateira de trabalho sr(a) {pessoa["nome"]} ~[Caso nao tenha 0]'))
if pessoa['ctps'] !=0:
    pessoa['ano'] = int(input(f'qual ano de contratacao sr(a) {pessoa["nome"]}'))
    pessoa['salario'] = float(input(f'qual salario sr(a) {pessoa["nome"]}'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano'] + 35) - datetime.now().year)

for k,v in pessoa.items():
    print(k,v)