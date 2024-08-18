import re

def processar_arquivo():
    # Nome dos arquivos
    arquivo_entrada = "frase.txt"
    arquivo_saida = "palavras.txt"
    
    # Lê o conteúdo do arquivo de entrada
    with open(arquivo_entrada, 'r') as arquivo:
        conteudo = arquivo.read()
    
    # Remove caracteres não alfabéticos e espaços
    palavras = re.findall(r'[a-zA-Z]+', conteudo)
    
    # Escreve as palavras no arquivo de saída, uma por linha
    with open(arquivo_saida, 'w') as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + '\n')
    
    # Lê e imprime o conteúdo do arquivo de saída
    with open(arquivo_saida, 'r') as arquivo:
        conteudo_saida = arquivo.read()
    
    print(conteudo_saida)

# Executa a função
processar_arquivo()
