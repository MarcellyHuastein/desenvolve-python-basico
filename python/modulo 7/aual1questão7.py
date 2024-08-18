import random

def encrypt(nomes):
    # Gera uma chave aleatória entre 1 e 10
    chave = random.randint(1, 10)
    
    # Função para criptografar um único caractere
    def criptografar_caractere(c):
        # Obtém o código Unicode do caractere e adiciona a chave
        codigo = ord(c) + chave
        
        # Garante que o código resultante esteja dentro do intervalo visível (33 a 126)
        if codigo > 126:
            codigo = 33 + (codigo - 127)
        
        return chr(codigo)
    
    # Criptografa cada nome na lista
    nomes_criptografados = []
    for nome in nomes:
        nome_criptografado = ''.join(criptografar_caractere(c) for c in nome)
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

# Lista de nomes para criptografar
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Chama a função e obtém os nomes criptografados e a chave
nomes_criptografados, chave = encrypt(nomes)

# Exibe o resultado
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
