# 💈 BarberStats - Sistema de Fechamento de Caixa

Este é um projeto desenvolvido em **Python** e **SQL** para automatizar o fechamento financeiro de uma barbearia. O objetivo é transformar os dados brutos de vendas (Cartão, QR Code) em um relatório detalhado de faturamento líquido.

## 🚀 Funcionalidades

- **Cálculo Automático de Taxas:** Processa descontos diferenciados para crédito, débito e Pix/QR Code.
- **Integração SQL:** Persistência de dados segura utilizando SQLite3.
- **Relatório de Performance:** Exibe faturamento bruto, líquido e média de vendas diária através da biblioteca Pandas.

## 🛠️ Tecnologias Utilizadas

* **Python 3.13**
* **SQLite3** (Banco de dados)
* **Pandas** (Análise e processamento de dados)
* **DB Browser for SQLite** (Interface para gestão do banco)

## 📊 Exemplo de Relatório

Ao executar o `analise.py`, o sistema gera o seguinte output no terminal:

========================================
      RELATÓRIO DE VENDAS - BARBEARIA
========================================
  Data_Dia  Total_Vendas  Valor_Liquido
2023-10-27        1801.0        1750.62
----------------------------------------
Faturamento Bruto Total:  R$  1801.00
Faturamento Líquido Total: R$  1750.62
Média de Vendas por Dia:   R$  1801.00
========================================

## ⚙️ Como executar

1. Clone o repositório.
2. Certifique-se de que o arquivo `barbearia_oficial.db` está na mesma pasta que o `analise.py`.
3. Instale o Pandas se ainda não tiver: `pip install pandas`.
4. Execute: `python analise.py`.

---
Desenvolvido por [Seu Nome] - Estudo de integração Python + SQL.