def validarCPF(CPF:str) -> bool:
    return True
def validarCNPJ(CNPJ:str) -> bool:
    return True
def validarEmail(Email:str) -> bool:
    return True
def validarCelular(celular:str) -> bool:
    return True
def validarTelefoneFixo(telefoneFixo: str) -> bool:
    return True
def validarCEP(CEP: str) -> bool:
    return True
def validarData(data: str) -> bool:
    return True
def validarCPF_CNPJ(CPF_CNPJ: str,tipo: str) -> bool:
    return (validarCPF(CPF_CNPJ) and  tipo == "Pessoa") or (validarCNPJ(CPF_CNPJ) and  tipo == "Empresa")
def validarCodigoBarras(codigoBarras: str) -> bool:
    return True
