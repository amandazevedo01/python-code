import pytest
from Modulos.gera_fibonacci import Fibonacci

class TesteExercicio:

    def setup(self):
        pass

    def test_multiplo5(self):
        resultado = multiplo5(5)

        assert resultado == 'fizz'

    def test_multiplo7(self):
        resultado = multiplo7(7)

        assert resultado == 'buzz'

    def test_multiplo5e7(self):
        resultado = multiplo5e7(35)

        assert resultado == 'fizzbuzz'

    def test_nao_multiplo(self):
        resultado = nao_multiplo(2)

        assert resultado == 'miss'