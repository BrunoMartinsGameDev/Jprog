from itertools import permutations

def questao12():
    def is_magico(quadrado):
        soma_linhas = [sum(quadrado[i:i+3]) for i in range(0, 9, 3)]
        soma_colunas = [sum(quadrado[i::3]) for i in range(3)]
        soma_diagonais = [quadrado[0] + quadrado[4] + quadrado[8], quadrado[2] + quadrado[4] + quadrado[6]]
        return len(set(soma_linhas + soma_colunas + soma_diagonais)) == 1

    quadrados_magicos = []
    for p in permutations(range(1, 10)):
        if is_magico(p):
            quadrados_magicos.append(p)
    print(f"Quadrados magicos: {quadrados_magicos}")
