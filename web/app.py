import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from my_utils import descom_fecha
from make_plots import sns_plot_user

st.write("""
# Análisis de reportes de Moodle

Esta aplicación analiza los ficheros csv descargados de  Administración de sistema/Reportes activos!
""")

st.sidebar.header('Datos de entrada')
# get data
# @st.cache(allow_output_mutation=True) # maybe source of resource limit issue
# @st.cache
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


# Chequear si se subió un fichero
if uploaded_file is not None:

    # Construir cuerpo de la app para fichero subido
    df = pd.read_csv(uploaded_file)
    df = df.rename(columns={
                    'Hora': 'DT',
                    'Nombre completo del usuario': 'Name',
                    'Usuario afectado': 'User_afec',
                    'Contexto del evento': 'Context',
                    'Componente': 'Component',
                    'Nombre evento': 'Event',
                    'Descripción': 'Description',
                    'Origen': 'Origen',
                    'Dirección IP': 'IP',
                })
    df = df.loc[df["Name"] != "-"]
    df = descom_fecha(df)

    # Sidebar
    n_users = st.sidebar.slider('Usuarios más activos a mostrar', 1, 50, 20)
    n_context = st.sidebar.slider('Cursos más activos a mostrar', 1, 50, 20)

    # Main
    st.subheader('Registros a analizar')
    st.write(df)

    st.subheader('Usuarios más activos por cantidad de accesos')
    fig = sns.catplot(y="Name", kind="count",
                palette="ch:.25", edgecolor=".6",
                data=df, order=df['Name'].value_counts().iloc[:n_users].index)
    st.pyplot(fig)

    st.subheader('Cursos más activos por cantidad de accesos')
    fig = sns.catplot(y="Context", kind="count",
                palette="ch:.25", edgecolor=".6",
                data=df, order=df['Context'].value_counts().iloc[:n_context].index)
    st.pyplot(fig)

    




else:

    st.write("Suba un fichero csv para iniciar.")

    
