import emoji # type: ignore

# Exibe a lista de emojis disponíveis com seus códigos
print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

# Solicita uma frase codificada ao usuário
frase_codificada = input("Digite uma frase e ela será emojizada:\n")

# Converte a frase codificada em uma frase com emojis visuais
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Exibe a frase emojizada
print("Frase emojizada:")
print(frase_emojizada)
