import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn import metrics

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

#%matplotlib inline


unsafe_allow_html = True

#criando dataframe através do arquivo csv
renda = pd.read_csv('./input/dados.csv')


st.header("Etapa 3 Crisp-DM: Preparação dos dados", divider="green")

st.write('')

st.write('Nessa etapa realizamos as seguintes operações com os dados:') 

st.write('* seleção: Nesta fase, os dados já estão pré-selecionados')
st.write('* limpeza: Nesta fase, os dados já identificamos e tratamos os dados faltantes')
st.write('* construção: Nesta fase, não faremos construção de novas variáveis')
st.write('* integração: Temos apenas uma fonte de dados, não é necessário integração')
st.write('* formatação: Os dados já se encontram em formatos úteis')

st.write('____________________')

st.subheader('\n Conferindo que não há dados faltantes')
# Verificar se há valores faltantes
dados_faltantes = renda.isna().any()
# corrigir erro comentado - colocar quebra de linha
#dados_faltantes = pd.dataframe.dados_faltantes
st.warning(dados_faltantes)
    
st.write('____________________')

st.subheader('\n Conferindo as categorias e frequência dos dados')
# Verificar se há valores faltantes
select_dtypes = renda.select_dtypes('object').describe().transpose()
st.dataframe(select_dtypes)

st.write('____________________')

st.subheader('\n Quantidade de categorias por variável')

metadata = pd.DataFrame(renda.dtypes, columns = ['tipo'])

metadata['n_categorias'] = 0

for var in metadata.index:
    metadata.loc[var,'n_categorias'] = len(renda.groupby([var]).size())

metadata

st.write('____________________')

st.subheader('\n Conversão das variáveis categóricas em variáveis numéricas (dummies)')

renda = pd.get_dummies(data=renda.copy(),
                    columns=['sexo', 'posse_de_veiculo', 'posse_de_imovel'],
                    drop_first=True)

renda = pd.get_dummies(data=renda)

print(renda.info())
renda

st.write('____________________')