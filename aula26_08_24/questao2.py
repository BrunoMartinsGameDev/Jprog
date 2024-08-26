import math


# Função para calcular as quantidades e preços
def questao2(area):
    # Dados fornecidos
    litros_por_metro_quadrado = 1 / 6  # 1 litro para cada 6 metros quadrados
    litros_lata = 18  # Capacidade da lata
    preco_lata = 80.00  # Preço da lata
    litros_galao = 3.6  # Capacidade do galão
    preco_galao = 25.00  # Preço do galão
    folga = 1.10  # 10% de folga

    # Acrescentando 10% de folga
    area_com_folga = area * folga
    
    # Quantidade total de tinta necessária em litros
    litros_necessarios = area_com_folga * litros_por_metro_quadrado
    
    # Situação 1: Apenas latas de 18 litros
    latas_necessarias = math.ceil(litros_necessarios / litros_lata)
    preco_latas = latas_necessarias * preco_lata
    
    # Situação 2: Apenas galões de 3,6 litros
    galoes_necessarios = math.ceil(litros_necessarios / litros_galao)
    preco_galoes = galoes_necessarios * preco_galao
    
    # Situação 3: Misturar latas e galões (para minimizar desperdício)
    latas_misturadas = litros_necessarios // litros_lata  # Latões inteiros
    resto = litros_necessarios % litros_lata  # Restante em litros
    galoes_misturados = math.ceil(resto / litros_galao)  # Galões para o resto
    preco_misto = (latas_misturadas * preco_lata) + (galoes_misturados * preco_galao)
    
    print(f"Quantidade de tinta necessária: {litros_necessarios:.2f} litros")
    print(f"Quantidade de latas necessária: {latas_necessarias}")
    print(f"Quantidade de galões necessária: {galoes_necessarios}")
    print(f"Preço das latas: R$ {preco_latas:.2f}")
    print(f"Preço dos galões: R$ {preco_galoes:.2f}")
    print(f"Preço da mistura: R$ {preco_misto:.2f}")
