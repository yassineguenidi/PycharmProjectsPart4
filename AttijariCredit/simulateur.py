import datetime

import requests
import streamlit as st
import pandas as pd
from PIL import Image
from dateutil.relativedelta import relativedelta

from loan_prediction import pred

logo = Image.open(r'images\att.png')
st.set_page_config(page_title="AttijariCredit", page_icon=logo, layout="wide")


def simulateur():
    global nom, cin, salaire1, salaire2, salaire3, salaire4, salaire5, salaire6 , moyenne, credit,duree
    global capital, dureeCredit,tauxAnnuel
    capital=0
    dureeCredit=0
    tauxAnnuel=0.0
    nom=""
    moyenne=0
    credit=0
    duree=0
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    # ---- LOAD ASSETS ----
    # lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

    credex = Image.open(r'images\credex.png')
    credex2 = Image.open(r'images\credex2.png')
    creditau1 = Image.open(r'images\creditau1.png')
    creditau2 = Image.open(r'images\creditau2.png')
    awledi = Image.open(r'images\awledi.jpg')
    entreprise = Image.open(r'images\entreprise.jpg')
    enligne = Image.open(r'images\enligne.jpg')
    etranger = Image.open(r'images\etranger.jpg')
    recrute = Image.open(r'images\recrute.jpg')
    logo = Image.open(r'images\attijari.gif')
    sept = Image.open(r'images\septsursept.jpg')
    question = Image.open(r'images\question.jpg')


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

    # ---- DEMANDE CIN ----
    with st.container():
        st.write("---")

        left_column, mid_column, right_column = st.columns((1, 1, 1))
        with mid_column:
            st.header("Simulateur de credit")
            cin = st.text_input("Entrez votre CIN")
            rechercheParCin(cin)

    # ---- COORDONNEES ----
    with st.container():
        st.write("---")
        st.subheader("Vos coordonnées")

        left_column,mid_column, right_column = st.columns((1, 1,1))
        with left_column:
            st.write("Le Numero du RIB "+ribN)
            st.text("le nom est "+nomN)
            st.text("Date naissance " + dateNaissN)

        with mid_column:
            st.text("Profession " + professionN)
            st.text("Employeur "+ employeurN)
            st.text("Position "+ positionN)
        with right_column:
            st.text("Etat Civile "+etatN)

    # ---- SALAIRES ----
    with st.container():
        st.write("---")
        st.subheader("Votre salaires")
        first_column, second_column ,third_column,fourth_column,fifth_column,= st.columns((0.5,0.5,0.5,0.5, 1))
        with first_column:
            salaire1=st.number_input("Mois-6",min_value=0)
            salaire2=st.number_input("Mois-5",min_value=0)
        with second_column:
            salaire3=st.number_input("Mois-4",min_value=0)
            salaire4=st.number_input("Mois-3",min_value=0)
            st.text("Votre salaire moyen :")
        with third_column:
            salaire5=st.number_input("Mois-2",min_value=0)
            salaire6=st.number_input("Mois-1",min_value=0)
            st.write(calculmediane())

        with fourth_column:
            st.empty()
        with fifth_column:
            st.empty()

    # ---- CAPACITE DE REMBOURCEMENT ----
    with st.container():
        st.write("---")
        st.subheader("Capacité de rembourcement")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            calculRembourcement()
            st.text("Max Credit "+ str(maxCredit))
            credit = st.number_input("Credit Demandé",min_value=0,max_value=50000)
            duree = st.number_input("Durée (En années)",min_value=0.0 ,max_value=100.0)
            st.text("TMM : "+str(tmm))
            st.text("Commission : "+ str(comm))
            st.text("Taux : "+ str(taux))

            if st.button("valider"):
                checkAtt()

        with right_column:
            st.empty()

    #----CARACTERISTIQUES DE CREDIT----
    with st.container():
        if checkAtt():
            st.write("---")

            first_column, second_column, third_column = st.columns((2, 1, 2))
            with first_column:
                st.subheader("CARACTERISTIQUES DE CREDIT")
                st.text("Capital Emprunté :" + str(credit))
                st.text("Duree de Rembourcement :" + str(duree * 12))
                st.text("Date " + str(datetime.date.today()))
                st.text("Capital Emprunté " + str(margeinteret))
            with second_column:

                st.empty()

            with third_column:
                st.subheader("TABLEAU D'AMORTISSEMENT")
                tableauAmortissement(credit,margeinteret,duree) 
        else :
            st.empty()

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            if st.button("valider2"):
                revapp= float(AppN)
                revCoApp = float(coAppN)
                # duree
                if (pred(revapp, int(duree), revCoApp, 1.0) == 1):
                # if (pred(revapp, int(duree), revCoApp, 1.0) == 1):
                    st.text("felicitation vous etes eligible au credit")
                else:
                    st.text("Desolé vous n'etes pas eligible au credit")
        with text_column:
            st.empty()

    # ---- ENLIGNE ----
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.empty()
        with text_column:
            st.empty()

    # ---- CONTACT ----

