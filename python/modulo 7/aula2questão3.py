import string

def eh_palindromo(frase):
    # Remove espaços em branco, sinais de pontuação e converte para minúsculas
    frase_limpa = ''.join(c.lower() for c in frase if c not in string.whitespace and c not in string.punctuation)
    
    # Verifica se a frase limpa é igual ao seu reverso
    return frase_limpa == frase_limpa[::-1]

def main():
    while True:
        # Solicita a frase do usuário
        frase_usuario = input('Digite uma frase (digite "fim" para encerrar): ')
        
        # Verifica se o usuário quer encerrar
        if frase_usuario.lower() == 'fim':
            break
        
        # Verifica se a frase é um palíndromo e exibe o resultado
        if eh_palindromo(frase_usuario):
            print(f'"{frase_usuario}" é palíndromo')
        else:
            print(f'"{frase_usuario}" não é palíndromo')

# Executa o programa principal
main()
