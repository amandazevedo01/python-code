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



n = leiaINT(f'Digite um numero inteiro: ')
a = leiaFloat(f'Digite um numero float: ')
print(f'voce acabou de digitar o numero {n} e {a}')