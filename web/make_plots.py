import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def matplotlib_plot(chart_type: str, df):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": 1, "Chinstrap": 2, "Gentoo": 3}
            )
            ax.scatter(x=df["bill_depth_mm"], y=df["bill_length_mm"], c=df["color"])
            plt.title("Bill Depth by Bill Length")
            plt.xlabel("Bill Depth (mm)")
            plt.ylabel("Bill Length (mm)")
    elif chart_type == "Histogram":
        with st.echo():
            plt.title("Count of Bill Depth Observations")
            ax.hist(df["bill_depth_mm"])
            plt.xlabel("Bill Depth (mm)")
            plt.ylabel("Count")
    elif chart_type == "Bar":
        with st.echo():
            df_plt = df.groupby("species", dropna=False).mean().reset_index()
            ax.bar(x=df_plt["species"], height=df_plt["bill_depth_mm"])
            plt.title("Mean Bill Depth by Species")
            plt.xlabel("Species")
            plt.ylabel("Mean Bill Depth (mm)")

    elif chart_type == "Line":
        with st.echo():
            ax.plot(df.index, df["bill_length_mm"])
            plt.title("Bill Length Over Time")
            plt.ylabel("Bill Length (mm)")
    elif chart_type == "3D Scatter":
        ax = fig.add_subplot(projection="3d")
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": 1, "Chinstrap": 2, "Gentoo": 3}
            )
            ax.scatter3D(
                xs=df["bill_depth_mm"],
                ys=df["bill_length_mm"],
                zs=df["body_mass_g"],
                c=df["color"],
            )
            ax.set_xlabel("bill_depth_mm")
            ax.set_ylabel("bill_length_mm")
            ax.set_zlabel("body_mass_g")
            plt.title("3D Scatterplot")
    return fig

def sns_plot_user(df):
    fig, ax = plt.subplots()
    sns.barplot(data=df)
    plt.title("Usuarios más activos")
    return fig

def sns_plot(chart_type: str, df):
    """ return seaborn plots """
    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            sns.scatterplot(
                data=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                hue="species",
            )
            plt.title("Bill Depth by Bill Length")
    elif chart_type == "Histogram":
        with st.echo():
            sns.histplot(data=df, x="bill_depth_mm")
            plt.title("Count of Bill Depth Observations")
    elif chart_type == "Bar":
        with st.echo():
            sns.barplot(data=df, x="species", y="bill_depth_mm")
            plt.title("Mean Bill Depth by Species")
    elif chart_type == "Boxplot":
        with st.echo():
            sns.boxplot(data=df)
            plt.title("Bill Depth Observations")
    elif chart_type == "Line":
        with st.echo():
            sns.lineplot(data=df, x=df.index, y="bill_length_mm")
            plt.title("Bill Length Over Time")
    elif chart_type == "3D Scatter":
        st.write("Seaborn doesn't do 3D ☹️. Here's 2D.")
        sns.scatterplot(data=df, x="bill_depth_mm", y="bill_length_mm", hue="island")
        plt.title("Just a 2D Scatterplot")
    return fig



