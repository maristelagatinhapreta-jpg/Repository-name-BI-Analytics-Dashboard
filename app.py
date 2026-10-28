import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Teste")

dados = pd.DataFrame({
    "Mes": ["Jan", "Fev", "Mar"],
    "Vendas": [10, 20, 15]
})

fig = px.bar(dados, x="Mes", y="Vendas")

st.plotly_chart(fig)