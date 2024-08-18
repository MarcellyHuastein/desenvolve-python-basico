# Lendo a temperatura em graus Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))  # Lê o valor em Fahrenheit e converte para inteiro

# Convertendo a temperatura de Fahrenheit para Celsius
celsius = (fahrenheit - 32) * (5 / 9)  # Aplica a fórmula de conversão
celsius_int = int(celsius)  # Converte o valor em Celsius para inteiro

# Imprimindo o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius_int} graus Celsius.")
