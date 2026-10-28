
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="BI Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Dados
dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai"],
    "Vendas": [10000, 15000, 12000, 18000, 22000],
    "Clientes": [80, 120, 95, 150, 180]
}

df = pd.DataFrame(dados)

# Título
st.title("📊 BI Analytics Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Faturamento",
    f"R$ {df['Vendas'].sum():,.2f}"
)

col2.metric(
    "Clientes",
    int(df["Clientes"].sum())
)

col3.metric(
    "Ticket Médio",
    f"R$ {df['Vendas'].sum()/df['Clientes'].sum():.2f}"
)

st.divider()

# Gráficos
col4, col5 = st.columns(2)

with col4:
    fig1 = px.bar(
        df,
        x="Mês",
        y="Vendas",
        color="Vendas",
        title="Vendas por Mês"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.line(
        df,
        x="Mês",
        y="Clientes",
        markers=True,
        title="Clientes por Mês"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Tabela
st.subheader("Dados Detalhados")
st.dataframe(df, use_container_width=True)