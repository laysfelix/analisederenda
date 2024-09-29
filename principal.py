import streamlit as st




st.set_page_config(
    page_title="2º Projeto .: Ciência de Dados ",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    #menu_items={
        #'Get Help': 'https://www.extremelycoolapp.com/help',
       # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        #'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

unsafe_allow_html = True

st.markdown("**Bem-vindo** :sunglasses:")
st.markdown("Cientista de Dados em formação: Lays Félix")

st.markdown('Eu tenho 37 anos e trabalho como Analista de TI há 17 anos na mesma empresa.')
st.markdown('Estou fazendo transição de carreira para :red[Ciência de Dados]:heart_eyes:')

st.write("[Github](https://github.com/laysfelix)")
st.write("[Kaggle](https://www.kaggle.com/laysfelix)") 
st.write("[Linkedin](https://www.linkedin.com/in/laysfelixbusiness/)")

st.sidebar.page_link('./principal.py', label="Home", icon="🏠")
st.sidebar.page_link('./pages/Etapa 1.py', label="Etapa 1: Entendimento do negócio", icon="1️⃣")
st.sidebar.page_link('./pages/Etapa 2.py', label="Etapa 2: Crisp-DM: Entendimento dos dados", icon="2️⃣")
st.sidebar.page_link('./pages/Etapa 2.1 Profile Report.py', label="Etapa 2.1: Profile Report", icon="📊")
st.sidebar.page_link('./pages/Etapa 3.py', label="Etapa 3: Preparação dos dados", icon="3️⃣")
st.sidebar.page_link('./pages/Etapa 4.py', label="Etapa 4: Modelagem", icon="4️⃣")
st.sidebar.page_link('./pages/Etapa 5.py', label="Etapa 5: Avaliação dos resultados", icon="5️⃣")
st.sidebar.page_link('./pages/Etapa 6.py', label="Etapa 6: Implantação dos resultados", icon="6️⃣")