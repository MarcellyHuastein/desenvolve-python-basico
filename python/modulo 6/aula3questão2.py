def extrair_dominio(url):
    # Remove o prefixo "www." e o sufixo ".com"
    return url[4:-4]

def main():
    # Lista de URLs fornecida
    urls = [
        "www.google.com",
        "www.gmail.com",
        "www.github.com",
        "www.reddit.com",
        "www.yahoo.com"
    ]
    
    # Usar fatiamento para criar a lista de domínios
    dominios = [extrair_dominio(url) for url in urls]
    
    # Imprimir a lista de domínios
    print("Domínios:", dominios)

# Executa o programa principal
if __name__ == "__main__":
    main()
