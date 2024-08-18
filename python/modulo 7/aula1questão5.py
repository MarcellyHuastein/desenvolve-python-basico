# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define um conjunto de vogais
vogais = "aeiouAEIOU"

# Inicializa uma lista para armazenar os índices das vogais
indices_vogais = []

# Percorre cada caractere da frase e verifica se é uma vogal
for i, caractere in enumerate(frase):
    if caractere in vogais:
        indices_vogais.append(i)

# Conta o número de vogais
quantidade_vogais = len(indices_vogais)

# Exibe o resultado
print(f"{quantidade_vogais} vogais")
print(f"Índices {indices_vogais}")
