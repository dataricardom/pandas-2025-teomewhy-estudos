# %%

import pandas as pd
import sqlalchemy
# %%
# Conexão com banco de dados Postgres.

engine_2 = sqlalchemy.create_engine("postgresql+psycopg://postgres:postgres@localhost/northwind")

# %%

tb_customers_2 = pd.read_sql_table("categories",con=engine_2)

# %% 

tb_customers_2
# %%
#Conexão com Sqlite
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%
# Evite usar pd.read_sql_table para carregar a tabela inteira, pois:
# - Pode consumir muita memória se a tabela for grande
# - Pode sobrecarregar a conexão com o banco
# - Pode afetar o desempenho de outras operações no banco
tb_customers = pd.read_sql_table("tb_customers",con=engine)

# %%
tb_customers


# %%
# A melhor prática é usar pd.read_sql_query com filtros (WHERE, LIMIT, etc.)

query = 'SELECT * FROM tb_customers LIMIT 100'


df_100 = pd.read_sql_query(query, con=engine)

df_100