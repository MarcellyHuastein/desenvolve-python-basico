import string

def validador_senha(senha):
    # Verifica o comprimento da senha
    if len(senha) < 8:
        return False
    
    # Inicializa flags para cada critério
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    
    # Verifica cada caractere na senha
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in string.punctuation:
            tem_caractere_especial = True
    
    # Verifica se todos os critérios foram atendidos
    return tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial

# Exemplo de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
