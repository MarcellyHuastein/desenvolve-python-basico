import re

def processar_arquivo():
    nome_arquivo = "estomago.txt"
    
    # Variáveis para armazenar informações do arquivo
    linhas = []
    num_linhas = 0
    maior_linha = ""
    
    # Lê o arquivo e armazena as linhas
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        num_linhas = len(linhas)
        
        # Encontra a linha com maior número de caracteres
        maior_linha = max(linhas, key=len)
    
    # Imprime as primeiras 25 linhas
    print("Primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())
    
    # Imprime o número total de linhas
    print(f"\nNúmero total de linhas: {num_linhas}")
    
    # Imprime a linha com maior número de caracteres
    print(f"\nLinha com maior número de caracteres:\n{maior_linha.strip()}")
    
    # Contagem de menções aos nomes dos personagens
    texto = ''.join(linhas).lower()  # Junta todo o texto e converte para minúsculas
    
    # Usa regex para encontrar as menções exatas dos personagens
    count_nonato = len(re.findall(r'\bnonato\b', texto))
    count_iria = len(re.findall(r'\bíria\b', texto))
    
    # Imprime o número de menções aos nomes dos personagens
    print(f"\nNúmero de menções a 'Nonato': {count_nonato}")
    print(f"Número de menções a 'Íria': {count_iria}")

# Executa a função
processar_arquivo()
