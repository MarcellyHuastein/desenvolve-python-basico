# Solicita ao usuário para inserir o primeiro número
primeiro_numero = float(input("Digite o primeiro número: "))

# Solicita ao usuário para inserir o segundo número
segundo_numero = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os dois números
diferenca_absoluta = abs(primeiro_numero - segundo_numero)

# Arredonda a diferença para duas casas decimais
diferenca_absoluta_arredondada = round(diferenca_absoluta, 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca_absoluta_arredondada}")
