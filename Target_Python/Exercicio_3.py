import json

faturamento_mensal = '''
[
    {"dia": 1, "faturamento": 22174.1664},
    {"dia": 2, "faturamento": 24537.6698},
    {"dia": 3, "faturamento": 26139.6134},
    {"dia": 4, "faturamento": 0.0},
    {"dia": 5, "faturamento": 0.0},
    {"dia": 6, "faturamento": 26742.6612},
    {"dia": 7, "faturamento": 0.0},
    {"dia": 8, "faturamento": 42889.2258},
    {"dia": 9, "faturamento": 46251.174},
    {"dia": 10, "faturamento": 11191.4722},
    {"dia": 11, "faturamento": 0.0},
    {"dia": 12, "faturamento": 0.0},
    {"dia": 13, "faturamento": 3847.4823},
    {"dia": 14, "faturamento": 373.7838},
    {"dia": 15, "faturamento": 2659.7563},
    {"dia": 16, "faturamento": 48924.2448},
    {"dia": 17, "faturamento": 18419.2614},
    {"dia": 18, "faturamento": 0.0},
    {"dia": 19, "faturamento": 0.0},
    {"dia": 20, "faturamento": 35240.1826},
    {"dia": 21, "faturamento": 43829.1667},
    {"dia": 22, "faturamento": 18235.6852},
    {"dia": 23, "faturamento": 4355.0662},
    {"dia": 24, "faturamento": 13327.1025},
    {"dia": 25, "faturamento": 0.0},
    {"dia": 26, "faturamento": 0.0},
    {"dia": 27, "faturamento": 25681.8318},
    {"dia": 28, "faturamento": 1718.1221},
    {"dia": 29, "faturamento": 13220.495},
    {"dia": 30, "faturamento": 8414.61}
]
'''


dados = json.loads(faturamento_mensal)

faturamentos_validos = [dia["faturamento"] for dia in dados if dia["faturamento"] > 0]


menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)
media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)


dias_acima_da_media = sum(1 for dia in faturamentos_validos if dia > media_mensal)

resultados = {
    "menor_faturamento": menor_faturamento,
    "maior_faturamento": maior_faturamento,
    "media_mensal": media_mensal,
    "dias_acima_da_media": dias_acima_da_media
}

resultados