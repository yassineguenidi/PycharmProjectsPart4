import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def public():

    from PIL import Image
    import streamlit as st
    global id

    global rib
    global typeCreditPub

    global name
    global date
    global lieu
    global nationnalite
    global adresse
    global code
    global cin
    global delivre
    global etatPub
    global profession
    global employeur
    global revenu
    global retenu

    global nameConj
    nameConj=""
    global dateNaissConj
    dateNaissConj=""
    global lieuConj
    lieuConj=""
    global nationnaliteConj
    nationnaliteConj=""
    global adresseConj
    adresseConj=""
    global cinConj
    cinConj=""
    global delivreConj
    delivreConj=""
    global professionConj
    professionConj=""
    global employeurConj
    employeurConj=""
    global revenuConj
    revenuConj=""
    global retenuConj
    retenuConj=""

    global montantDev
    global montantcred
    global duree

    global cinPubFile
    global cdiPub
    global attestationPub
    global justificatifPub
    global domiciliationPub
    global bulletinPub
    global devisPub
    global facturePub
    global extraitPub

    global agreePub
    # imagePub = Image.open(r'attijari.gif')
    # st.image(imagePub, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
    # st.title("SECTEUR PUBLIC")

    typeCreditPub = st.selectbox(
        'Quel type du credit voulez vous',
        ('CREDEX', 'TAHSSIN', 'CREDITAU', 'Rachat Externe(prospect)'))
    st.write('Vous avez choisi:', typeCreditPub)

    rib=st.text_input("RIB", key="ribPub")
    name=st.text_input("Nom & prenom", key="namePub")
    date=st.text_input("Date du naissance", key="dateNaissPub")
    lieu=st.text_input("Lieu du naissance", key="lieuPub")
    nationnalite=st.text_input("Nationnalité", key="NationnalitePub")
    adresse=st.text_input("Adresse", key="adressePub")
    code=st.text_input("Code postal", key="codePub")
    cin=st.text_input("CIN", key="cinPub")
    delivre = st.text_input("Delivré Le", key="delivrePub")
    etatPub = st.selectbox(
        'Etat civil',
        ('Célibataire', 'Marie(e)', 'Divorce(e)', 'Veuf(e)'))

    st.write('Vous avez choisi:', etatPub)

    profession=st.text_input("Profession", key="professionPub")
    employeur = st.selectbox(
        'Votre Employeur',
        ('Ministre d\'education', 'Ministre de santé', 'Ministre d\'agriculture', 'Telecom', 'Fonctionnaire d\'etat',
         'Ministre de Jeunesse & du Sport', 'SSC', 'Autre'))
    st.write('Vous avez choisi:', employeur)
    revenu=st.text_input("Revenu mensuel(Net)", key="revenuPub")
    retenu=st.text_input("Retenu ", key="retenuPub")

    if etatPub== 'Marie(e)':
        st.subheader("Veuillez saisir les informations du compte joint")
        #st.text("============================================================================================")
        nameConj=st.text_input("Nom & prenom du conjoint(e)", key="nameconjointPub")
        dateNaissConj=st.text_input("Date du naissance", key="dateNaissConjPub")
        lieuConj=st.text_input("Lieu du naissance", key="lieuConjPub")
        nationnaliteConj=st.text_input("Nationnalité", key="NationnaliteConjPub")
        adresseConj=st.text_input("Adresse", key="adresseConjPub")
        cinConj=st.text_input("CIN", key="cinConjPub")
        delivreConj = st.text_input("Delivré Le", key="delivreConjPub")

        professionConj=st.text_input("Profession", key="professionConjPub")
        employeurConj=st.text_input("Employeur", key="employeurConjPub")
        revenuConj=st.text_input("Revenu mensuel(Net)", key="revenuConjPub")
        retenuConj=st.text_input("Retenu ", key="retenuConjPub")

    st.subheader("Demande de financement")
    montantDev=st.text_input("Montant du Devis", key="montantdevisPub")
    montantcred=st.text_input("Montant du Crédit", key="montantcreditPub")
    duree=st.text_input("Durée de Crédit ", key="dureecreditPub")

    st.subheader("Documents à fournir (Tous les documents doivent être de date récente)")
    cinPubFile = st.file_uploader("Copie du CIN", type=["pdf", "docx", "txt"])
    bulletinPub = st.file_uploader("Dernier Bulletin de paie", type=["pdf", "docx", "txt"])
    attestationPub = st.file_uploader("Attestation de travail avec la mention \"Tutulaire\"",
                                      type=["pdf", "docx", "txt"])
    justificatifPub = st.file_uploader(
        "Justificatif d'adresse Personnelle(Facture STEG/SONEDE ou certificat du residence",
        type=["pdf", "docx", "txt"])
    domiciliationPub = st.file_uploader("Domiciliation salaire", type=["pdf", "docx", "txt"])
    if (typeCreditPub == "TAHSSIN"):
        st.text("Pour credit TAHSIN")
        devisPub = st.file_uploader(
            "Devis des travaux d'aménagement avec: Date, Montant en TTC, Nom de Client, Cachet et signature du Fournisseur",
            type=["pdf", "docx", "txt"])
    if (typeCreditPub == "CREDITAU"):
        st.text("Pour credit AUTO")
        facturePub = st.file_uploader("Facture pro_forma ou promesse de vente", type=["pdf", "docx", "txt"])
    if (typeCreditPub == "Rachat Externe(prospect)"):
        st.text("Pour Rachat Externe")
        extraitPub = st.file_uploader(
            "Derniers (06) extraits de compte de la banque concoeur + tableau(x) d'amortissement+ Attestation d'engagement ",
            type=["pdf", "docx", "txt"])

    # adding a checkbox
    agreePub = st.checkbox('I agree to the given conditions.')

    if st.button('Valider'):
        if not bool(agreePub):
            st.error("Veuillez accepter les conditions d'utilisation!")
            return False
        checkPublic()

