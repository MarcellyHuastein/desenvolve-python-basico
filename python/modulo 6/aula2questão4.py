def main():
    # Solicitar e ler a quantidade de elementos da lista 1
    n1 = int(input("Digite a quantidade de elementos da lista 1: "))
    lista1 = []
    print(f"Digite os {n1} elementos da lista 1:")
    for _ in range(n1):
        lista1.append(int(input()))
    
    # Solicitar e ler a quantidade de elementos da lista 2
    n2 = int(input("Digite a quantidade de elementos da lista 2: "))
    lista2 = []
    print(f"Digite os {n2} elementos da lista 2:")
    for _ in range(n2):
        lista2.append(int(input()))
    
    # Criar a lista intercalada
    lista_intercalada = []
    min_len = min(len(lista1), len(lista2))
    
    # Intercalar os elementos
    for i in range(min_len):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    # Adicionar os elementos restantes da lista maior
    if len(lista1) > len(lista2):
        lista_intercalada.extend(lista1[min_len:])
    else:
        lista_intercalada.extend(lista2[min_len:])
    
    # Imprimir a lista intercalada
    print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

# Executa o programa principal
if __name__ == "__main__":
    main()
