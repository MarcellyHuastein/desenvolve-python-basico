# Solicitando o primeiro número
numero1 = int(input("Digite o primeiro número: "))  # Lê o primeiro número e converte para inteiro

# Solicitando o segundo número
numero2 = int(input("Digite o segundo número: "))  # Lê o segundo número e converte para inteiro

# Calculando a soma dos dois números
soma = numero1 + numero2

# Verificando se a soma é par ou ímpar
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
