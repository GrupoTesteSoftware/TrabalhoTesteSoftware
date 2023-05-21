import unittest
import sys 
import os
sys.path.append(os.path.abspath('..'))
import Packages.validadores as validadores

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        cpf = '123.456.789-09'
        resultado = validadores.validarCPF(cpf)
        self.assertTrue(resultado)  # Espera-se que o resultado seja True

    def test_cpf_invalido(self):
        cpf = '123.456.789-10'
        resultado = validadores.validarCPF(cpf)
        self.assertFalse(resultado)  # Espera-se que o resultado seja False

    def test_cpf_formato_incorreto(self):
        cpf = '12345678910'  # Formato incorreto (sem pontos e traço)
        resultado = validadores.validarCPF(cpf)
        self.assertFalse(resultado)  # Espera-se que o resultado seja False

class TestValidarCNPJ(unittest.TestCase):
    def test_cnpj_valido(self):
        cnpj_valido = '12.345.678/0001-90'
        self.assertTrue(validadores.validarCNPJ(cnpj_valido))  # Espera-se que o resultado seja True

    def test_cnpj_invalido(self):
        cnpj_invalido = '12.345.678/0001-91'
        self.assertFalse(validadores.validarCNPJ(cnpj_invalido))  # Espera-se que o resultado seja False

class TestValidarCEP(unittest.TestCase):
    def test_cep_valido(self):
        cep_valido = '12345-678'
        self.assertTrue(validadores.validarCEP(cep_valido))  # Espera-se que o resultado seja True

    def test_cep_invalido(self):
        cep_invalido = '12345678'
        self.assertFalse(validadores.validarCEP(cep_invalido))  # Espera-se que o resultado seja False

class TestValidarTelefoneFixo(unittest.TestCase):
    def test_telefone_valido(self):
        telefone_valido = '(12) 3456-7890'
        self.assertTrue(validadores.validarTelefoneFixo(telefone_valido))  # Espera-se que o resultado seja True

    def test_telefone_invalido(self):
        telefone_invalido = '(12) 3456-78901'
        self.assertFalse(validadores.validarTelefoneFixo(telefone_invalido))  # Espera-se que o resultado seja False
class TestValidarCelular(unittest.TestCase):
    def test_celular_oito_digitos_valido(self):
        celular_valido = '(31) 9123-4567'
        self.assertTrue(validadores.validarCelular(celular_valido))  # Espera-se que o resultado seja True

    def test_celular_oito_digitos_invalido(self):
        celular_invalido = '(31) 9123a-456'
        self.assertFalse(validadores.validarCelular(celular_invalido))  # Espera-se que o resultado seja False

    def test_celular_nove_digitos_valido(self):
        celular_valido = '(21) 91234-5678'
        self.assertTrue(validadores.validarCelular(celular_valido))  # Espera-se que o resultado seja True

    def test_celular_nove_digitos_invalido(self):
        celular_invalido = '(31) 912 34-567 89'
        self.assertFalse(validadores.validarCelular(celular_invalido))  # Espera-se que o resultado seja False
class TestValidarEmail(unittest.TestCase):
    def test_email_valido(self):
        email_valido = 'exemplo@example.com.br'
        self.assertTrue(validadores.validarEmail(email_valido))  # Espera-se que o resultado seja True

    def test_email_invalido(self):
        email_invalido = 'exemploexample.com'
        self.assertFalse(validadores.validarEmail(email_invalido))  # Espera-se que o resultado seja False


class Testdata(unittest.TestCase):
    def test_email_valido(self):
        email_valido = 'exemplo@example.com'
        self.assertTrue(validadores.validarEmail(email_valido))  # Espera-se que o resultado seja True

    def test_email_invalido(self):
        email_invalido = 'exemploexample.com'
        self.assertFalse(validadores.validarEmail(email_invalido))  # Espera-se que o resultado seja False

if __name__ == '__main__':
    unittest.main()