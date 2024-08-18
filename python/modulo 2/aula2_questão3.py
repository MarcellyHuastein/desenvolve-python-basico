# Inicializando as variáveis
v1 = 10
v2 = 20

# Usando uma variável auxiliar para trocar os valores
aux = v1  # Armazenando o valor de v1 na variável auxiliar
v1 = v2   # Atribuindo o valor de v2 a v1
v2 = aux  # Atribuindo o valor armazenado em aux a v2

# Imprimindo os valores finais das variáveis
print("v1:", v1)  # Deve imprimir 20
print("v2:", v2)  # Deve imprimir 10