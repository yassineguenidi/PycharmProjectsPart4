import datetime

import requests
import streamlit as st
import pandas as pd
from PIL import Image
from dateutil.relativedelta import relativedelta

logo = Image.open(r'images\att.png')
st.set_page_config(page_title="AttijariCredit", page_icon=logo, layout="wide")


def gererProfile():

    logo = Image.open(r'images\attijari.gif')
    cinT=ribT=nomT =""
    rechercheParNom(nomT)
    rechercheParCin(cinT)
    rechercheParRib(ribT)
    # ---- BIENVENU ----
    with st.container():
        left_column, mid_column, right_column = st.columns((1, 3, 1))
        with left_column:
           st.empty()
        with mid_column:
            st.image(logo, width=400)
            st.header("BIENVENUE A L'AGENCE DE REMADA")
            st.subheader("Croire en vous")
        with right_column:
            st.empty()

    # ---- RECHERCHE COORDONNEES ----
    with st.container():

        st.write("---")

        left_column, mid_column, right_column = st.columns((1, 1, 1))
        with mid_column:
            st.header("Fiche du client")
            type = st.selectbox(
                'Rechercher par',
                ('Nom', 'RIB', 'CIN'))
            st.write("Vous avez choisi "+ type)

            if type=="CIN":
                cinT = st.text_input("Entrez le CIN du client à rechercher")
            if type=="Nom":
                nomT = st.text_input("Entrez le Nom du client à rechercher")
            if type=="RIB":
                ribT = st.text_input("Entrez RIB du client à rechercher")
            if st.button("Rechercher"):
                if nomT != "":
                    rechercheParNom(nomT)
                nomT=""
                if cinT != "":
                    st.write(cinT)
                    rechercheParCin(cinT)
                cinT=""
                if ribT != "":
                    st.write(ribT)
                    rechercheParRib(ribT)
                ribT=""


    # ---- COORDONNEES ----
    with st.container():
        st.write("---")
        left_column, mid_column, right_column = st.columns((1, 1, 1))
        with mid_column:
            st.subheader("Vos coordonnées")
            st.markdown("##")
    with st.container():

        o,left_column,mid_column, right_column ,r = st.columns((1,1, 1,1,1))
        with left_column:

            st.write("Le nom est : " + nomN)
            st.write("Le Numero du RIB : "+ribN)
            st.write("Le CIN : "+ cinN)
            st.write("Date naissance : " + dateNaissN)
            st.write("Adresse : " + adresseN)
            st.write("Profession : " + professionN)
            st.write("Revenu : " + revenuN)
            st.write("Etat civile : " + etatN)

        with mid_column:

            st.write(".")
            st.write(".")
            st.write("Delivré le : " + delivreN)
            st.write("Lieu de naissance : "+ lieuN)
            st.write("Code Postale : " + codePostal)
            st.write("Employeur : " + employeurN)
            st.write("Retenu : " + retenuN)
            st.write(".")

        with right_column:
            st.write(".")
            st.write(".")
            st.write(".")
            st.write("Nationnalité : "+nationnaliteN)
            st.write(".")
            st.write(".")
            st.write(".")

    if etatN=="Marie(e)":
        with st.container():
            st.write("---")
            left_column, mid_column, right_column = st.columns((1, 1, 1))
            with mid_column:
                st.subheader("coordonnées du compte joint(e)")
                st.markdown("##")
        with st.container():

            o, left_column, mid_column, right_column, r = st.columns((1, 1, 1, 1, 1))
            with left_column:
                st.write("Le nom est : " + nomConjN)
                st.write("Le CIN : " + cinConjN)
                st.write("Date naissance : " + dateNaissConjN)
                st.write("Adresse : " + adresseConjN)
                st.write("Revenu : " + revenuConjN)

            with mid_column:
                st.write(".")
                st.write("Delivré le : " + delivreConjN)
                st.write("Lieu de naissance : " + lieuConjN)
                st.write(".")
                st.write("Retenu : " + retenuConjN)
            with right_column:
                st.write(".")
                st.write(".")
                st.write("Nationnalité : " + nationnaliteConjN)
                st.write(".")

def rechercheParCin(thiscin):
    import csv
    global nom, ribN, cinN, delivreN, dateNaissN, lieuN, nationnaliteN, adresseN, codePostal, professionN, employeurN
    global revenuN, retenuN, etatN, nomConjN, cinConjN, delivreConjN, dateNaissConjN, lieuConjN, nationnaliteConjN
    global adresseConjN, professionConjN, employeurConjN, revenuConjN, retenuConjN

    nomN = ""
    ribN = ""
    cinN = ""
    delivreN = ""
    dateNaissN = ""
    lieuN = ""
    nationnaliteN = ""
    adresseN = ""
    codePostal = ""
    professionN = ""
    employeurN = ""
    revenuN = ""
    retenuN = ""
    etatN = ""
    nomConjN = ""
    cinConjN = ""
    delivreConjN = ""
    dateNaissConjN = ""
    lieuConjN = ""
    nationnaliteConjN = ""
    adresseConjN = ""
    professionConjN = ""
    employeurConjN = ""
    revenuConjN = ""
    retenuConjN = ""
    with open("credit.csv", 'r') as f:
        obj = csv.DictReader(f)

        for i in obj:
            if i["cin"]==thiscin:
                nomN=i["nom"]
                ribN = i["RIB"]
                cinN = thiscin
                delivreN = i["delivre"]
                dateNaissN = i["date"]
                lieuN = i["lieu"]
                nationnaliteN = i["nationnalite"]
                adresseN = i["adresse"]
                codePostal = i["code_postal"]
                professionN = i["profession"]
                employeurN = i["employeur"]
                revenuN = i["revenu"]
                retenuN = i["retenu"]
                etatN = i["etat_civile"]

                nomConjN = i["nom_conjoint"]
                cinConjN = i["cinConj"]
                delivreConjN = i["delivreConj"]

                dateNaissConjN =i["date_naiss_conj"]
                lieuConjN = i["lieu_conj"]
                nationnaliteConjN = i["nationnalite_conj"]
                adresseConjN = i["adresseConj"]
                professionConjN = i["profession_conj"]
                employeurConjN = i["employeur_conj"]
                revenuConjN = i["revenu_conj"]
                retenuConjN = i["retenu_conj"]
        print("par cin  ribN : " + ribN + " le nom : " + nomN + "dateNaissN : " + dateNaissN)

