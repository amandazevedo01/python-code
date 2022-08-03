#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
     cont = mai = 0
     print('\nAnalisando os falores passados... ')
     for valor in num:
         print(f' {valor} , ', end='', flush=True)
         sleep(0.3)
         if valor > mai:
             mai = valor
     print()
     print(f'o maior é {mai}')

maior(3,2,5)
maior(3,2,5,7)