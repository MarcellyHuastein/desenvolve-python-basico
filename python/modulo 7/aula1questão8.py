def calcular_digito_verificador(digitos):
    """
    Calcula o dígito verificador baseado nos 9 primeiros dígitos.
    """
    soma = 0
    multiplicador = 10
    
    for digito in digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)

def validar_cpf(cpf):
    """
    Valida um CPF conforme as regras de cálculo dos dígitos verificadores.
    """
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return "Inválido"

    # Calcula o primeiro dígito verificador
    primeiros_nove_digitos = cpf[:9]
    primeiro_digito_calculado = calcular_digito_verificador(primeiros_nove_digitos)
    
    # Calcula o segundo dígito verificador
    primeiro_digito = primeiro_digito_calculado
    segundo_digito_calculado = calcular_digito_verificador(primeiros_nove_digitos + primeiro_digito)
    
    # Verifica se os dígitos calculados correspondem aos dígitos fornecidos
    if cpf[-2:] == primeiro_digito_calculado + segundo_digito_calculado:
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF do usuário
cpf_usuario = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# Valida o CPF e exibe o resultado
resultado = validar_cpf(cpf_usuario)
print(resultado)
