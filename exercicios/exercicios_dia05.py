#%%
import pandas as pd

# %%

clientes = pd.read_csv("..//data/clientes.csv")
clientes
# %%
#Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
clientes["twitch_points"] = clientes["qtdePontos"] * clientes["flTwitch"]
clientes.head(5)

# %%
# Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
clientes["vinculo_social"] = clientes["flEmail"] | clientes["flTwitch"] | clientes["flYouTube"] | clientes["flBlueSky"] | clientes["flInstagram"]
clientes.head(5)

#%%


#Qual é o id de cliente que tem maior saldo de pontos? E o menor?

cliente_mais_pontos = clientes.loc[clientes["qtdePontos"].idxmax()]
cliente_mais_pontos
# %%
cliente_menos_pontos = clientes.loc[clientes["qtdePontos"].idxmin()]
cliente_menos_pontos


#%%
clientes.sort_values(by= "qtdePontos", ascending=False).head(1)["idCliente"]
# %%
clientes.sort_values(by= "qtdePontos", ascending=True).head(1)["idCliente"]

# %%

# %% 
# Lê o arquivo CSV com as transações dos clientes
transacoes = pd.read_csv("..//data/transacoes.csv")

# Visualiza as 5 primeiras linhas do DataFrame
transacoes.head(5)

# %%
# Ordena o DataFrame pela data de criação da transação,
# garantindo que a transação mais antiga venha primeiro
transacoes_ord = transacoes.sort_values("dtCriacao")

# Cria uma nova coluna 'data' contendo apenas a parte da data (sem hora)
# Isso facilita a identificação de transações por dia
transacoes_ord["data"] = pd.to_datetime(transacoes_ord["dtCriacao"]).dt.date

# %%
# Remove duplicatas mantendo apenas a primeira transação de cada cliente por dia
# Isso garante que, para cada cliente e data, apenas a transação mais antiga será considerada
transacoes_primeiras = transacoes_ord.drop_duplicates(keep="first", subset=["idCliente", "data"])

# Exibe o resultado final (opcional)
transacoes_primeiras.head()
