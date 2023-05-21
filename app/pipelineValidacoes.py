from typing import List, Tuple 

def Executar(validacoes: List[Tuple[bool,str]]) -> Tuple[bool,str]:
    for validacao in validacoes:
        if validacao[0] == False:
            return validacao
    return True,"Sucess"
    