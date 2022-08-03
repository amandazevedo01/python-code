def aumentar(preço=0,taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return moeda(res) if formato else res


def diminuir(preço = 0,taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return moeda(res) if formato else res


def dobro(preço = 0,formato=False):
    res = preço * 2
    return moeda(res) if formato else res


def metade(preço = 0,formato=False):
    res = preço/2
    return moeda(res) if formato else res

def moeda (preço = 0, moeda = 'R$'):
    '''
    :param preço: Insira um valor para ser calculado
    :param moeda: Qual Formato da moeda
    :return: Retorna o valor formatado
    '''
    return f'{moeda}{preço:>2.2f}'.replace('.',',')

def resumo (preço=0, taxaa=10, taxar=5):
    """

    :rtype: object
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: {moeda(preço)}')
    print('-'*30)
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço \t{metade(preço,True)}')
    print(f'{taxaa} o preço do Preço {aumentar(preço,taxaa,True)}')
    print(f'{taxar} do Preço \t\t{diminuir(preço,taxaa,True)}')
    print('-'*30)
