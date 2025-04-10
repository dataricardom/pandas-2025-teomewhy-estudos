# %%
import pandas as pd

# %%
# Lê o arquivo CSV com os dados dos clientes
clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%
# Remove linhas que contenham pelo menos um valor ausente (NA)
clientes.dropna()

# %%
# Aplica a remoção de linhas com NA ao próprio DataFrame
clientes = clientes.dropna()

# %%
# Remove apenas linhas onde **todas** as colunas têm NA
clientes.dropna(how="all")

# %%
# Exemplo de DataFrame com valores ausentes
df = pd.DataFrame({
    "nome": ["Téo", None, "Capu", "Junior"],
    "idade": [None, None, 43, 52],
    "salario": [3453, 4324, None, 5423]
})
df

# %%
# Remove linhas onde a coluna "idade" está completamente ausente (how="all" com subset)
df.dropna(how="all", subset=["idade"])

# %%
# Remove linhas onde **qualquer** uma das colunas "idade" ou "salario" está ausente
df.dropna(how="any", subset=["idade", "salario"])

# %%
# Preenche valores ausentes na coluna "idade" com 0
df["idade"] = df["idade"].fillna(0)
df

# %%
# Preenche valores ausentes na coluna "nome" com "Clarissa"
df["nome"].fillna("Clarissa")

# %%
# Preenche múltiplas colunas com valores diferentes
df.fillna({"nome": "Clarissa", "idade": 0})

# %%
# Preenche NA de "salario" e "idade" com a média de cada coluna
medias = df[["salario", "idade"]].mean()
df.fillna(medias)

# %%
df
