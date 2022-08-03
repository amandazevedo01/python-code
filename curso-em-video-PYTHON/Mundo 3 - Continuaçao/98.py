#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
def contador(inicio,passo,fim):
    global p
    if passo ==0:
        if inicio > fim:
            while inicio>fim:
                p=1
                print(inicio, end=' ')
                inicio = inicio - p
        elif inicio < fim:
            while inicio < fim:
                p = 1
                print(inicio, end=' ')
                inicio = inicio + p
    if inicio < fim:
        while inicio<fim:
            print(inicio, end=' ')
            inicio = inicio + passo
    elif inicio > fim:
        while inicio>fim:
            print(inicio, end=' ')
            inicio = inicio - passo

i = int(input('inicio'))
p = int(input('passo'))
f = int(input('fim'))
contador(i,p,f)
