import moeda
p = float(input('Digite preço R$: '))
print(f'A metade do {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
