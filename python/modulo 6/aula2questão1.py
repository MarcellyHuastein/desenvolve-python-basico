import random

def main():
    # Gerar 20 valores inteiros aleatórios entre -100 e 100
    lista_original = [random.randint(-100, 100) for _ in range(20)]
    
    # Ordenar a lista sem modificar a lista original
    lista_ordenada = sorted(lista_original)
    
    # Encontrar o índice do maior valor
    maior_valor = max(lista_original)
    indice_maior = lista_original.index(maior_valor)
    
    # Encontrar o índice do menor valor
    menor_valor = min(lista_original)
    indice_menor = lista_original.index(menor_valor)
    
    # Imprimir a lista ordenada
    print("Lista ordenada:", lista_ordenada)
    
    # Imprimir a lista original
    print("Lista original:", lista_original)
    
    # Imprimir o índice do maior valor
    print("Índice do maior valor:", indice_maior)
    
    # Imprimir o índice do menor valor
    print("Índice do menor valor:", indice_menor)

# Executa o programa principal
if __name__ == "__main__":
    main()
