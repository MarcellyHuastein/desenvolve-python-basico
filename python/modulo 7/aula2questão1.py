def converter_data_para_extenso(data):
    # Lista com os nomes dos meses
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Separa a data em dia, mês e ano
    dia, mes, ano = data.split('/')
    
    # Converte o mês para o índice da lista (note que o mês é 1-12 e a lista é 0-11)
    mes_extenso = meses[int(mes) - 1]
    
    # Retorna a data formatada
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

# Solicita a data de nascimento do usuário
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

# Converte e exibe a data com o nome do mês por extenso
data_formatada = converter_data_para_extenso(data_nascimento)
print(data_formatada)
