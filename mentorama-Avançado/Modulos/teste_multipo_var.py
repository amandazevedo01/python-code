def multiplo5(var1):
    if var1 % 5 == 0:
        resultado = 'fizz'
        return resultado


def multiplo7(var1):
    if var1 % 7 == 0:
        resultado = 'buzz'
        return resultado


def multiplo5e7(var1):
    if var1 % 7 == 0 and var1 % 5 == 0:
        resultado = 'fizzbuzz'
        return resultado


def nao_multiplo(var1):
    if var1 % 7 != 0 and 0 != var1 % 5:
        resultado = 'miss'
        return resultado

