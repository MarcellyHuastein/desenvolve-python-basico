# Solicita o número do celular do usuário
numero = input("Digite o número: ")

# Remove caracteres não numéricos (por exemplo, espaços ou parênteses)
numero = ''.join(filter(str.isdigit, numero))

# Verifica o comprimento do número
if len(numero) == 8:
    # Adiciona o 9 na frente
    numero = '9' + numero

# Verifica se o número já tem 9 dígitos
if len(numero) == 9:
    # Verifica se o primeiro dígito é 9
    if numero[0] != '9':
        print("Número inválido. O número com 9 dígitos deve começar com 9.")
        exit()

# Adiciona o separador "-" e formata o número
numero_formatado = f"{numero[:5]}-{numero[5:]}"

# Exibe o número completo formatado
print(f"Número completo: {numero_formatado}")
