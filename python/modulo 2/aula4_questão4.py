# Lendo o valor em reais
valor = int(input("Digite o valor em reais: "))  # Lê o valor total em reais

# Definindo as notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calculando a quantidade de notas necessárias para cada valor
print("Notas necessárias:")
for nota in notas:
    quantidade_notas = valor // nota  # Calcula a quantidade de notas do tipo atual
    valor %= nota  # Atualiza o valor restante após retirar as notas do tipo atual
    print(f"{quantidade_notas} nota(s) de R${nota},00")  # Imprime a quantidade de notas formatada
