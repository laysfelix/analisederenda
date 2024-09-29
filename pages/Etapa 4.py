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


st.header('Etapa 4 Crisp-DM: Modelagem', divider="green")

st.write('')

st.write('Nessa etapa que realizaremos a construção do modelo. Os passos típicos são:') 

st.write('* Selecionar a técnica de modelagem -> Utilizaremos a técnica de floresta aleatória (random forest), pois é uma técnica bastante versátil e robusta que captura bem padrões complexos nos dados, relativamente fácil de se usar e que costuma produzir excelentes resultados para uma classificação como estas. Vamos ver esse algoritmo em detalhes mais adiante no curso, mas pense nele por enquanto como uma regra complexa baseada nas variáveis explicativas que classifica o indivíduo como inadimplente ou não. Mais adiante no curso vamos extrair mais dessa técnica.')
st.write('* Desenho do teste -> Antes de rodar o modelo precisamos construir um desenho do teste que será realizado. Para desenvolver um modelo como este, é considerado uma boa prática dividir a base em duas, uma chamada treinamento, onde o algoritmo "aprende", e outra chamada teste, onde o algoritmo é avaliado. Essa prática fornece uma métrica de avaliação mais fidedigna do algoritmo, falaremos mais detalhes em lições futuras.')

st.write('Dividindo a base em treino e teste')

# Variáveis explicativas:
X = renda.drop("mau",axis = 1)
st.write('Quantidade de linhas e colunas (X):', X.shape)

# Variável resposta:
y = renda["mau"]
st.write('Quantidade de linhas (y):', len(y), '\n\n')

# Separando a base em 70% para treinamento e 30% para teste:
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=100)

st.write('Quantidade de linhas e colunas de X_train (70%):', X_train.shape)
st.write('Quantidade de linhas de y_train (70%):', 
      len(y_train), '\n')


st.write('Quantidade de linhas e colunas de X_test (30%):', X_test.shape)
st.write('Quantidade de linhas de y_test (30%):', 
      len(y_test))

st.write('____________________')

X_train

st.subheader('Rodando o modelo')

st.write('Treinar uma Random Forest com 3 árvores')

#corrigir para streamlit gerar a arvore (erro_Treinar uma Random Forest com 3 árvores-etapa4.png)
#clf = RandomForestClassifier(n_estimators=3)
#clf.fit(X_train,y_train)


#corrigir para streamlit gerar a arvore (erro_Treinar uma Random Forest com 3 árvores-etapa4.png)
#print erro_valores-preditos-etapa4.png
# new_data = X_test

# # Processar a entrada
# if new_data:
#     new_data = [float(x) for x in new_data.split(',')]
#     new_data = np.array(new_data).reshape(1, -1)

#     # Fazer a previsão
#     y_pred = clf.predict(new_data)

#     # Exibir o resultado
#     st.write("A previsão é:", y_pred[0])


# Calculando a acuracia
# acc = metrics.accuracy_score(y_test, y_pred)
# print('Acurácia: {0:.2f}%'.format(acc*100))


st.subheader('Matriz de Confusão')


# tab = pd.crosstab(index = y_pred, 
#                   columns = y_test)
# tab
