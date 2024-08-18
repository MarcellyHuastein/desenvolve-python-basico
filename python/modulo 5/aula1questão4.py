from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Formata a data e hora no formato desejado
data_formatada = f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"Hora: {agora.hour:02d}:{agora.minute:02d}"

# Exibe a data e a hora formatadas
print(data_formatada)
print(hora_formatada)
