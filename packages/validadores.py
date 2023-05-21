import re

def validarCPF(CPF:str) -> bool:
    cpf_standard = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}$")
    legal_format = cpf_standard.match(cpf)
    if(not legal_format):
      return False
    
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    init_cpf = cpf
    cpf = cpf[:9]
    
    checksum = 0
    mult = 10
    for num in range(9):
        checksum += int(cpf[num]) * (mult - int(num))
    rest = checksum % 11
    if(rest<2):
        first_digit = 0
    else:
        first_digit = 11-rest
    cpf += str(first_digit)

    checksum = 0
    mult = 11
    for num in range(10):
        checksum += int(cpf[num]) * (mult - int(num))
    rest = checksum % 11
    if(rest<2):
        second_digit = 0
    else:
        second_digit = 11-rest
    cpf += str(second_digit)

    return cpf==init_cpf

def validarCNPJ(cnpj:str) -> bool:
  cnpj_standard = re.compile("[0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2}$")
  legal_format = cnpj_standard.match(cnpj)
  if(not legal_format):
    return False
  
  cnpj = cnpj.replace('.', '')
  cnpj = cnpj.replace('-', '')
  cnpj = cnpj.replace('/', '')
  init_cnpj = cnpj
  cnpj = cnpj[:12]

  checksum = 0
  mult = [5,4,3,2,9,8,7,6,5,4,3,2]
  for num in range(12):
    checksum += int(cnpj[num]) * mult[num]
  rest = checksum % 11
  if(rest<2):
    first_digit = 0
  else:
    first_digit = 11 - rest
  cnpj += str(first_digit)

  checksum = 0
  mult = [6,5,4,3,2,9,8,7,6,5,4,3,2]
  for num in range(13):
    checksum += int(cnpj[num]) * mult[num]
  rest = checksum % 11
  if(rest<2):
    second_digit = 0
  else:
    second_digit = 11 - rest
  cnpj += str(second_digit)

  return cnpj==init_cnpj

def validarEmail(email:str) -> bool:
  size = len(email)
  at, dot, dot_before_at ,dot_after_at = 0, 0, 0, 0
  for i in range(size):
    symbol = email[i]
    if(symbol=='@'):
      if(at>0):
        return False
      at += 1
      if(i<3):
        return False
    elif(at>0):
      if(dot>0):
        dot_after_at += 1
      elif(symbol=='.'):
        dot = 1
        if(dot_before_at<3):
          return False
      else:
        dot_before_at += 1
  if(i+1==size and dot_after_at>1):
    return True
  else:
    return False

def validarCelular(celular:str) -> bool:
  celular = celular.replace('+', '')
  celular = celular.replace('(', '')
  celular = celular.replace(')', '')
  celular = celular.replace('-', '')
  celular = celular.replace(' ', '')
  celular = celular.removeprefix('0')

  size = len(celular)
  if(size==12 or size==13):
    ddi = celular[:2] 
    if(ddi!="55"):
      return False
    celular = celular[2:]
    size = len(celular)
  
  ddds = re.compile("(1[1-9]|2[12478]|3[1-578])|4[1-9]|5[13-5]|6[1-9]|7[13-579]|8[1-9]|9[1-9]")
  valid_ddd = ddds.match(celular)
  if(not valid_ddd):
    return False
  
  if(size<10 or size>11):
    return False

  if(size==11 and celular[2]!='9'):
    return False

  valid_prefixes = ['6','7','8','9']
  if(celular[-8] not in valid_prefixes):
    return False
  
  return True

def validarTelefoneFixo(telefoneFixo: str) -> bool:
  telefoneFixo = telefoneFixo.replace('+', '')
  telefoneFixo = telefoneFixo.replace('(', '')
  telefoneFixo = telefoneFixo.replace(')', '')
  telefoneFixo = telefoneFixo.replace('-', '')
  telefoneFixo = telefoneFixo.replace(' ', '')
  telefoneFixo = telefoneFixo.removeprefix('0')

  size = len(telefoneFixo)
  
  ddds = re.compile("(1[1-9]|2[12478]|3[1-578])|4[1-9]|5[13-5]|6[1-9]|7[13-579]|8[1-9]|9[1-9]")
  valid_ddd = ddds.match(telefoneFixo)
  if(not valid_ddd):
    return False
  
  if(size!=10):
    return False

  valid_prefixes = ['2','3','4','5']
  if(telefoneFixo[-8] not in valid_prefixes):
    return False
  
  return True

def validarCEP(cep: str) -> bool:
  cep_standard = re.compile("[0-9]{2}[.]?[0-9]{3}[-]?[0-9]{3}$")
  legal_format = cep_standard.match(cep)
  if(not legal_format):
    return False
  return True

def validarCodigoBarras(codigoBarras: str) -> bool:
  return True 