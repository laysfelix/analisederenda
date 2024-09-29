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

#Definindo variáveis, treino e teste

# Variáveis explicativas:
# X = renda.drop("mau",axis = 1)

# # Variável resposta:
# y = renda["mau"]

# # Separando a base em 70% para treinamento e 30% para teste:
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)


st.header('Etapa 5 Crisp-DM: Avaliação dos resultados', divider="green")

st.write('Faremos a avaliação do nosso modelo através do percentual de acerto, avaliando a classificação do modelo (inadimplente e não inadimplente) e comparando com o estado real armazenado na variável resposta (AtrasoRelevante2anos). Esse percentual de acerto é frequentemente chamado de acurácia.') 

st.subheader('Decision -> 1ª TreeClassifier')

# clf = DecisionTreeClassifier(random_state=100)
# clf = clf.fit(X=X_train, 
#               y=y_train)
# clf


# plt.figure(figsize=(18,9))
# plot_tree(decision_tree=clf,
#           feature_names=X_train.columns.tolist(),
#           class_names=['bons', 'maus'],
#           filled=True, 
#           rounded=True)

# plt.show()

st.image(".\import_1a_arvore_decision.png")


st.subheader('.:. Matriz de confusão para a base de treino da 1ª árvore')

st.image(".\_1a_matriz-de-confusao-treino.png")



st.subheader('.:. Matriz de confusão para a base de teste da 1ª árvore')

st.image(".\_1a_matriz-de-confusao-teste.png")

# predict_train = clf.predict(X=X_train)

# st.write('Valores preditos de treino:') 
# st.write(pd.Series(predict_train).value_counts(), '\n')

# prst.writeint('Valores reais:')
# st.write(y_train.value_counts())



st.subheader('Decision -> 2ª TreeClassifier')

st.image(".\import_2a_arvore_decision.png")



st.subheader('.:. Matriz de confusão para a base de treino da 2ª árvore')

st.image(".\_2a_matriz-de-confusao-treino.png")



st.subheader('.:. Matriz de confusão para a base de teste da 2ª árvore')

st.image(".\_2a_matriz-de-confusao-teste.png")