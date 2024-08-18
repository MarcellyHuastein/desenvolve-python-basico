def substituir_vogais(frase):
    # Define as vogais (minúsculas e maiúsculas)
    vogais = "aeiouAEIOU"
    
    # Substitui cada ocorrência de vogal por '*'
    frase_modificada = ''.join('*' if caractere in vogais else caractere for caractere in frase)
    
    return frase_modificada

# Solicita a frase do usuário
frase_usuario = input("Digite uma frase: ")

# Substitui as vogais por '*' e exibe a frase modificada
frase_modificada = substituir_vogais(frase_usuario)
print(f"Frase modificada: {frase_modificada}")
