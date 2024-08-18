# Solicitando a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()  # Lê a classe e transforma em minúscula

# Solicitando os pontos de força e magia
forca = int(input("Digite os pontos de força (de 1 a 20): "))  # Lê os pontos de força e converte para inteiro
magia = int(input("Digite os pontos de magia (de 1 a 20): "))  # Lê os pontos de magia e converte para inteiro

# Validando os pontos de atributo de acordo com a classe escolhida
if classe == "guerreiro":
    # Requisitos para Guerreiro
    atributos_validos = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    # Requisitos para Mago
    atributos_validos = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    # Requisitos para Arqueiro
    atributos_validos = (forca > 5) and (forca <= 15) and (magia > 5) and (magia <= 15)
else:
    # Classe inválida
    atributos_validos = False

# Imprimindo se os pontos de atributo são consistentes com a classe escolhida
print(f"Pontos de atributo consistentes com a classe escolhida: {atributos_validos}")
