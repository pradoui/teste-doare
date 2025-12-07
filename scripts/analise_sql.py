import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

try:
    db_password = os.getenv("DATABASE_PASSWORD")
    if not db_password:
        raise ValueError("Senha não encontrada no .env")

    p_password = urllib.parse.quote_plus(db_password)
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    db_name = os.getenv("DB_NAME")
    user = os.getenv("USER")

    db_string = f"postgresql://{user}:{p_password}@{host}:{port}/{db_name}"
    engine = create_engine(db_string)

    query_sql = """
    SELECT 
        b.email,
        b.primeiro_nome_tratado AS primeiro_nome,
        b.data_de_registro,
        b.status,
        t."Descrição" AS tipo_doacao,
        b.canal_tratado AS canal,
        d.valor_bruto AS valor
    FROM tabela_base b
    LEFT JOIN tabela_dados_doacao d ON b.email = d.email
    LEFT JOIN tabela_tipo t ON d."CD_Tipo" = t."CD_Tipo"
    """

    df_final = pd.read_sql(query_sql, engine)
    
    print("Query executada com sucesso!")
    print(df_final.head())

    print("\n--- Totais para Conferência ---")
    print(f"Valor Total: R$ {df_final['valor'].sum():,.2f}")
    print(f"Total de Doadores Únicos: {df_final['email'].nunique()}")

except Exception as e:
    print(f"Erro na execução da query: {e}")