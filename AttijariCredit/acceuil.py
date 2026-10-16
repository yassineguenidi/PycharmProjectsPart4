import streamlit as st

from home import homePage
from login import loginPage
from signup import signup


def acceuil():

    acceuil = ["Page Acceuil", "Login", "SignUp"]
    choicea = st.sidebar.selectbox("Menu", acceuil)

    if choicea == "Page Acceuil":
        homePage()
    elif choicea == "Login":
        loginPage()
    elif choicea == "SignUp":
        signup()



acceuil()