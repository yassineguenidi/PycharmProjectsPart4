
import streamlit as st
from mainPrincipal import mainPrincip
from prive import prive
from public import public
from retraite import retraite

def menu():


    menu = ["menu", "Secteur public", "Secteu Privé", "Retraite"]
    choices = st.sidebar.selectbox("Quel Type Du Credit", menu)

    if choices == "menu":
        mainPrincip()
    if choices == "Secteur public":
        public()
    if choices == "Secteu Privé":
        prive()
    if choices == "Retraite":
        retraite()

menu()