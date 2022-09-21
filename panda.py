#Usando o Google colab

#importando a biblioteca pandas
import pandas as pd
#pd e uma abreviação que criamos

df = pd.read_csv("/content/drive/My Drive/Datasets/Gapminder.csv",error_bad_lines=False, sep=";")
#copiando o caminho do arquivo aqui
#error_bad_lines=False, sep=";" passando esse parametro 


#Visualizando as 5 primeiras linhas
df.head(5) #ja que chamamos a planilha de df,apenas chamamos o head para ler
#trocando os nomes das colunas
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})
#country será agora país,assim como os outros

#Sabendo a quantidade de linhas e colunas
df.shape

#sabendo as colunas
df.columns

#sabendo os tipos de variaveis em cada coluna
df.dtypes

#sabendo as ultimas linhas do arquivo
df.tail()

#pega 5 linhas aleatoriamente
df.sample


#sabendo os valores da coluna "continente"
df["continente"].unique()

#sabendo todos os dados da oceania
Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()

#agrupando e sabendo a quantidade de paises em qual continente
df.groupby("continente")["Pais"].nunique()
#sabendo a expectativa de vida de cada ano
df.groupby("Ano")["Expectativa de vida"].mean()

#sabendo o valor medio do PIB
df["PIB"].mean()
#soma da coluna PIB
df["PIB"].sum()

#alterando o tipo de dado da coluna lojaID
df["LojaID"] = df["LojaID"].astype("object")

#Consultando linhas com valores faltantes ou nulos
df.isnull().sum()

#Substituindo os valores nulos pela média da venda
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando as linhas com valores nulos
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

#Criando a coluna de receita
#multiplicando a coluna vendas pela da quantidade
df["Receita"] = df["Vendas"].mul(df["Qtde"])

#Retornando a maior receita
df["Receita"].max()

#Retornando a menor receita
df["Receita"].min()

#nlargest ver as 3 maiores receitas junto com todas as outras colunas
df.nlargest(3, "Receita")

#nsamllest ver as 3 menores receitas junto com todas as outras colunas
df.nsmallest(3, "Receita")

#Agrupamento por cidade
#somará a soma da receita de cada cidade 
df.groupby("Cidade")["Receita"].sum()

#Ordenando o conjunto de dados pela coluna receita do maior ao menor, das 10 primeiras linhas
df.sort_values("Receita", ascending=False).head(10)
