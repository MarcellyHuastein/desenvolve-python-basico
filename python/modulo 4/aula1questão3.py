# Solicita ao usuário que insira três valores
n1 = float(input("Digite o valor de n1: "))
n2 = float(input("Digite o valor de n2: "))
n3 = float(input("Digite o valor de n3: "))

# Calcula a média
m = (n1 + n2 + n3) / 3

# Verifica a média e imprime o resultado adequado
if m >= 60:
    print("aprovado")
elif m >= 40:
    print("recuperação")
else:
    print("reprovado")

# Imprime "fim" após o resultado
print("fim")
