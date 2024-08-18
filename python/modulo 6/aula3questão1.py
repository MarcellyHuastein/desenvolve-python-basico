def main():
    # Solicitar números ao usuário até que o usuário digite uma entrada não válida
    lista = []
    print("Digite pelo menos 4 números inteiros. Para finalizar a entrada, digite 'fim':")
    
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            if len(lista) < 4:
                print("Por favor, digite pelo menos 4 números.")
            else:
                break
        else:
            try:
                numero = int(entrada)
                lista.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro ou 'fim' para finalizar.")
    
    # Fatiamento e impressão dos resultados
    print("Lista original:", lista)
    print("Os 3 primeiros elementos:", lista[:3])
    print("Os 2 últimos elementos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[::2])
    print("Elementos de índice ímpar:", lista[1::2])

# Executa o programa principal
if __name__ == "__main__":
    main()
