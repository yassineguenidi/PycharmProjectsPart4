import datetime
import plotly.express as px
import requests
import streamlit as st
import pandas as pd
from PIL import Image
from dateutil.relativedelta import relativedelta

logo = Image.open(r'images\att.png')
st.set_page_config(page_title="AttijariCredit", page_icon=logo, layout="wide")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
plt.style.use('ggplot')
# df=pd.read_csv(r"credit.csv")
import csv

def visualiser():

    # with open('credit.csv') as csvfile:
    #     df = list(csv.reader(csvfile))
    df = pd.read_csv("credit.csv",header=0)
    print(df)
    st.dataframe(df)

    st.header("please filter here")
    type = st.multiselect(
        "select type de credit",
        options=df["Type"].unique(),
        default=df["Type"].unique()
    )
    lieu = st.multiselect(
        "select lieu de naissance",
        options=df["lieu"].unique(),
        default=df["lieu"].unique()
    )
    etat_civile = st.multiselect(
        "select etat civile",
        options=df["etat_civile"].unique(),
        default=df["etat_civile"].unique()
    )
    employeur = st.multiselect(
        "select Employeur",
        options=df["employeur"].unique(),
        default=df["employeur"].unique()
    )
    revenu = st.slider(
        'Veuillez choisir le revenu',
        0.0, 10000.0,3500.0)
    retenu = st.slider(
        'Veuillez choisir le retenu',
        0.0, 100000.0,40000.0)

    df_selection = df.query(
        "Type==@type & lieu==@lieu & etat_civile==@etat_civile & employeur==@employeur "
        "& revenu<=@revenu & retenu <=@retenu"
    )



    st.dataframe(df_selection)


visualiser()