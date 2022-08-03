from ex109 import moeda
p = float(input('Digite preço R$: '))
print(f'A metade do {p} é {moeda.metade(p,True)}')
print(f'O dobro de {p} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Diminuido 10%, temos {moeda.diminuir(p,10,True)}')

