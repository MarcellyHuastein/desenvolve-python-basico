import csv

def criar_csv_livros(nome_arquivo):
    # Lista de livros com suas informações
    livros = [
        ["O Hobbit", "J.R.R. Tolkien", "1937", "310"],
        ["1984", "George Orwell", "1949", "328"],
        ["O Senhor dos Anéis", "J.R.R. Tolkien", "1954", "1178"],
        ["Orgulho e Preconceito", "Jane Austen", "1813", "279"],
        ["Dom Quixote", "Miguel de Cervantes", "1605", "1023"],
        ["A Revolução dos Bichos", "George Orwell", "1945", "112"],
        ["Moby Dick", "Herman Melville", "1851", "635"],
        ["A Menina que Roubava Livros", "Markus Zusak", "2005", "552"],
        ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", "1997", "223"],
        ["Cem Anos de Solidão", "Gabriel García Márquez", "1967", "417"]
    ]
    
    # Abre o arquivo CSV para escrita
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        
        # Escreve o cabeçalho
        writer.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
        
        # Escreve as informações dos livros
        writer.writerows(livros)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"
criar_csv_livros(nome_arquivo)
