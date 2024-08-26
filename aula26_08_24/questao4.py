import math

def questao4(a, b, c):
    if a == 0:
        print( "A equação não é do segundo grau.")
    
    delta = b ** 2 - 4 * a * c
    
    if delta < 0:
        print( "A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print( f"A equação possui uma única raiz: {raiz}.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print( f"A equação possui duas raízes reais: {raiz1} e {raiz2}.")
