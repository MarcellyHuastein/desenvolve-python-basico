# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Definindo as vogais
vogais = 'aeiouAEIOU'

# Compreensão de listas para encontrar vogais na frase e ordená-las
lista_vogais = sorted([char for char in frase if char in vogais])

# Compreensão de listas para encontrar consoantes na frase
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

# Imprimindo os resultados
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
