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