def checkPublic():
    if checkAttributes():
        if checkCompteJointes():
            if checkDemandeFinancement():
                if typeCreditPub == "CREDEX":
                    if checkFileCredex():
                        saveAttributes()
                        return True
                if typeCreditPub == "TAHSSIN":
                    if checkFileTahssin():
                        saveAttributes()
                        return True
                if typeCreditPub == "CREDITAU":
                    if checkFileCreditaux():
                        saveAttributes()
                        return True
                if typeCreditPub == "Rachat Externe(prospect)":
                    if checkFileRachat():
                        saveAttributes()
                        return True
    return False

def checkAttributes():
    if not bool(rib):
        st.text("Veuillez saisir votre RIB correctement!")
        return False
    elif not bool(name):
        st.text("Veuillez saisir votre nom !")
        return False
    elif not bool(date):
        st.text("Veuillez saisir votre date du naissance !")
        return False
    elif not bool(lieu):
        st.text("Veuillez saisir votre lieu du naissance !")
        return False
    elif not bool(nationnalite):
        st.text("Veuillez saisir votre nationnalité !")
        return False
    elif not bool(adresse):
        st.text("Veuillez saisir votre adresse !")
        return False
    elif not bool(code):
        st.text("Veuillez saisir votre code postal !")
        return False
    elif bool(cin) == False or len(cin) != 8:
        st.text("Veuillez saisir votre CIN correctement !")
        return False
    elif not bool(delivre):
        st.text("Veuillez saisir la date de livraison du CIN !")
        return False
    elif not bool(profession):
        st.text("Veuillez saisir votre profession !")
        return False
    elif not bool(employeur):
        st.text("Veuillez saisir votre employeur !")
        return False
    elif not bool(revenu):
        st.text("Veuillez saisir votre revenu !")
        return False
    elif not bool(retenu):
        st.text("Veuillez saisir votre retenu !")
        return False
    else:
        print("valide attributes check")
        return True

def checkCompteJointes():
    if etatPub == 'Marie(e)':
        if not bool(nameConj):
            st.text("Veuillez saisir le nom du conjoint!")
            return False
        elif not bool(dateNaissConj):
            st.text("Veuillez saisir votre date du naissance du conjoint !")
            return False
        elif not bool(lieuConj):
            st.text("Veuillez saisir votre lieu du naissance du conjoint!")
            return False
        elif not bool(nationnaliteConj):
            st.text("Veuillez saisir votre nationnalité !")
            return False
        elif not bool(adresseConj):
            st.text("Veuillez saisir votre adresse !")
            return False
        elif bool(cinConj) == False or len(cin) != 8:
            st.text("Veuillez saisir la CIN du conjoint correctement !")
            return False
        elif not bool(delivreConj):
            st.text("Veuillez saisir la date de livraison du CIN !")
            return False
        elif not bool(professionConj):
            st.text("Veuillez saisir votre profession !")
            return False
        elif not bool(employeurConj):
            st.text("Veuillez saisir votre employeur !")
            return False
        elif not bool(revenuConj):
            st.text("Veuillez saisir votre revenu !")
            return False
        elif not bool(retenuConj):
            st.text("Veuillez saisir votre retenu !")
            return False
        else:
            print("check conjointe valide")
            return True
    return True

