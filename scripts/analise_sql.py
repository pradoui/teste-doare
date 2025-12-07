import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///doare.db')

query_sql = """
SELECT 
    b.email,
    b.primeiro_nome_tratado AS primeiro_nome,
    b.data_de_registro,
    b.data_de_pagamento,
    b.status,
    t.Descrição AS tipo_doacao_descricao,
    b.forma_de_pagamento,
    b.canal_tratado AS canal_origem,
    d.valor_bruto AS valor
FROM tabela_base b
LEFT JOIN tabela_dados_doacao d 
    ON b.email = d.email
LEFT JOIN tabela_tipo t 
    ON d.CD_Tipo = t.CD_Tipo
LEFT JOIN tabela_canal c 
    ON b.canal_tratado = c.Canal
"""

try:
    df_final = pd.read_sql(query_sql, engine)
    
    print("Cruzamento de dados realizado com sucesso!")

    total_valor = df_final['valor'].sum()
    print(f"\nValor Total Soma: R$ {total_valor:,.2f}")

except Exception as e:
    print(f"Erro ao executar a consulta SQL: {e}")