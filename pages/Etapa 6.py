import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


unsafe_allow_html = True

#st.title('Aplicação com Sreamlit') #chamando arquivo projeto_streamlit.py
#streamlit run http://localhost:8501/projeto_streamlit.py --> mas não funcionou, erro no run.

st.header('Etapa 6 Crisp-DM: Implantação', divider="green")

st.write('Nessa etapa colocamos em uso o modelo desenvolvido, normalmente implementamos o modelo desenvolvido com certo nível de automação, que toma as decisões automaticamente - aprovando os clientes muito bons, negando os clientes muito ruins e enviando para análise manual os clientes intermediários.')

st.write('Analisando os modelos criados acima, eu escolheria o 2º modelo porque a proporção de todos os acertos na base de teste está maior - 95,37% que no 1º modelo - 91,82%.')