# Solicitando a distância da entrega e o peso do pacote
distancia = float(input("Digite a distância da entrega (em km): "))  # Lê a distância e converte para float
peso = float(input("Digite o peso do pacote (em kg): "))  # Lê o peso e converte para float

# Calculando o valor do frete com base na distância
if distancia <= 100:
    valor_por_kg = 1.00
elif 101 <= distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

# Calculando o valor total do frete
frete = valor_por_kg * peso

# Adicionando a taxa extra para pacotes com peso superior a 10 kg
if peso > 10:
    frete += 10.00

# Imprimindo o valor total do frete
print(f"Valor do frete: R${frete:.2f}")
