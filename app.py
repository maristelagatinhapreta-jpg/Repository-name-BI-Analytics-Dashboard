import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="BI Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [10000, 15000, 12000, 18000, 22000, 25000],
    "Clientes": [80, 120, 95, 150, 180, 210],
    "Região": ["Sul", "Sudeste", "Sul", "Norte", "Nordeste", "Sul"]
}

df = pd.DataFrame(dados)

st.title("📊 BI Analytics Dashboard")

faturamento = df["Vendas"].sum()
clientes = df["Clientes"].sum()
ticket = faturamento / clientes

col1, col2, col3 = st.columns(3)

col1.metric("💰 Faturamento", f"R$ {faturamento:,.2f}")
col2.metric("👥 Clientes", clientes)
col3.metric("🎯 Ticket Médio", f"R$ {ticket:.2f}")

st.subheader("📈 Vendas por Mês")

fig_bar = px.bar(
    df,
    x="Mês",
    y="Vendas",
    color="Vendas",
    text_auto=True
)

st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("📉 Evolução de Clientes")

fig_line = px.line(
    df,
    x="Mês",
    y="Clientes",
    markers=True
)

st.plotly_chart(fig_line, use_container_width=True)

st.subheader("🥧 Distribuição por Região")

regioes = (
    df.groupby("Região")["Vendas"]
    .sum()
    .reset_index()
)

fig_pie = px.pie(
    regioes,
    names="Região",
    values="Vendas"
)

st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("📋 Dados Detalhados")

st.dataframe(df, use_container_width=True)