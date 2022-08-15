from gera_fibonacci import Fibonacci

gerar_sequencia = Fibonacci()
gerar_sequencia = iter(gerar_sequencia)
sequencia_fibonacci = {
                       posicao_da_sequencia + 1 : valor_da_sequencia for posicao_da_sequencia,
                       valor_da_sequencia in enumerate(next(gerar_sequencia))
                       }
print(sequencia_fibonacci)
