import matplotlib.pyplot as plt

# Criando o gráfico de barras
analise_dias['valor_liquido'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Lucro Líquido por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('R$ Líquido')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Lendo os dados para o Pandas
df = pd.read_sql_query("SELECT * FROM servicos", conn)

# Definindo as taxas (ajuste conforme a barbearia usa)
taxas = {'Crédito': 0.0499, 'Débito': 0.02, 'Pix': 0.0}

# Criando a coluna de valor líquido
df['taxa_aplicada'] = df['tipo_pagamento'].map(taxas)
df['valor_liquido'] = df['valor'] * (1 - df['taxa_aplicada'])

# Agrupando por dia da semana
analise_dias = df.groupby('dia_semana').agg({
    'id': 'count',           # Quantidade de cortes
    'valor': 'sum',         # Faturamento Bruto
    'valor_liquido': 'sum'  # Faturamento Líquido
}).rename(columns={'id': 'qtd_cortes'})

# Ordenando os dias para o gráfico não ficar bagunçado
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
analise_dias = analise_dias.reindex(ordem_dias)

print(analise_dias)

import matplotlib.pyplot as plt

# Criando o gráfico de barras
analise_dias['valor_liquido'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Lucro Líquido por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('R$ Líquido')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()