import random

def carrega_palavras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

def carrega_estagios(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        estagios = arquivo.read().splitlines()
    return estagios

def imprime_enforcado(erros, estagios):
    if erros < len(estagios):
        print(estagios[erros])
    else:
        print("Número de erros excedido. Jogo perdido!")

def jogo_forca():
    palavras = carrega_palavras("gabarito_forca.txt")
    estagios = carrega_estagios("gabarito_enforcado.txt")
    
    palavra = random.choice(palavras).upper()
    palavras_ocultas = ['_'] * len(palavra)
    tentativas = 6
    erros = 0
    letras_erradas = set()
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while erros < tentativas and '_' in palavras_ocultas:
        print("\n" + " ".join(palavras_ocultas))
        print(f"Tentativas restantes: {tentativas - erros}")
        print("Letras erradas: " + ", ".join(letras_erradas))
        letra = input("Digite uma letra: ").upper()
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavras_ocultas[i] = letra
        else:
            if letra not in letras_erradas:
                letras_erradas.add(letra)
                erros += 1
                imprime_enforcado(erros, estagios)
        
    if '_' not in palavras_ocultas:
        print(f"Parabéns! Você ganhou. A palavra era {palavra}.")
    else:
        print(f"Você perdeu. A palavra era {palavra}.")
        
# Executa o jogo
jogo_forca()