def rechercheParNom(thisnom):
    import csv

    global nomN, ribN, cinN, delivreN, dateNaissN, lieuN, nationnaliteN, adresseN, codePostal, professionN, employeurN
    global revenuN, retenuN, etatN, nomConjN, cinConjN, delivreConjN, dateNaissConjN, lieuConjN, nationnaliteConjN
    global adresseConjN, professionConjN, employeurConjN, revenuConjN, retenuConjN

    nomN =""
    ribN =""
    cinN = ""
    delivreN =""
    dateNaissN =""
    lieuN = ""
    nationnaliteN = ""
    adresseN = ""
    codePostal =""
    professionN = ""
    employeurN = ""
    revenuN = ""
    retenuN = ""
    etatN = ""
    nomConjN = ""
    cinConjN = ""
    delivreConjN =""
    dateNaissConjN =""
    lieuConjN =""
    nationnaliteConjN = ""
    adresseConjN = ""
    professionConjN = ""
    employeurConjN = ""
    revenuConjN = ""
    retenuConjN = ""

    with open("credit.csv", 'r') as f:
        obj = csv.DictReader(f)

        for i in obj:
            if i["nom"] == str(thisnom):
                nomN = thisnom
                ribN = i["RIB"]
                cinN = i["cin"]
                delivreN = i["delivre"]
                dateNaissN = i["date"]
                lieuN = i["lieu"]
                nationnaliteN = i["nationnalite"]
                adresseN = i["adresse"]
                codePostal = i["code_postal"]
                professionN = i["profession"]
                employeurN = i["employeur"]
                revenuN = i["revenu"]
                retenuN = i["retenu"]
                etatN = i["etat_civile"]

                nomConjN = i["nom_conjoint"]
                cinConjN = i["cinConj"]
                delivreConjN = i["delivreConj"]

                dateNaissConjN = i["date_naiss_conj"]
                lieuConjN = i["lieu_conj"]
                nationnaliteConjN = i["nationnalite_conj"]
                adresseConjN = i["adresseConj"]
                professionConjN = i["profession_conj"]
                employeurConjN = i["employeur_conj"]
                revenuConjN = i["revenu_conj"]
                retenuConjN = i["retenu_conj"]
        print("par nom  ribN : " + ribN + " le nom : " + nomN + " dateNaissN : " + dateNaissN)

def rechercheParRib(thisrib):
    import csv

    global nomN, ribN, cinN, delivreN, dateNaissN, lieuN, nationnaliteN, adresseN, codePostal, professionN, employeurN
    global revenuN, retenuN, etatN, nomConjN, cinConjN, delivreConjN, dateNaissConjN, lieuConjN, nationnaliteConjN
    global adresseConjN, professionConjN, employeurConjN, revenuConjN, retenuConjN

    nomN = ""
    ribN = ""
    cinN = ""
    delivreN = ""
    dateNaissN = ""
    lieuN = ""
    nationnaliteN = ""
    adresseN = ""
    codePostal = ""
    professionN = ""
    employeurN = ""
    revenuN = ""
    retenuN = ""
    etatN = ""
    nomConjN = ""
    cinConjN = ""
    delivreConjN = ""
    dateNaissConjN = ""
    lieuConjN = ""
    nationnaliteConjN = ""
    adresseConjN = ""
    professionConjN = ""
    employeurConjN = ""
    revenuConjN = ""
    retenuConjN = ""

    with open("credit.csv", 'r') as f:
        obj = csv.DictReader(f)

        for i in obj:
            if i["RIB"] == thisrib:
                nomN = i["nom"]
                ribN = thisrib
                cinN = i["cin"]
                delivreN = i["delivre"]
                dateNaissN = i["date"]
                lieuN = i["lieu"]
                nationnaliteN = i["nationnalite"]
                adresseN = i["adresse"]
                codePostal = i["code_postal"]
                professionN = i["profession"]
                employeurN = i["employeur"]
                revenuN = i["revenu"]
                retenuN = i["retenu"]
                etatN = i["etat_civile"]

                nomConjN = i["nom_conjoint"]
                cinConjN = i["cinConj"]
                delivreConjN = i["delivreConj"]

                dateNaissConjN = i["date_naiss_conj"]
                lieuConjN = i["lieu_conj"]
                nationnaliteConjN = i["nationnalite_conj"]
                adresseConjN = i["adresseConj"]
                professionConjN = i["profession_conj"]
                employeurConjN = i["employeur_conj"]
                revenuConjN = i["revenu_conj"]
                retenuConjN = i["retenu_conj"]
        print("par rib  ribN : " + ribN + " le nom : " + nomN + "dateNaissN : " + dateNaissN)


gererProfile()
