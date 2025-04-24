# %% 
import pandas as pd
import numpy as np
# %%
transacoes = pd.read_csv("../data/transacoes.csv")

transacoes.head()
# %%
#Criando funções personalisadas de agregação:

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) **2)
# %%

idades = pd.Series([21,23,24,28,35,45,68,72,85,90,60,25,29])

idades

# %%

diff_amp(idades)

# %%
#Refazendo agregações com agg e utilisando a função criada.
summary_2 =(transacoes.groupby(by=["idCliente"], as_index=False)
 .agg({"idTransacao": ["count"],
                 "qtdePontos": ["sum", "mean", diff_amp]}))
# %%
summary_2.columns
# %% 
# Definindo colunas

summary_2.columns = ['idCliente', 'qtdeTransacao', 'totalPontos', 'avgPontos','diff_amp']
summary_2


# %%
# Essa função life_time calcula o tempo de vida (em dias) de um conjunto de datas, ou seja
# a diferença entre a data mais recente e a mais antiga dentro de uma Series do pandas.
def life_time(tempo: pd.Series):
    dt = pd.to_datetime(tempo)
    return (dt.max() - dt.min()).days
# Após isso pode ser usada no agg.

# %%

summary_3 = (transacoes.groupby(by=["idCliente"], as_index=False)
 .agg({"idTransacao": ["count"],
                 "qtdePontos": ["sum", "mean", diff_amp]
                 ,"dtCriacao": [life_time]}))

summary_3.columns = ["idCliente", "qtdeTransacao","totalPontos","avgPontos","diff_amp","life_time"]

# %%

summary_3