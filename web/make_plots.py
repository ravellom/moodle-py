import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sns_plot_user1(df, n_users):
    fig, ax = plt.subplots()
    fig = sns.catplot(y="Name", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data=df, order=df['Name'].value_counts().iloc[:n_users].index)
    plt.title("Usuarios más activos")
    return fig

def sns_plot_user2(df):
        st.subheader('Usuarios conectados por día')
        df_usuario =  df[['date','Name']].value_counts().reset_index().rename(
            columns={'index': 'date', 'Name': 'User', 0:'N'})
        df_2 = df_usuario['date'].value_counts().reset_index().rename(
            columns={'index': 'Date', 'date':'N'}).sort_values('Date')
        fig = sns.relplot(x="Date", y="N", kind="line", data=df_2)
        return fig


