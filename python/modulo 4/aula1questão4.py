# Solicita ao usuário que insira o número de valores
n = int(input("Digite o número de valores: "))

# Inicializa a variável maior com 0
maior = 0

# Enquanto n for maior que 0, continua lendo valores e comparando
while n > 0:
    # Solicita ao usuário que insira um valor
    x = float(input("Digite um valor: "))
    
    # Verifica se x é maior que maior
    if x > maior:
        maior = x
    
    # Decrementa o contador n
    n = n - 1

# Após o loop, imprime o maior valor encontrado
print("O maior valor é:", maior)
