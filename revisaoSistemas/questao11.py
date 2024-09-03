import random


def questao11():
    def jogar_dados():
        return random.randint(1, 6) + random.randint(1, 6)
    
    primeira_jogada = jogar_dados()
    if primeira_jogada in [7, 11]:
        print( "Você tirou um 'natural' e ganhou!")
    elif primeira_jogada in [2, 3, 12]:
        print( "Craps! Você perdeu.")
    else:
        ponto = primeira_jogada
        while True:
            jogada = jogar_dados()
            if jogada == ponto:
                print( f"Você tirou seu ponto ({ponto}) e ganhou!")
                break
            elif jogada == 7:
                print( "Você tirou 7 e perdeu!")
                break
