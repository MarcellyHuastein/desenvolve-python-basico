import os

def salvar_frase():
    # Solicita uma frase ao usuário
    frase = input("Digite uma frase: ")
    
    # Define o nome do arquivo
    nome_arquivo = "frase.txt"
    
    # Abre o arquivo no modo de escrita e salva a frase
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(frase)
    
    # Obtém o caminho absoluto do arquivo
    caminho_absoluto = os.path.abspath(nome_arquivo)
    
    # Imprime o caminho completo do arquivo
    print(f"Frase salva em {caminho_absoluto}")

# Executa a função
salvar_frase()
