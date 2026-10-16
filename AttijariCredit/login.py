from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

from database import make_hashes, login_user, check_hashes
from prive import prive
from public import public
from retraite import retraite
mainSector =  st.container()

def loginPage():
    image = Image.open(r'images\attijari.gif')
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.title("BIENVENUE A L'AGENCE DE REMADA")
    username = st.sidebar.text_input("Nom d'utilisateur")
    password = st.sidebar.text_input("Mot du passe", type='password')
    if st.sidebar.button("Submit"):

        hashed_pswd = make_hashes(password)
        if login_user(username, check_hashes(password, hashed_pswd)):
            st.sidebar.success("Vous avez connecté")
            selected = option_menu(
                menu_title= "CHOISIR LE SECTEUR",
                options =["PRIVE","PUBLIC","RETRAITE"],
                icons= ["house","book", "envelop"],
                menu_icon="cast",
                default_index=0,
                orientation="horiznontal",
            )
            if selected == "PRIVE":

                st.text("prive")
            elif selected =="PUBLIC":
                st.text("public")
                public()
            elif selected == "RETRAITE":

                retraite()
        else:
            st.sidebar.error("Les coordonnées sont invalides Veuillez réessayer !")
            return



loginPage()