def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaINT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[35mEntrada de Dados interrompida\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[35mEntrada de Dados interrompida\033[m')
            return 0
        else:
            return n



def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaINT('Sua Opção: ')
    return opc
