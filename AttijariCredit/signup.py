from PIL import Image
import streamlit as st
# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib
# DB Management
import sqlite3

from database import create_usertable, add_userdata, make_hashes


def signup():
    image = Image.open(r'images\attijari.gif')

    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
    st.title("BIENVENUE A L'AGENCE DE REMADA sign up")
    image1 = Image.open(r'images\credit1.jpg')
    image2 = Image.open(r'images\enligne.jpg')
    images = [image1, image2]
    st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
    st.sidebar.subheader("Créer un nouveau compte")
    new_user = st.sidebar.text_input("Nom d'utilisateur")
    new_password = st.sidebar.text_input("Mot du passe", type='password')

    if st.sidebar.button("Signup"):
        create_usertable()
        if add_userdata(new_user, make_hashes(new_password)):
            st.sidebar.success("You have successfully created a valid Account")
            st.sidebar.info("Go to Login Menu to login")
            return True
        return False

signup()