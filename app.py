import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Mi primera app de análisis con Streamlit")

data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C'],
    'Valor': [10, 30, 20]
})

fig = px.bar(data, x='Categoría', y='Valor', title='Gráfico de barras simple')
st.plotly_chart(fig)