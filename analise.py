import sqlite3
import pandas as pd
import os

# --- CONFIGURAÇÕES DE TAXAS (Mude aqui quando souber os valores reais) ---
TAXA_DEBITO = 0.02   # Exemplo: 2%
TAXA_CREDITO = 0.04  # Exemplo: 4%
TAXA_QR_CODE = 0.00  # Geralmente 0%

# Localização do banco
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio, 'barbearia_oficial.db')

try:
    conexao = sqlite3.connect(caminho_banco)
    
    # SQL Inteligente: Já traz os dados e calcula o líquido de cada linha
    query = f"""
    SELECT 
        Data_Dia, 
        Total_Vendas,
        (Vendas_Debito * {1 - TAXA_DEBITO}) + 
        (Vendas_Credito * {1 - TAXA_CREDITO}) + 
        (Codigo_QR * {1 - TAXA_QR_CODE}) AS Valor_Liquido
    FROM Fechamento_Barbearia;
    """
    
    df = pd.read_sql_query(query, conexao)

    if not df.empty:
        # --- CÁLCULOS EXTRAS PARA O RELATÓRIO ---
        total_bruto = df['Total_Vendas'].sum()
        total_liquido = df['Valor_Liquido'].sum()
        media_diaria = df['Total_Vendas'].mean()

        print("\n" + "="*40)
        print("      RELATÓRIO DE VENDAS - BARBEARIA")
        print("="*40)
        print(df.to_string(index=False)) # Mostra a tabela sem o índice chato
        print("-"*40)
        print(f"Faturamento Bruto Total:  R$ {total_bruto:>8.2f}")
        print(f"Faturamento Líquido Total: R$ {total_liquido:>8.2f}")
        print(f"Média de Vendas por Dia:   R$ {media_diaria:>8.2f}")
        print("="*40)
    else:
        print("O banco de dados está vazio.")

except Exception as e:
    print(f"❌ Erro ao gerar relatório: {e}")

finally:
    if 'conexao' in locals():
        conexao.close()