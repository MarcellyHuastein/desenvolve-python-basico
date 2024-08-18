from collections import Counter

def encontrar_anagramas(palavra_objetivo, frase):
    # Normaliza a palavra objetivo (minúsculas e remove espaços)
    palavra_objetivo = palavra_objetivo.lower()
    
    # Conta a frequência de cada caractere na palavra objetivo
    contagem_objetivo = Counter(palavra_objetivo)
    
    # Separa a frase em palavras
    palavras = frase.split()
    
    # Lista para armazenar anagramas encontrados
    anagramas = []
    
    # Verifica cada palavra na frase
    for palavra in palavras:
        palavra_normalizada = palavra.lower()
        # Conta a frequência de cada caractere na palavra
        contagem_palavra = Counter(palavra_normalizada)
        
        # Verifica se a contagem de caracteres da palavra é igual à contagem da palavra objetivo
        if contagem_palavra == contagem_objetivo:
            anagramas.append(palavra)
    
    return anagramas

# Solicita a frase e a palavra objetivo do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Encontra os anagramas
anagramas = encontrar_anagramas(palavra_objetivo, frase)

# Exibe os anagramas encontrados
print("Anagramas:", anagramas)
