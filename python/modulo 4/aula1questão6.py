# Função para calcular e imprimir os resultados
def organizar_experimentos():
    # Lê o número total de experimentos
    N = int(input("Digite o número de experimentos: "))
    
    # Inicializa contadores
    total_cobaias = 0
    total_sapos = 0
    total_ratos = 0
    total_coelhos = 0
    
    # Processa cada experimento
    for _ in range(N):
        # Lê a quantidade e o tipo de cobaia
        entrada = input().strip().split()
        quantia = int(entrada[0])
        tipo = entrada[1].lower()  # Converte o tipo para minúscula
        
        # Atualiza os contadores
        total_cobaias += quantia
        if tipo == 's':
            total_sapos += quantia
        elif tipo == 'r':
            total_ratos += quantia
        elif tipo == 'c':
            total_coelhos += quantia
    
    # Calcula os percentuais
    percentual_sapos = (total_sapos / total_cobaias) * 100
    percentual_ratos = (total_ratos / total_cobaias) * 100
    percentual_coelhos = (total_coelhos / total_cobaias) * 100
    
    # Imprime os resultados
    print(f"total: {total_cobaias} cobaias")
    print(f"total de coelhos: {total_coelhos}")
    print(f"total de ratos: {total_ratos}")
    print(f"total de sapos: {total_sapos}")
    print(f"percentual de coelhos: {percentual_coelhos:.2f}%")
    print(f"percentual de ratos: {percentual_ratos:.2f}%")
    print(f"percentual de sapos: {percentual_sapos:.2f}%")

# Executa a função
organizar_experimentos()
