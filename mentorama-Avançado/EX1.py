from Modulos.teste_multipo_var import multiplo5, multiplo7, multiplo5e7, nao_multiplo

def var_multiplo():
    var = int(input('Digite um numero inteiro'))
    print(multiplo5(var))
    print(multiplo7(var))
    print(multiplo5e7(var))
    print(nao_multiplo(var))


var_multiplo()



