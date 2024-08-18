# Definindo as variáveis
juros = 1.01
saldo = 500.0

# Atualizando o saldo para cada mês
for _ in range(3):
    saldo *= juros

# Imprimindo o novo saldo após 3 meses
print("Após 3 meses meu novo saldo é")
print(saldo)