def rechercheParCin(thiscin):
    import csv
    global nomN, dateNaissN, professionN, adresseN, ribN, etatN,typeCreditN,employeurN,positionN,coAppN,AppN
    nomN = ""
    positionN=""
    employeurN=""
    professionN = ""
    adresseN = ""
    dateNaissN = ""
    ribN = ""
    etatN = ""
    typeCreditN=""
    coAppN=""
    AppN=""
    with open("credit.csv", 'r') as f:
        obj = csv.DictReader(f)

        for i in obj:
            if i["cin"]==thiscin:

                positionN="Titulaire"
                typeCreditN=i["Type"]
                nomN=i["nom"]
                dateNaissN = i["date"]
                professionN = i["profession"]
                employeurN = i["employeur"]
                adresseN = i["adresse"]
                ribN = i["RIB"]
                etatN=i["etat_civile"]
                coAppN=i["revenu_conj"]
                AppN=i["revenu"]
                print("ribN : "+ ribN +" le nom : "+nomN ," Type de Credit "+ typeCreditN , "dateNaissN : "+dateNaissN +" Employeur : " + employeurN +" professionN : " +
                      professionN + " adresseN : "+adresseN +"revenu appliqué "+ AppN +"revenu Conjoint "+ coAppN  )

def calculmediane():
    import statistics

    lst = [salaire1 , salaire2 , salaire3 , salaire4 , salaire5  , salaire6]

    return statistics.median(lst)

def calculRembourcement():

    global  tmm, comm, taux, maxCredit,margeinteret
    maxCredit=""
    tmm=7.02
    comm= 2.0
    taux=tmm+ 5
    margeinteret=comm+taux

    if employeurN=="Ministre d\'education" :
        comm = 1
        taux = tmm + 3
        margeinteret = comm + taux
    if employeurN=="Ministre de santé" :
        comm = 1
        taux = tmm + 2.75
        margeinteret = comm + taux
    if employeurN=="Ministre d\'agriculture" :
        comm = 1
        taux = tmm + 2.5
        margeinteret = comm + taux
    if employeurN=="Telecom" :
        comm = 0.5
        taux = tmm + 2
        margeinteret = comm + taux
    if employeurN=="Fonctionnaire d\'etat" :
        comm = 2
        taux = tmm + 5
        margeinteret = comm + taux
    if employeurN=="Ministre de Jeunesse & du Sport" :
        comm = 1
        taux = tmm + 2.6
        margeinteret = comm + taux
    if employeurN=="SSC" :
        comm = 1.5
        taux = tmm + 3
        margeinteret = comm + taux

    if typeCreditN=="CREDEX":
        maxCredit=10000
    if typeCreditN=="TAHSSIN":
        maxCredit=20000
    if typeCreditN=="CREDITAU":
        maxCredit=50000

def checkAtt():
    if credit != 0 and duree !=0 :
        if credit > maxCredit:
            st.warning("le credit ne doit pas depasser " + str(maxCredit))
            return False
        if typeCreditN == "CREDEX":
            if duree > 36:
                st.warning("la duree de rembourcement ne doit pas depasser 36 mois!")
                return False

        if typeCreditN == "TAHSSIN":
            if duree > 36:
                st.warning("la duree de rembourcement ne doit pas depasser 60 mois!")
                return False

        if typeCreditN == "CREDITAU":
            if duree > 36:
                st.warning("la duree de rembourcement ne doit pas depasser 84 mois!")
                return False
    return  True

def calculecheance(capital, tauxAnnuel, dureeCredit):
    if capital*tauxAnnuel*dureeCredit != 0:
        import math
        tauxMensuel=(tauxAnnuel*0.01)/12
        nbEcheance=dureeCredit*12
        a= capital * tauxMensuel*math.pow(1+tauxMensuel,nbEcheance)
        b=math.pow(1+tauxMensuel,nbEcheance)-1
        return round(a/b,2)

def calculTauxInteret(capital,tauxAnnuel):
    if (capital*tauxAnnuel)!=0:
        return capital * ((tauxAnnuel*0.01)/12)

def tableauAmortissement(capital,tauxAnnuel, dureeCredit):
    if checkAtt() and (capital * tauxAnnuel * dureeCredit)!=0:
        date = datetime.date.today()
        No = 1
        restant = capital
        interet = calculTauxInteret(capital, tauxAnnuel)
        echeance = calculecheance(capital, tauxAnnuel, dureeCredit)
        principal = echeance - interet

        @st.cache(allow_output_mutation=True)
        def get_data():
            return []

        get_data().clear()
        while (No <= dureeCredit * 12):
            get_data().append(
                {"Date": date,
                 "No": No,
                 "Restant": restant,
                 "Interet": interet,
                 "Principal": principal,
                 "Echeance": echeance})
            print(" Date : " + str(date)
                  + " No : " + str(No)
                  + " Restant dû : " + str(restant)
                  + " Interet : " + str(interet)
                  + " Principal : " + str(principal)
                  + " Echeance : " + str(echeance))
            date = date + relativedelta(months=1)
            No += 1
            restant = restant - principal
            interet = calculTauxInteret(restant, tauxAnnuel)
            principal = echeance - interet
        df = pd.DataFrame(get_data())
        st.dataframe(df)

# print(calculecheance(200000,1.92,20))
# print(calculTauxInteret(200000,1.92))
# # print(datetime.date.today()+ relativedelta(months=1))
# # rechercheParCin("77777777")
# tableauAmortissement(200000,1.92,20)

simulateur()