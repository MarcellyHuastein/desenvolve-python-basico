# Dados iniciais
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Construção da lista aprovados usando compreensão de listas
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

# Impressão do resultado
print(aprovados)
