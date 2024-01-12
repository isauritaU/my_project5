import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button(
    'Construir histograma de kilometraje')  # crear un botón
disper_button = st.button('Relación de kilometraje y precio')
build_hist = st.checkbox('Relación precio y año del modelo')
build_hist_2 = st.checkbox('Modelos de vehículos')

st.header('Catálogo de Vehículos US')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creando un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)
elif build_hist:
    st.write('a continuación la relación entre año del modelo del vehiculo y precio')
    fig_3 = px.histogram(car_data, x='price', y='model_year')
    st.plotly_chart(fig_3, use_container_width=True)
elif build_hist_2:
    st.write('a continuación los modelos de los vehículos')
    fig_4 = px.histogram(car_data, x='model')
    st.plotly_chart(fig_4, use_container_width=True)
elif disper_button:
    st.write('creando un gráfico de dispersión en relación kilometraje/precio')
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)
