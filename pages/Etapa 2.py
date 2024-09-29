import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
#import plotly.express as px

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn import metrics

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

#%matplotlib inline


unsafe_allow_html = True

#st.title('Aplicação com Sreamlit') #chamando arquivo projeto_streamlit.py
#streamlit run http://localhost:8501/projeto_streamlit.py --> mas não funcionou, erro no run.

st.header('Etapa 2 CRISP - DM: Entendimento dos dados', divider="green")

st.write('Foram fornecidas 16 variáveis incluindo a variável resposta (em negrito).' 
'O significado de cada uma dessas variáveis se encontram na tabela abaixo.')

st.write('')
st.subheader(' \n Dicionário de dados')

st.write('Os dados estão dispostos em uma tabela com uma linha para cada cliente, e uma coluna para cada variável '
'armazenando as características desses clientes.')

st.image(".\dicionario_de_dados.png")

st.write('')
st.subheader('\n Importando bibliotecas e pacotes')

st.image(".\import_bibliotecas.png")


renda = pd.read_csv('./input/dados.csv')

st.write('Quantidade de linhas e colunas do dataframe:\n',
      renda.shape[0], 'linhas \n',
      renda.shape[1], 'colunas \n'
     )

st.write('Quantidade de linhas duplicadas:',
      renda.duplicated().sum())

renda.drop_duplicates(inplace=True)

st.write('Quantidade de linhas após remoção:',
      len(renda), '\n')

renda.reset_index(drop=True, inplace=True)

#st.write(renda.info())

renda

st.write('')
st.subheader(' \n Entendimento dos dados - Univariada')
st.write('Nesta etapa tipicamente avaliamos a distribuição de todas as variáveis. Nesta demonstração vamos analisar algumas variáveis.')

st.write(renda['mau'].value_counts())
st.write("\nTaxa de inadimplentes:")
st.write(renda['mau'].mean())

st.write('____________________')


st.write('\n Distribuição percentual da variável resposta (mau):')
st.write(round(renda.mau.value_counts(normalize=True).rename(
    {False: 'Adimplentes',
     True: 'Inadimplentes'}) * 100, 2))

st.write('____________________')

# Criar o gráfico
fig, ax = plt.subplots()
renda['mau'].value_counts().plot.bar(rot=0, ax=ax)
plt.title(label='Distribuição da variável resposta (mau)')
plt.xlabel(xlabel="Cliente")
plt.xticks(ticks=[0,1], labels=['Adimplentes', 'Inadimplentes'])

# Exibir o gráfico no Streamlit
st.pyplot(fig)

st.write('____________________')

fig2, ax = plt.subplots()
renda['posse_de_imovel'].value_counts().plot.bar(rot=0, ax=ax)
plt.title(label='Distribuição da Posse de imóvel')
plt.xlabel(xlabel="Imóvel")
plt.xticks(ticks=[0,1], labels=['Não possuem', 'possuem'])

# Exibir o gráfico no Streamlit
st.pyplot(fig2)

st.write('____________________')


fig3, ax = plt.subplots()
renda['posse_de_veiculo'].value_counts().plot.bar(rot=0, ax=ax)
plt.title(label='Distribuição da Posse de veículo')
plt.xlabel(xlabel="Veículo")
plt.xticks(ticks=[0,1], labels=['Não possuem', 'possuem'])

# Exibir o gráfico no Streamlit
st.pyplot(fig3)

st.write('____________________')


st.write('')
st.subheader(' \n Entendimento dos dados - Bivariadas')
st.write('Nesta etapa vamos entender a alteração da inadimplência indicada pela variável' 
'resposta e as variáveis explicativas. Para isto, vamos calcular a taxa de inadimplentes' 
'(qtd inadimplentes / total) para diferentes variáveis.')

#1º gráfico

var = 'idade'
cat_srs, bins = pd.qcut(renda[var], 4, retbins=True)
g = renda.groupby(cat_srs)
biv = g['mau'].mean()

fig5, ax = plt.subplots()
plt.title(label='Distribuição dos inadimplentes por idade')
ax = biv.plot.line(ax=ax)
ax.set_ylabel("Proporção de inadimplentes")
ax.set_xlabel("Idade")
ticks = plt.xticks(range(len(biv.index.values)), biv.index.values, rotation=90)

st.pyplot(fig5)

#2º gráfico

var = 'tempo_emprego'
cat_srs, bins = pd.qcut(renda[var], 4, retbins=True)
g = renda.groupby(cat_srs)
biv = g['mau'].mean()

fig6, ax = plt.subplots()
plt.title(label='Distribuição dos inadimplentes por tempo de emprego')
ax = biv.plot.line(ax=ax)
ax.set_ylabel("Proporção de inadimplentes")
ax.set_xlabel("Tempo de emprego")
ticks = plt.xticks(range(len(biv.index.values)), biv.index.values, rotation=90)

st.pyplot(fig6)
