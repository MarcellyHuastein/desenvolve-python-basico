import random
from collections import Counter

def main():
    # Gerar duas listas com 20 valores aleatórios entre 0 e 50
    lista1 = [random.randint(0, 50) for _ in range(20)]
    lista2 = [random.randint(0, 50) for _ in range(20)]
    
    # Contar a frequência de cada valor em lista1 e lista2
    contador1 = Counter(lista1)
    contador2 = Counter(lista2)
    
    # Encontrar a interseção das duas listas e remover duplicatas
    interseccao = list(set(lista1) & set(lista2))
    
    # Ordenar a lista de interseção
    interseccao.sort()
    
    # Imprimir as listas e a interseção
    print("Lista1:", lista1)
    print("Lista2:", lista2)
    print("Interseccao:", interseccao)
    
    # Imprimir a contagem de cada elemento em ambas as listas
    print("Contagem")
    for valor in interseccao:
        cont_lista1 = contador1.get(valor, 0)
        cont_lista2 = contador2.get(valor, 0)
        print(f"{valor}: (lista1={cont_lista1}, lista2={cont_lista2})")

# Executa o programa principal
if __name__ == "__main__":
    main()
