import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import date, time


def sns_plot_general1(df, date_s, date_f):
    dfg2 = df['date'].value_counts().reset_index().rename(
            columns={'index': 'Date', 'date':'N'})
    dfg2["Date"] = pd.to_datetime(dfg2["Date"]) 
    g = sns.relplot(x="Date", y="N", kind="line", data=dfg2[(dfg2['Date'] > date_s) & (dfg2['Date'] < date_f)])
    plt.xticks(rotation=-45)
    g.fig.set_size_inches(14, 4)
    access_mean = dfg2[(dfg2['Date'] > date_s) & (dfg2['Date'] < date_f)].N.mean()
    g.ax.axhline(access_mean, alpha=0.3, color='red')
    return g

def sns_plot_general2(df, date_s, date_f):
    fig, ax = plt.subplots()
    df["date"] = pd.to_datetime(df["date"])
    df = df[(df['date'] > date_s) & (df['date'] < date_f)]
    dfg5 = df[["wd","hour"]].value_counts().reset_index().rename(
            columns={0:'N'})
    dfg6 = dfg5.pivot_table(index='wd', columns='hour', values='N')
    ax = sns.heatmap(dfg6)
    #data=dfg2[(dfg2['Date'] > date_s) & (dfg2['Date'] < date_f)])
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
    fig, ax = plt.subplots()
    fig = sns.catplot(y="Name", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data=df, order=df['Name'].value_counts().iloc[:n_users].index)
    plt.title("Usuarios más activos")
    #plt.figure(figsize=(4, 4))
    plt.gcf().set_size_inches(8, 4)
    return fig

def sns_plot_user2(df):
    #fig, ax = plt.subplots()
    df_usuario =  df[['date','Name']].value_counts().reset_index().rename(
        columns={'index': 'date', 'Name': 'User', 0:'N'})
    df_2 = df_usuario['date'].value_counts().reset_index().rename(
        columns={'index': 'Date', 'date':'N'}).sort_values('Date')
    fig = sns.relplot(x="Date", y="N", kind="line", data=df_2)
    plt.xticks(rotation=-45)
    #plt.figure(figsize=(16, 4))
    plt.gcf().set_size_inches(12, 4)
    return fig

def sns_plot_comp(df, comps):
    fig, ax = plt.subplots()
    #df_comp = df[(df.Componente.isin(cadena))]['Componente'].value_counts().reset_index().rename(
        #columns={'index': 'Componente', 'Componente':'N'})
    fig = sns.catplot(y="Component", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data=df, order=df[(df.Component.isin(comps))]['Component'].value_counts().index)
                    #data=df, order=df['Component'].value_counts().index)
                    #data=df_comp)
    plt.gcf().set_size_inches(8, 4)
    return fig

def sns_plot_foros_gen(df):
    fig, ax = plt.subplots()
    df2 = df.loc[df['Context'].str.contains(r'^Foro'),['Context','Name']].value_counts().reset_index().rename(columns={'index': 'Context', 0:'N'})
    fig = sns.catplot(y="Context", kind="count",
                    palette="ch:.25", edgecolor=".6",
                    data= df2,
                    order=df2['Context'].value_counts().index,
                    height=4)
    plt.gcf().set_size_inches(6, 6)
    return fig



