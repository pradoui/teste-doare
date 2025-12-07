import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

load_dotenv()

db_password = os.getenv("DATABASE_PASSWORD")
p_password = urllib.parse.quote_plus(db_password)
host = os.getenv("HOST")
port = os.getenv("PORT")
db_name = os.getenv("DB_NAME")
user = os.getenv("USER")

db_string = f"postgresql://{user}:{p_password}@{host}:{port}/{db_name}"
engine = create_engine(db_string)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, '..', 'data', 'doare_excel.xlsx')

try:
    df_base = pd.read_excel(caminho_arquivo, sheet_name='Base')
    df_dados = pd.read_excel(caminho_arquivo, sheet_name='Dados doação')
    df_tipo = pd.read_excel(caminho_arquivo, sheet_name='Tipo de doação')
    df_canal = pd.read_excel(caminho_arquivo, sheet_name='Canal')
    print("Excel lido com sucesso!")
except Exception as e:
    print(f"Erro ao ler Excel: {e}")
    exit()

if 'nome' in df_base.columns:
    df_base['primeiro_nome_tratado'] = df_base['nome'].astype(str).str.split(' ').str[0]
    print("Nomes tratados.")

if 'utm_source' in df_base.columns:
    df_base['utm_source'] = df_base['utm_source'].fillna('Desconhecido') 
    df_base['canal_tratado'] = df_base['utm_source'].astype(str).str.split('_').str[0]
    print("Canais tratados.")

print("--- Salvando no Supabase ---")

df_base.to_sql('tabela_base', con=engine, index=False, if_exists='replace')
df_dados.to_sql('tabela_dados_doacao', con=engine, index=False, if_exists='replace')
df_tipo.to_sql('tabela_tipo', con=engine, index=False, if_exists='replace')
df_canal.to_sql('tabela_canal', con=engine, index=False, if_exists='replace')

print("Sucesso! Dados importados para o Supabase.")