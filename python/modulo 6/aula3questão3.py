import random

def encontrar_intervalo_maior_negativos(lista):
    max_negativos = 0
    melhor_inicio = 0
    melhor_fim = 0
    
    n = len(lista)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublista = lista[i:j]
            num_negativos = sum(1 for x in sublista if x < 0)
            if num_negativos > max_negativos:
                max_negativos = num_negativos
                melhor_inicio = i
                melhor_fim = j
    
    return melhor_inicio, melhor_fim

def main():
    # Gerar uma lista com 20 elementos aleatórios entre -10 e 10
    lista = [random.randint(-10, 10) for _ in range(20)]
    
    print("Original:", lista)
    
    # Encontrar o intervalo com mais números negativos
    inicio, fim = encontrar_intervalo_maior_negativos(lista)
    
    # Deletar o intervalo encontrado da lista
    del lista[inicio:fim]
    
    # Imprimir a lista editada
    print("Editada:", lista)

# Executa o programa principal
if __name__ == "__main__":
    main()
