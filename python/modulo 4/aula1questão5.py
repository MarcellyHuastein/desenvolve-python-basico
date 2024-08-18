# Solicita ao usuário que insira o número de respondentes
N = int(input("Digite o número de respondentes: "))

# Inicializa a soma das idades
soma_idades = 0

# Loop para ler as idades dos respondentes
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    soma_idades += idade

# Calcula a média das idades
media_idades = soma_idades / N

# Imprime a média das idades
print(f"A média das idades é: {media_idades:.2f}")
