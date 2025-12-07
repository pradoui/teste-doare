# Teste Navega. - Dashboard de doações
Desenvolvido por: Thiago Prado

## Objetivo: Desenvolver uma automação que processe um banco Excel, organizando suas referências e gerando um banco de dados sql, conectando através de uma API com um Dashboard.

## Arquitetura

O projeto foi desenvolvido utilizando uma arquitetura de microsserviços orientada a dados:

1.  **ETL (Extração e Tratamento):** Python + Pandas para limpar o Excel e normalizar dados.
2.  **Database:** PostgreSQL (Hospedado no Supabase) com Connection Pooling para alta performance.
3.  **Backend API:** FastAPI (Hospedado no Render) servindo dados tratados em JSON.
4.  **Frontend/BI:** Power BI consumindo a API em tempo real.

## 🛠 Tecnologias

* **Linguagem:** Python 3.10+
* **Libs:** Pandas, SQLAlchemy, FastAPI, Uvicorn.
* **Infra:** Supabase (PostgreSQL), Render (Cloud PaaS).
* **Visualização:** Power BI.

## 🔒 Segurança

* Credenciais de banco de dados protegidas via Variáveis de Ambiente (.env).
* Conexão via Transaction Pooler (Porta 6543) para otimização de recursos.

## 📊 Como rodar localmente

1.  Clone o repositório.
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Configure o `.env` com as credenciais do banco.
4.  Execute: `uvicorn api:app --reload`
