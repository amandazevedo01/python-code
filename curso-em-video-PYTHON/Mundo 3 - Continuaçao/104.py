def leiaINT(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
        if ok:
            break





n = leiaINT (f'Digite um numeri: ')
print(f'voce acabou de digitar o numero {n}')