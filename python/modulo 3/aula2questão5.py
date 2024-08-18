# Solicitando o gênero do usuário
genero = input("Digite seu gênero (M ou F): ").strip().upper()  # Lê o gênero e transforma em maiúsculas

# Solicitando a idade e o tempo de serviço
idade = int(input("Digite sua idade: "))  # Lê a idade e converte para inteiro
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))  # Lê o tempo de serviço e converte para inteiro

# Verificando se o usuário pode se aposentar
pode_aposentar = (
    (genero == "F" and idade > 60) or  # Mulheres com mais de 60 anos
    (genero == "M" and idade > 65) or  # Homens com mais de 65 anos
    (tempo_servico >= 30) or           # Tempo de serviço de pelo menos 30 anos
    (idade == 60 and tempo_servico >= 25)  # 60 anos e pelo menos 25 anos de serviço
)

# Imprimindo se a pessoa pode se aposentar
print(pode_aposentar)
