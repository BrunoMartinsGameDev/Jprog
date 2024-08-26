def questao8(temperaturas):
    media_anual = sum(temperaturas) / len(temperaturas)
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    temperaturas_acima_media = []
    for i, temp in enumerate(temperaturas):
        if temp > media_anual:
            temperaturas_acima_media.append((meses[i], temp))
    print(f"Média anual: {media_anual:.2f}")
    print(f"Temperaturas acima da média anual: {temperaturas_acima_media}")