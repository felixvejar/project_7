import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Mi primera app web")
car_data = pd.read_csvf("vehicles_us.csv")
hist_button = st.button("Construir Histograma")
scatter_button = st.button("Construir Gráfico de Dispersión")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncions de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")
    fig = px.scatter(car_data, x="odometer", y="price", color="manufacturer")
    st.plotly_chart(fig, use_container_width=True)
