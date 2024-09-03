from questao1 import questao1
from questao2 import questao2
from questao3 import questao3
from questao4 import questao4
from questao5 import questao5
from questao6 import questao6
from questao7 import questao7
from questao8 import questao8
from questao9 import questao9
from questao10 import questao10
from questao11 import questao11
from questao12 import questao12 


while True:
    questao = input("Digite o numero da questão que deseja revisar(1 a 12): ")
    if(questao == '0'): 
        print("Revisão encerrada")
        break
    if(questao.isdigit()):
        if(int(questao) >= 1 and int(questao) <= 12):
            match int(questao):
                case 1: questao1(65) # questao1(Peso)
                case 2: questao2(100) # questao2(Area)
                case 3: questao3(10, 400) # questao3(Valor_Hora, Horas_Trabalhadas)
                case 4: questao4(2, 1, 16) # questao4(a, b, c)
                case 5: questao5() 
                case 6: questao6( 80000, 0.03, 200000, 0.40) # questao6(populacao_A, taxa_A, populacao_B, taxa_B)
                case 7: questao7(100) # questao7(n)
                case 8: questao8([20, 30, 40, 15, 25, 35, 10, 50, 60, 0, 0, 0]) # questao8(temperaturas)
                case 9: questao9()
                case 10: questao10( int(input("Digite um numero: "))) # questao10(numero)
                case 11: questao11()
                case 12: questao12()
            continue
        else:
            print("Questão invalida")
            input()
            continue
    else:
        print("Questão invalida")
        input()
        continue