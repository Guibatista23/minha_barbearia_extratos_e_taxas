import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# --- PASSO 1: CRIAR O BANCO E OS DADOS ---
conn = sqlite3.connect('barbearia_analise.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS servicos')
cursor.execute('''
CREATE TABLE servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    valor REAL,
    tipo_pagamento TEXT,
    data TEXT,
    dia_semana TEXT
)
''')

# Simulando a realidade que você me passou:
# Terça com 4 cortes, Sábado bombando, outros equilibrados.
dados = [
    # SEGUNDA
    ('Cli Seg', 50.0, 'Pix', '2026-02-16', 'Segunda'),
    ('Cli Seg', 50.0, 'Débito', '2026-02-16', 'Segunda'),
    ('Cli Seg', 50.0, 'Pix', '2026-02-16', 'Segunda'),
    ('Cli Seg', 50.0, 'Crédito', '2026-02-16', 'Segunda'),
    ('Cli Seg', 50.0, 'Pix', '2026-02-16', 'Segunda'),
    ('Cli Seg', 50.0, 'Pix', '2026-02-16', 'Segunda'),
    
    # TERÇA (Fraco: 4 cortes conforme você relatou)
    ('Cli Ter', 50.0, 'Crédito', '2026-02-17', 'Terça'),
    ('Cli Ter', 50.0, 'Débito', '2026-02-17', 'Terça'),
    ('Cli Ter', 50.0, 'Crédito', '2026-02-17', 'Terça'),
    ('Cli Ter', 50.0, 'Pix', '2026-02-17', 'Terça'),

    # QUARTA/QUINTA/SEXTA (Média de 7 cortes)
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),
    ('Cli Qua', 50.0, 'Pix', '2026-02-18', 'Quarta'),

    # SÁBADO (Melhor dia: 15 cortes)
    ('Cli Sab', 60.0, 'Crédito', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Crédito', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Débito', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
    ('Cli Sab', 60.0, 'Pix', '2026-02-21', 'Sábado'),
]

cursor.executemany('INSERT INTO servicos (cliente, valor, tipo_pagamento, data, dia_semana) VALUES (?,?,?,?,?)', dados)
conn.commit()

# --- PASSO 2: ANÁLISE COM PANDAS ---
df = pd.read_sql_query("SELECT * FROM servicos", conn)

# Taxas
taxas = {'Crédito': 0.0499, 'Débito': 0.02, 'Pix': 0.0}
df['taxa_aplicada'] = df['tipo_pagamento'].map(taxas)
df['valor_liquido'] = df['valor'] * (1 - df['taxa_aplicada'])

# Agrupamento
analise_dias = df.groupby('dia_semana').agg({
    'id': 'count',
    'valor': 'sum',
    'valor_liquido': 'sum'
}).rename(columns={'id': 'qtd_cortes'})

# Ordenação para o gráfico ficar certo
ordem_dias = ["Segunda", "Terça", "Quarta", "Sexta", "Sábado"] # Adicionei os dias que alimentamos
analise_dias = analise_dias.reindex(ordem_dias)

print("Tabela de Análise:")
print(analise_dias)

# --- PASSO 3: GRÁFICO ---
plt.figure(figsize=(10,6))
analise_dias['valor_liquido'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Lucro Líquido por Dia da Semana (Foco em Ociosidade)')
plt.xlabel('Dia da Semana')
plt.ylabel('R$ Líquido')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salva o gráfico como imagem para você usar no LinkedIn depois
plt.savefig('grafico_barbearia.png')
plt.show()

conn.close()