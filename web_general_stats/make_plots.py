from matplotlib import figure
from seaborn.rcmod import set_style
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import date, time


def sns_plot_general1(df, date_s, date_f):
    dfg2 = df['date'].value_counts().reset_index().rename(
            columns={'index': 'Date', 'date':'N'} )
    dfg2["Date"] = pd.to_datetime(dfg2["Date"]) 
    g = sns.relplot(x="Date", y="N", kind="line", 
                    data=dfg2[(dfg2['Date'] > date_s) & (dfg2['Date'] < date_f)])
    plt.xticks(rotation=-45)
    g.fig.set_size_inches(14, 4)
    access_mean = dfg2[(dfg2['Date'] > date_s) & (dfg2['Date'] < date_f)].N.mean()
    g.ax.axhline(access_mean, alpha=0.3, color='red', linestyle="--")
    g.set_axis_labels(x_var="Fecha",y_var="Accesos")
    return g

def sns_plot_general2(df, date_s, date_f):
    fig, ax = plt.subplots(figsize=(6,3)) 
    df["date"] = pd.to_datetime(df["date"])
    df = df[(df['date'] > date_s) & (df['date'] < date_f)]
    dfg5 = df[["wd","hour"]].value_counts().reset_index().rename(
            columns={0:'N'})
    dfg6 = dfg5.pivot_table(index='wd', columns='hour', values='N')
    ax = sns.heatmap(dfg6, cmap="Reds", linewidths=.3)
    ax.set_xlabel("Horas del día")
    ax.set_ylabel("Días de semana (0 - Domingo : 6 - Sábado)")
    return fig

def sns_plot_course1(df, n_context):
    #fig, ax = plt.subplots()
    df2 = df.loc[df['Context'].str.contains(r'^Curso')]
    g = sns.catplot(y="Context", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data= df2,
                    order=df2['Context'].value_counts().iloc[:n_context].index,
                    height=4)
                    #aspect=4/4)
    g.set_axis_labels("Accesos", "Cursos", labelpad=10)
    g.fig.set_size_inches(6, 6)
    return g

def sns_plot_user1(df, n_users):
    g = sns.catplot(y="Name", kind="count",
                    #palette="ch:.25", edgecolor=".6",
                    data=df, order=df['Name'].value_counts().iloc[:n_users].index)
    plt.title("Usuarios más activos")
    g.fig.set_size_inches(8, 4)
    g.set_axis_labels("Accesos", "Nombre", labelpad=5)
    return g

def sns_plot_user2(df):
    df2 = df[df.Component.isin(["Foro", "Tarea", "Glosario","Cuestionario", "Libro"])]
    df3 = ( df2['Context']
                .value_counts()
                .reset_index() 
                .rename(columns={'index': 'Context', 'Context':'N'}) )
    g =  sns.catplot(y="Context", x="N", kind="bar", data=df3, 
                        edgecolor=".8", #palette="ch:.25"
                        height=5, aspect=2)
    g.ax.set_title("Participación en las principales actividades del curso")
    g.set_axis_labels("Accesos", "Actividades", labelpad=5)
    return g

def sns_plot_comp(df, comps):
    #df_comp = df[(df.Componente.isin(cadena))]['Componente'].value_counts().reset_index().rename(
        #columns={'index': 'Componente', 'Componente':'N'})
    g = sns.catplot(y="Component", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data=df, order=df[(df.Component.isin(comps))]['Component'].value_counts().index)
                    #data=df, order=df['Component'].value_counts().index)
                    #data=df_comp)
    g.fig.set_size_inches(8, 4)
    g.set_axis_labels("Accesos", "Tipo de actividades", labelpad=5)
    return g

def sns_plot_foros_gen(df):
    df2 = df.loc[df['Context'].str.contains(r'^Foro'),['Context','Name']].value_counts().reset_index().rename(columns={'index': 'Context', 0:'N'})
    g = sns.catplot(y="Context", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data= df2,
                    order=df2['Context'].value_counts().index,
                    height=4)
    g.fig.set_size_inches(6, 6)
    g.set_axis_labels("Cantidad de estudiantes", "Foros", labelpad=5)
    return g



