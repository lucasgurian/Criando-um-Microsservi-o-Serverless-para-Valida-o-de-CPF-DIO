import re

def is_cpf_valid(cpf: str) -> bool:
    """
    Valida um número de CPF brasileiro.

    Args:
        cpf: O número de CPF a ser validado.

    Returns:
        True se o CPF for válido, False caso contrário.
    """
    # Remove caracteres não numéricos
    cpf = ''.join(re.findall(r'\d', str(cpf)))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True
