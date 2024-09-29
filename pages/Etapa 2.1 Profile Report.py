import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

from ydata_profiling import ProfileReport


unsafe_allow_html = True

st.write('')
st.subheader(' \n Geração do ProfileReport')

renda = pd.read_csv("./input/dados.csv")

# Produce and save the profiling report
profile = ProfileReport(renda, title="Análise de Renda gerado pelo Profile Report")
profile.to_file('analise_renda.html')

with st.spinner('Arquivo sendo gerado. Por favor, aguarde.'):
    time.sleep(20)
st.success("Done!")
# incluir https da url do git
st.write("[Análise de Renda]('analise_renda.html')")
