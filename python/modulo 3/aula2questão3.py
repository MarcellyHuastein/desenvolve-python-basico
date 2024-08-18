# Solicitando a idade do usuário
idade = int(input("Digite sua idade: "))  # Lê a idade do usuário e converte para inteiro

# Solicitando se o usuário já jogou pelo menos 3 jogos de tabuleiro
jogou_pelo_menos_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True ou False): ") == "True"  # Lê a resposta como string e converte para booleano

# Solicitando o número de jogos vencidos
vencedor = int(input("Quantos jogos já venceu? "))  # Lê o número de jogos vencidos e converte para inteiro

# Verificando se o usuário atende aos critérios para ingressar no clube
aptos_para_ingressar = (16 <= idade <= 18) and jogou_pelo_menos_3_jogos and (vencedor >= 1)

# Imprimindo se o usuário está apto para ingressar no clube
print(f"Apto para ingressar no clube de jogos de tabuleiro: {aptos_para_ingressar}")
