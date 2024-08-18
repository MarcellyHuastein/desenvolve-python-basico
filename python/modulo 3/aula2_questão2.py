# Solicitando as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))  # Lê a idade de Juliana e converte para inteiro
idade_cris = int(input("Digite a idade de Cris: "))        # Lê a idade de Cris e converte para inteiro

# Verificando se pelo menos uma das pessoas é maior de 17 anos
pode_entrar = (idade_juliana > 17) or (idade_cris > 17)  # Verifica se pelo menos uma das idades é maior que 17

# Imprimindo o resultado
print(pode_entrar)  # Imprime True se pelo menos uma for maior de 17 anos, caso contrário, False
