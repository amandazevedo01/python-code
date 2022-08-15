import pytest

class Fibonacci:
    def __iter__(self):
        self.anterior = 0
        self.proximo = 1
        self.interacao = ""
        return self

    def __next__(self):
        sequencia_fibonacci = [self.anterior]
        try:
            self.interacao = int(input("Digite a quantidade da sequência Fibonacci: "))
            if self.interacao == 0:
                raise StopIteration
        except:
            print("!!! Operação cancelada !!!")
        for x in range(self.interacao - 1):
            valor_fibonacci = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = valor_fibonacci
            sequencia_fibonacci.append(self.proximo)

        assert len(sequencia_fibonacci) == self.interacao
        return sequencia_fibonacci