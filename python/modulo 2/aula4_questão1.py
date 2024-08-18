# Lendo as dimensões do terreno e o preço do metro quadrado
comprimento = int(input("Digite o comprimento do terreno em metros: "))  # Lê o comprimento do terreno como um número inteiro
largura = int(input("Digite a largura do terreno em metros: "))        # Lê a largura do terreno como um número inteiro
preco_m2 = float(input("Digite o preço do metro quadrado em reais: "))  # Lê o preço do metro quadrado como um número ponto flutuante

# Calculando a área do terreno em metros quadrados
area_m2 = comprimento * largura  # Multiplica comprimento e largura para obter a área total do terreno

# Calculando o valor total do terreno
preco_total = preco_m2 * area_m2  # Multiplica o preço por metro quadrado pela área total para obter o valor do terreno

# Imprimindo o valor do terreno com formatação
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")  # Imprime a área do terreno e o valor total formatado com duas casas decimais e separadores de milhar
