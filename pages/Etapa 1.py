import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


unsafe_allow_html = True

#st.title('Aplicação com Sreamlit') #chamando arquivo projeto_streamlit.py
#streamlit run http://localhost:8501/projeto_streamlit.py --> mas não funcionou, erro no run.

st.header("Etapa 1 CRISP - DM: Entendimento do negócio", divider="green")

st.write('Somos a ProsperAlta e oferecemos soluções inteligentes para o seu desenvolvimento financeiro.'
'A gente entende que as melhores escolhas são aquelas que trazem resultados para todos. Oferecemos mais de 300 produtos' 
'e serviços financeiros de um jeito simples e próximo para você, para a sua empresa e para o seu agronegócio. \n \n')

st.write('')
st.subheader('\n Objetivo da modelagem')

st.write('Nossa tecnologia avalia os melhores clientes com prosperidade na renda através das variáveis registradas' 
'em nosso modelo preditivo.')

