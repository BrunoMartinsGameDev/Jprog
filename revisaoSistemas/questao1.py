def questao1(peso):
    # Definindo os limites e o valor da multa por quilo excedente
    limite_peso = 50  # Limite de peso em quilos
    valor_multa_por_quilo = 4.00  # Valor da multa por quilo excedente

    # Função para calcular o excesso de peso e a multa

    if peso > limite_peso:
        excesso = peso - limite_peso
        multa = excesso * valor_multa_por_quilo
    else:
        excesso = 0
        multa = 0
    print(f"Excesso de peso: {excesso} kg")
    print(f"Multa: R$ {multa:.2f}")