def checkDemandeFinancement():
    if not bool(montantDev):
        st.text("Veuillez saisir votre montant du Devis !")
        return False
    elif not bool(montantcred):
        st.text("Veuillez saisir votre montant du crédit !")
        return False
    elif not bool(duree):
        st.text("Veuillez saisir votre durée d crédit !")
        return False
    else:
        print("chech demande financement valide")
        return True

def checkFileCredex():
    if cinPubFile is None:
        st.text("Veuillez entrez votre copie du CIN!")
        return False
    # elif cdiPub is None:
    #     st.text("Veuillez entrez votre Contrat de travail CDI !")
    #     return False
    elif attestationPub is None:
        st.text("Veuillez entrez votre attestation de travail !")
        return False
    elif justificatifPub is None:
        st.text("Veuillez entrez votre justificatif d'adresse !")
        return False
    elif domiciliationPub is None:
        st.text("Veuillez entrez votre domiciliation du salaire !")
        return False
    elif bulletinPub is None:
        st.text("Veuillez entrez les (03) bulletins de paie !")
        return False
    else:
        save_uploadedfile(cinPubFile)
        save_uploadedfile(attestationPub)
        save_uploadedfile(justificatifPub)
        save_uploadedfile(domiciliationPub)
        save_multipleUploadedFile(bulletinPub)
        st.success("Saved Files  to CreditFiles\\" + str(cin))
        return True

def checkFileTahssin():
    if checkFileCredex():
        if devisPub is None:
            st.text("Veuillez entrez le devis des travaux d'amenagement!")
            return False
        else:
            save_uploadedfile(devisPub)
            return True
    else :
        return False

def checkFileCreditaux():
    if checkFileCredex():
        if facturePub is None:
            st.text("Veuillez entrez la facture pro_forma ou promesse de vente!")
            return False
        else:
            save_uploadedfile(facturePub)
            return True
    else:
        return False

def checkFileRachat() :
    if checkFileCredex():
        if extraitPub is None:
            st.text("Veuillez entrez les derniers (06) extraits de compte de la banque concoeur + tableau(x) d'amortissement+ Attestation d'engagement !")
            return False
        else:
            save_multipleUploadedFile(extraitPub)
            return True
    else:
        return False

def save_uploadedfile(uploadedfile):
    newpath = r'CreditFiles\public\\' + str(cin)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(os.path.join(newpath, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

def save_multipleUploadedFile(uploadedfiles):
    newpath = r'CreditFiles\public\\' + str(cin)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for uploadedfile in uploadedfiles:
        with open(os.path.join(newpath, uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())

def saveAttributes():
    @st.cache(allow_output_mutation=True)
    def get_data():
        return []
    get_data().append({"Type": typeCreditPub, "RIB": rib, "nom": name, "date": date, "lieu": lieu, "nationnalite": nationnalite
                             , "adresse": adresse, "code_postal": code, "cin": cin, "delivre": delivre
                             , "etat_civile": etatPub, "profession": profession, "employeur": employeur
                             , "revenu": revenu, "retenu": retenu ,"nom_conjoint": nameConj, "date_naiss_conj": dateNaissConj
                             , "lieu_conj": lieuConj, "nationnalite_conj": nationnaliteConj, "adresseConj": adresseConj, "cinConj": cinConj
                             , "delivreConj": delivreConj, "profession_conj": professionConj, "employeur_conj": employeurConj, "revenu_conj": revenuConj
                             , "retenu_conj": retenuConj, "montant_devis": montantDev, "montant_credit": montantcred, "duree": duree})
    df = pd.DataFrame(get_data())
    with open("credit.csv", "w", newline="") as file:
        df.to_csv(file, index=False)
    print("saved")
public()