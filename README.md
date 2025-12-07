# Teste Navega. - Dashboard de doações
Desenvolvido por: Thiago Prado

## Objetivo: Desenvolver uma automação que processe um banco Excel, organizando suas referências e gerando um banco de dados sql, conectando através de uma API com um Dashboard.

## Arquitetura

O projeto foi desenvolvido utilizando uma arquitetura de microsserviços orientada a dados:

1.  **ETL (Extração e Tratamento):** Python + Pandas para limpar o Excel e normalizar dados.
2.  **Database:** PostgreSQL (Hospedado no Supabase) com Connection Pooling para alta performance.
3.  **Backend API:** FastAPI (Hospedado no Render) servindo dados tratados em JSON.
4.  **Frontend/BI:** Power BI consumindo a API em tempo real.

## Tecnologias

* **Linguagem:** Python 3.10+
* **Libs:** Pandas, SQLAlchemy, FastAPI, Uvicorn.
* **Infra:** Supabase (PostgreSQL), Render (Cloud PaaS).
* **Visualização:** Power BI.

## Segurança

* Credenciais de banco de dados protegidas via Variáveis de Ambiente (.env).
* Conexão via Transaction Pooler (Porta 6543) para otimização de recursos.

## Como rodar localmente

1.  Clone o repositório.
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Configure o `.env` com as credenciais do banco.
4.  Execute: `uvicorn api:app --reload`

## Prints

1. Banco salvo no Supabase
<img width="821" height="727" alt="image" src="https://github.com/user-attachments/assets/ae2ae32b-a3b6-4a57-ab9a-2af86c4fb135" />

2. Dados JSON retornados da API
<img width="1117" height="519" alt="image" src="https://github.com/user-attachments/assets/5a012376-b77c-4062-8b75-c3d849dac29f" />
<img width="1905" height="1008" alt="image" src="https://github.com/user-attachments/assets/95d499df-c036-47d4-93c1-861dce77fe9a" />

3. Dashboard Power BI
<img width="1349" height="782" alt="image" src="https://github.com/user-attachments/assets/94a81d09-5805-4e70-81f4-f645f3bf6826" />
<img width="1309" height="445" alt="image" src="https://github.com/user-attachments/assets/2afb18d0-81e2-41de-992d-8ec63d3c5f41" />
