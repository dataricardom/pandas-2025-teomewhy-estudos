# %%
import pandas as pd

# descrição: Lê o arquivo CSV separado por ponto e vírgula (;), que contém os dados de transações com cartão.
df = pd.read_csv("dados_cartao.csv", sep=";")
df

# %%
# descrição: Converte a coluna "dtTransacao" de texto para o tipo datetime, para facilitar o cálculo de datas futuras.
df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df

# %%
# descrição: Cria uma nova coluna "vlParcela", que representa o valor de cada parcela dividindo o valor da venda pela quantidade de parcelas.
df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]
df

# %%
# descrição: Cria uma nova coluna chamada "ordemParcela" que contém uma lista com a ordem de cada parcela.
# Por exemplo, se uma venda tem 4 parcelas, a lista será [0, 1, 2, 3].
# Essa lista representa o número de meses a adicionar à data da transação para calcular a data de cada parcela futura.
df["ordemParcela"] = df.apply(
    lambda row: [i for i in range(row['qtParcelas'])],  # Gera a lista de parcelas com base na quantidade
    axis=1  # Aplica a função linha por linha
)
df

# %%
# descrição: "Explode" a lista da coluna "ordemParcela", duplicando as linhas para que cada parcela tenha uma linha separada.
df_explode = df.explode("ordemParcela")
df_explode

# %%
# descrição: Cria uma nova coluna "dtParcela", que calcula a data da parcela somando meses à data da transação com base na ordem da parcela.
def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt =  f"{dt.year}-{dt.month}"  # Formata a data para "AAAA-MM" (ano e mês).
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode

# %%
# descrição: Agrupa os dados por cliente e mês da parcela, somando os valores das parcelas para cada combinação.
# Em seguida, transforma o resultado em uma tabela onde cada coluna representa um mês (pivot_table),
# preenchendo com 0 onde não houver parcelas.
(df_explode.groupby(["idCliente", "dtParcela"])
           ['vlParcela'].sum()
           .reset_index()
           .pivot_table(index='idCliente',
                        columns='dtParcela',
                        values='vlParcela',
                        fill_value=0))
