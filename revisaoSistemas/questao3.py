# Função para calcular a folha de pagamento
def questao3(valor_hora, horas_trabalhadas):
    # Cálculo do salário bruto
    salario_bruto = valor_hora * horas_trabalhadas

    # Definindo as alíquotas
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = 0.05
    elif salario_bruto <= 2500:
        desconto_ir = 0.10
    else:
        desconto_ir = 0.20
    
    desconto_inss = 0.10
    fgts = 0.11
    sindicato = 0.03
    
    # Cálculo dos descontos
    valor_ir = salario_bruto * desconto_ir
    valor_inss = salario_bruto * desconto_inss
    valor_fgts = salario_bruto * fgts
    valor_sindicato = salario_bruto * sindicato
    
    # Total de descontos
    total_descontos = valor_ir + valor_inss + valor_sindicato
    
    # Cálculo do salário líquido
    salario_liquido = salario_bruto - total_descontos
    
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"IR: R$ {valor_ir:.2f}")
    print(f"INSS: R$ {valor_inss:.2f}")
    print(f"Sindicato: R$ {valor_sindicato:.2f}")
    print(f"FGTS: R$ {valor_fgts:.2f}")
    print(f"Total de descontos: R$ {total_descontos:.2f}")
    print(f"Salário liquido: R$ {salario_liquido:.2f}")


