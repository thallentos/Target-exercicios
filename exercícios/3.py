import json

# Dados de faturamento diário, simulando o conteúdo de um arquivo JSON
faturamento_mensal = {
    "faturamento_diario": [
        1200.50, 800.0, 0, 0, 1500.75, 1100.80, 0, 0,
        1320.60, 900.0, 0, 0, 1450.50, 1250.60, 0, 0,
        1380.40, 950.20, 0, 0, 1480.70, 1230.10, 0, 0,
        1400.0, 970.90, 0, 0, 1500.30, 1270.40, 0, 0
    ]
}

# Filtra os valores diferentes de 0
faturamento = [valor for valor in faturamento_mensal["faturamento_diario"] if valor > 0]

# Calcula o menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcula a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Conta o número de dias com faturamento superior à média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibe os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")
