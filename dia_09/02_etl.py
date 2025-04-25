# %% 
import pandas as pd
import sqlalchemy  # Importa as bibliotecas necessárias para manipulação de dados e conexão com o banco de dados

# %%

# Abre e lê o conteúdo do arquivo SQL que contém a consulta
with open('query.sql') as open_file:
    query = open_file.read()

# Exibe a consulta SQL no console para conferência
print(query)

# %% 

# Cria a engine de conexão com o banco de dados PostgreSQL (neste caso, com o banco "northwind")
engine = sqlalchemy.create_engine("postgresql+psycopg://postgres:postgres@localhost/northwind")

# %%

# Executa a consulta SQL lida anteriormente e armazena o resultado em um DataFrame
orders_city = pd.read_sql_query(query, con=engine)
orders_city  # Exibe o DataFrame com os resultados

# %%

# Exporta os dados do DataFrame para uma tabela no banco chamada "total_vendas_cidade"
# index=False garante que o índice do DataFrame não seja incluído como uma coluna na tabela
orders_city.to_sql("total_vendas_cidade", con=engine, index=False)
