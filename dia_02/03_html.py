# %% 
import pandas as pd
# %%
#Pega todas as tabelas do endereço.
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url)
dfs


# %%
#Descobrindo quantas dfs(tabelas) tem.

len(dfs)
# %%

#Buscando para saber qual tabela.
dfs[1]

#%% 

#Salvando em csv.
dfs_uf = dfs[1]
dfs_uf.to_csv("ufs.csv",
              index=False, 
              sep = ';')


