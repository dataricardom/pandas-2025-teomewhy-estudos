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