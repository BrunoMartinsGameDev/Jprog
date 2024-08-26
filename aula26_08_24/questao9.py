import random

def questao9():
    resultados = [0] * 6
    for _ in range(100):
        dado = random.randint(1, 6)
        resultados[dado - 1] += 1
    print(f'Resultados: {resultados}')
