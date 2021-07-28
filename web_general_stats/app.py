import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, time
from my_utils import load_data, descom_fecha
from make_plots import *
from html_strings import intro
menu_types = (
    "General",
    "Participantes",
    "Actividades",
) 
st.sidebar.header('Datos de entrada')
# get data
# @st.cache(allow_output_mutation=True) # maybe source of resource limit issue
# @st.cache
uploaded_file = st.sidebar.file_uploader("Suba un fichero CSV", type=["csv"], accept_multiple_files=True)


# Chequear si se subió un fichero
if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)
    st.write("Cantidad de ficheros cargados: ", len(uploaded_file))
    st.write("Rango de fechas en los datos: ", 
                df["date"].min().strftime("%d/%m/%Y"), " y ", 
                df["date"].max().strftime("%d/%m/%Y") )

    # Construct body of app with uploaded file

    # General sidebar
    menu = st.sidebar.selectbox("Seleccionar análisis", menu_types)
    show_table = st.sidebar.checkbox("Ver tabla?", False)

    # Main column
    if show_table: 
        st.subheader('Registros a analizar')
        st.write(df)

    # If is menu General show general stuffs
    if menu == "General":
        st.subheader('Accesos generales por días')
        st.write("Solo si hay más de un día en los registros")
        date_s = st.date_input("De:", value=df["date"].min())
        date_f = st.date_input("Hasta", value=df["date"].max())
        st.write(date_s,date_f)
        st.pyplot(sns_plot_general1(df, pd.to_datetime(date_s), pd.to_datetime(date_f)))

        # Horas x wekday
        st.pyplot(sns_plot_general2(df, pd.to_datetime(date_s), pd.to_datetime(date_f))) 

    if menu == "Participantes":
        users = sorted(df.Name.unique())
        # Sidebar
        n_users = st.sidebar.slider('Participantes más activos a mostrar', 1, 50, 20)
        # Main column
        st.subheader('Análisis de Participantes')
        st.subheader('Cantidad de Participantes:' + str(len(users)))
        st.write('Participantes más activos por cantidad de accesos')
        st.pyplot(sns_plot_user1(df, n_users))
        users = sorted(df.Name.unique())
        user = st.selectbox("Seleccionar Participante", users)
        st.pyplot(sns_plot_user2(df[df.Name == user]))

               
    if menu == "Actividades":
        st.subheader('Recursos y tipos de actividades más vistos')
        comp_types = sorted(df.Component.unique())
        selected_comp = st.sidebar.multiselect('Component', comp_types, comp_types)
        st.pyplot(sns_plot_comp(df, selected_comp))  

        st.subheader('Participación en los foros')
        st.write('Participación en los foros (vistas y escritura)')
        st.pyplot(sns_plot_foros_gen(df))

        st.write("Solo participación activa ('Mensaje creado' o 'Algún contenido ha sido publicado.')")
        st.pyplot(sns_plot_foros_gen(df[(df['Event'] == 'Mensaje creado')|(df['Event'] == 'Algún contenido ha sido publicado.')]))



        
        #df.loc[df['Contexto del evento'].str.contains(r'^' + cadena)]
else:
    # Intro de la app
    st.write(intro)
    st.write("Suba un fichero csv para iniciar.")

    
