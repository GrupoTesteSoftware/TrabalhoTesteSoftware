import unittest
import sys 
import os
sys.path.append(os.path.abspath('..'))
import Packages.validadores as validadores

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        cpf = '123.456.789-09'
        resultado = validadores(cpf)
        self.assertTrue(resultado)  # Espera-se que o resultado seja True

    def test_cpf_invalido(self):
        cpf = '123.456.789-10'
        resultado = validadores(cpf)
        self.assertFalse(resultado)  # Espera-se que o resultado seja False

    def test_cpf_formato_incorreto(self):
        cpf = '12345678910'  # Formato incorreto (sem pontos e traço)
        resultado = validadores(cpf)
        self.assertFalse(resultado)  # Espera-se que o resultado seja False

if __name__ == '__main__':
    unittest.main()