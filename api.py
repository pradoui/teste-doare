from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine
import uvicorn
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

app = FastAPI(title="API Doare", description="API para dashboard de dados das doações")

db_password = os.getenv("DATABASE_PASSWORD")
if not db_password:
    raise ValueError("DATABASE_PASSWORD não foi encontrado nas variáveis de ambiente.")

p_password = urllib.parse.quote_plus(db_password)
host = os.getenv("HOST")
port = os.getenv("PORT")
db_name = os.getenv("DB_NAME")
user = os.getenv("USER")

db_string = f"postgresql://{user}:{p_password}@{host}:{port}/{db_name}"
engine = create_engine(db_string)

@app.get("/dados")
def get_dados_doare():
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

    try:
        df = pd.read_sql(query_sql, engine)
        df = df.fillna("")

        json = df.to_dict(orient='records')
        return json
    except Exception as e:
        return {"erro": f"Erro ao executar a consulta SQL: {e}"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)