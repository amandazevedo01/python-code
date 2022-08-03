from ex115.lib.interface import *  # importanto tudo
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])
    if resposta ==1:
        #Opcao de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta ==2:
        #Cadastrar uma pessoa
        cabeçalho('Novo Cadastro')
        nome=str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq,nome,idade)
    elif resposta ==3:
        print('Saindo do Sistema. Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(1)
