import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import date, time
from my_utils import load_data, descom_fecha
from make_plots import *
from html_strings import html_temp, descriptive_message_temp, intro
menu_types = (
    "General",
    "Usuarios",
    "Actividades",
) 
st.sidebar.header('Datos de entrada')
# get data
# @st.cache(allow_output_mutation=True) # maybe source of resource limit issue
# @st.cache
uploaded_file = st.sidebar.file_uploader("Suba un fichero CSV", type=["csv"])

# Chequear si se subió un fichero
if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)

    # Construir cuerpo de la app para fichero subido

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
        #date_s = st.date_input("De:", "2021-05-01")
        #date_f = st.date_input("Hasta:", "2021-05-01")
        st.pyplot(sns_plot_general1(df, "2021-05-01", "2021-06-30"))

        # Horas x wekday
        st.pyplot(sns_plot_general2(df, "2021-05-01", "2021-06-30")) 

    if menu == "Usuarios":
        # Sidebar
        n_users = st.sidebar.slider('Usuarios más activos a mostrar', 1, 50, 20)
        # Main column
        st.subheader('Análisis de usuarios (Estudiantes)')
        st.subheader('Usuarios más activos por cantidad de accesos')
        #sns.set(rc={'figure.figsize':(4,4)})
        fig = sns_plot_user1(df, n_users)
        st.pyplot(fig)
        #plt.gcf().set_size_inches(4, 4)

        st.subheader('Usuarios conectados por días')
        st.write("Solo si hay más de un día en los registros")
        st.pyplot(sns_plot_user2(df))
                

    if menu == "Actividades":
        st.subheader('En desarrollo')
        comp_types = sorted(df.Component.unique())
        selected_comp = st.sidebar.multiselect('Component', comp_types, comp_types)
        st.pyplot(sns_plot_comp(df, selected_comp))  
        
        #df.loc[df['Contexto del evento'].str.contains(r'^' + cadena)]
else:
    # Intro de la app
    st.write(intro)
    st.write("Suba un fichero csv para iniciar.")

    
