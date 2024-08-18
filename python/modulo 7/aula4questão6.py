import csv

def processar_arquivo(nome_arquivo):
    # Dicionário para armazenar a música mais tocada por ano
    musica_mais_tocada_por_ano = {}

    # Abre o arquivo CSV para leitura
    with open(nome_arquivo, mode='r', encoding='latin-1') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        
        # Pular o cabeçalho
        next(leitor)

        for linha in leitor:
            # Verificar se a linha contém a quantidade correta de colunas
            if len(linha) != 10:
                continue
            
            track_name, artist_name, artist_count, released_year, _, _, _, _, streams, _ = linha
            
            # Filtrar os dados para considerar apenas os anos de 2012 a 2022
            if not released_year.isdigit() or not streams.isdigit():
                continue

            ano = int(released_year)
            if ano < 2012 or ano > 2022:
                continue

            streams = int(streams)
            
            # Atualizar a música mais tocada do ano
            if ano not in musica_mais_tocada_por_ano or streams > musica_mais_tocada_por_ano[ano][3]:
                musica_mais_tocada_por_ano[ano] = [track_name, artist_name, ano, streams]

    # Ordenar os anos e extrair os dados
    lista_musicas = [musica_mais_tocada_por_ano[ano] for ano in sorted(musica_mais_tocada_por_ano.keys())]
    
    return lista_musicas

# Nome do arquivo CSV
nome_arquivo = 'spotify-2023.csv'

# Processa o arquivo e obtém a lista de músicas mais tocadas
musicas_mais_tocadas = processar_arquivo(nome_arquivo)

# Imprime a lista resultante
print(musicas_mais_tocadas)
