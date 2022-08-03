from datetime import date

data_atual = date.today()
print(data_atual)
#nome = str(input('qual seu nome: '))
idade = int(input('qual a sua idade ? '))
hoje = data_atual.year
print(hoje)
nasc = hoje - idade
if