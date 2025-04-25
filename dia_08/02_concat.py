# %%
#Importando Pandas.
import pandas as pd 
# %%
#Criando dataframes de exemplo.
df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "capu", "coutinho", "maria", "leticia"]
})

df_02 = pd.DataFrame({
    "cliente":[6,7,8],
    "nome": ["kokinho", "elisa", "jardim"],
    "idade": [32,29,31]
})

df_02
#%%

df_03 = pd.DataFrame({
    "idade": [32,29,32,31,32]
})

df_03
# %%

df_full = pd.concat([df,df_02],ignore_index=True)

df_full
# %%
# Por padrão, o pd.concat junta os DataFrames **um embaixo do outro**, ou seja, ele empilha as linhas.
# Isso é o equivalente a adicionar mais registros (linhas) no final da tabela.
pd.concat([df,df_03])
#%% 
# Se quisermos **juntar lado a lado**, ou seja, colocar os DataFrames **como novas colunas**,
# precisamos informar que queremos juntar pelo eixo das colunas (axis=1).
pd.concat([df,df_03], axis=1)