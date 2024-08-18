import random

def main():
    # Gerar aleatoriamente um valor entre 5 e 20 para num_elementos
    num_elementos = random.randint(5, 20)
    
    # Gerar aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    
    # Calcular a soma dos valores da lista
    soma = sum(elementos)
    
    # Calcular a média dos valores da lista
    media = soma / num_elementos
    
    # Imprimir a lista elementos
    print("Lista elementos:", elementos)
    
    # Imprimir a soma dos valores da lista
    print("Soma dos valores:", soma)
    
    # Imprimir a média dos valores da lista
    print("Média dos valores:", media)

# Executa o programa principal
if __name__ == "__main__":
    main()
