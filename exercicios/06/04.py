# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()
# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv")
transacao_produto.head()

# %%
produto = pd.read_csv("../../data/produtos.csv")
produto.head()
# %%
#

transacoes_transacoes_produto = transacoes.merge(
    right=transacao_produto,
    how='left',
    on=['idTransacao'],
    suffixes=['Transacoes', 'Transacao_Prod'])
transacoes_transacoes_produto.head()
#%%

df_full = transacoes_transacoes_produto.merge(
    produto,
    how='left',
    on=['idProduto'])
df_full.head()

# %%
#Criando filtro após joins das tabelas.

df_full = df_full[df_full['descProduto']== 'Presença Streak']

df_full.head()
# %%
# Agrupando por id cliente e usando agg para agregação.
# Devido ao agg criar uma coluna multindex, no sorte values tem que especificar corretamente.
(df_full.groupby(
    by=['idCliente'])
    .agg({'qtdeProduto': ['count']})
    .sort_values(('qtdeProduto', 'count'),ascending=False)
    )

# %%
# Mesmo procedimento sem agg.

(df_full.groupby(
    by=['idCliente'])['qtdeProduto']
    .count()
    .sort_values(ascending=False)
)
# %%

# Obteando a resposta da questão que é apenas quem comprou a maior quantidade de streak:


(df_full.groupby(
    by=['idCliente'])['qtdeProduto']
    .count()
    .sort_values(ascending=False)
).head(1)

# Resultado: O cliente de id: 6313ceac-7806-4d34-aedd-476eed7c853a com : 76 compras.

# %%

# Uma forma mais performatica, já que o objetivo é saber a quantidade somente de Presença Streak.
# É antes de fazer o join em produtos, ja realizar o filtro do produto desejado.
# E apos isso fazer o join com as tabelas anteriores com right join em produto.
# O que vai retornar somente as transações que correspondem a Presensa Streak
produto = produto[produto['descProduto'] == "Presença Streak"]
produto
# %%
#Exemplo.
(transacoes
        .merge(transacao_produto,on=['idTransacao'],how='left')
        .merge(produto, on=['idProduto'], how='right')
        .groupby(by=['idCliente'])['idTransacao']
        .count()
        .sort_values(ascending=False)
        .head(1)
        )