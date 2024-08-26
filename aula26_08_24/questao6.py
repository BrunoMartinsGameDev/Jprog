def questao6(populacao_A, taxa_A, populacao_B, taxa_B):
    anos = 0
    while populacao_A < populacao_B:
        populacao_A += populacao_A * (taxa_A / 100)
        populacao_B += populacao_B * (taxa_B / 100)
        anos += 1
    print("Anos:", anos) 
