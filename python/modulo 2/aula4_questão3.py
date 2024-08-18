# Solicitando os dados dos produtos
nome_produto1 = input("Digite o nome do produto 1: ")  # Lê o nome do primeiro produto
preco_unitario1 = float(input("Digite o preço unitário do produto 1: "))  # Lê o preço unitário do primeiro produto e converte para float
quantidade1 = int(input("Digite a quantidade do produto 1: "))  # Lê a quantidade do primeiro produto e converte para inteiro

nome_produto2 = input("Digite o nome do produto 2: ")  # Lê o nome do segundo produto
preco_unitario2 = float(input("Digite o preço unitário do produto 2: "))  # Lê o preço unitário do segundo produto e converte para float
quantidade2 = int(input("Digite a quantidade do produto 2: "))  # Lê a quantidade do segundo produto e converte para inteiro

nome_produto3 = input("Digite o nome do produto 3: ")  # Lê o nome do terceiro produto
preco_unitario3 = float(input("Digite o preço unitário do produto 3: "))  # Lê o preço unitário do terceiro produto e converte para float
quantidade3 = int(input("Digite a quantidade do produto 3: "))  # Lê a quantidade do terceiro produto e converte para inteiro

# Calculando o preço total
preco_total = (preco_unitario1 * quantidade1) + (preco_unitario2 * quantidade2) + (preco_unitario3 * quantidade3)

# Imprimindo o total formatado
print(f"Total: R${preco_total:,.2f}")
