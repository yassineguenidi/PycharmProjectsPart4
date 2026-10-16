import streamlit as st
import os
from PIL import Image
import pandas as pd

def retraite():
    global id
    global rib
    global typeCreditRet

    global name
    global date
    global lieu
    global nationnalite
    global adresse
    global code
    global cin
    global delivre
    global etatRet
    global profession
    global employeur
    global revenu
    global retenu

    global nameConj
    nameConj = ""
    global dateNaissConj
    dateNaissConj = ""
    global lieuConj
    lieuConj = ""
    global nationnaliteConj
    nationnaliteConj = ""
    global adresseConj
    adresseConj = ""
    global cinConj
    cinConj = ""
    global delivreConj
    delivreConj = ""
    global professionConj
    professionConj = ""
    global employeurConj
    employeurConj = ""
    global revenuConj
    revenuConj = ""
    global retenuConj
    retenuConj = ""

    global montantDev
    global montantcred
    global duree

    global cinRetFile
    global cdiRet
    global attestationRet
    global justificatifRet
    global domiciliationRet
    global devisRet
    global factureRet

    global agreeRet
    # imageRet = Image.open(r'images\attijari.gif')
    # st.image(imageRet, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB',
    #          output_format='auto')
    # st.title("SECTEUR DU RETRAITE")

    typeCreditRet = st.selectbox(
        'Quel type du credit voulez vous',
        ('CREDEX', 'TAHSSIN', 'CREDITAU', 'Rachat Externe(prospect)'))
    st.write('Vous avez choisi:', typeCreditRet)

    rib = st.text_input("RIB", key="ribRet")
    name = st.text_input("Nom & prenom", key="nameRet")
    date = st.text_input("Date du naissance", key="dateNaissRet")
    lieu = st.text_input("Lieu du naissance", key="lieuRet")
    nationnalite = st.text_input("Nationnalité", key="NationnaliteRet")
    adresse = st.text_input("Adresse", key="adresseRet")
    code = st.text_input("Code postal", key="codeRet")
    cin = st.text_input("CIN", key="cinRet")
    delivre = st.text_input("Delivré Le", key="delivreRet")
    etatRet = st.selectbox(
        'Etat civil',
        ('Célibataire', 'Marie(e)', 'Divorce(e)', 'Veuf(e)'))

    st.write('Vous avez choisi:', etatRet)

    profession = st.text_input("Profession", key="professionRet")
    employeur = st.selectbox(
        'Votre Employeur',
        ('Ministre d\'education', 'Ministre de santé', 'Ministre d\'agriculture', 'Telecom', 'Fonctionnaire d\'etat',
         'Ministre de Jeunesse & du Sport', 'SSC', 'Autre'))
    st.write('Vous avez choisi:', employeur)
    revenu = st.text_input("Revenu mensuel(Net)", key="revenuRet")
    retenu = st.text_input("Retenu ", key="retenuRet")

    if etatRet == 'Marie(e)':
        st.subheader("Veuillez saisir les informations du compte joint")
        nameConj = st.text_input("Nom & prenom du conjoint(e)", key="nameconjointRet")
        dateNaissConj = st.text_input("Date du naissance", key="dateNaissConjRet")
        lieuConj = st.text_input("Lieu du naissance", key="lieuConjRet")
        nationnaliteConj = st.text_input("Nationnalité", key="NationnaliteConjRet")
        adresseConj = st.text_input("Adresse", key="adresseConjRet")
        cinConj = st.text_input("CIN", key="cinConjRet")
        delivreConj = st.text_input("Delivré Le", key="delivreConjRet")

        professionConj = st.text_input("Profession", key="professionConjRet")
        employeurConj = st.text_input("Employeur", key="employeurConjRet")
        revenuConj = st.text_input("Revenu mensuel(Net)", key="revenuConjRet")
        retenuConj = st.text_input("Retenu ", key="retenuConjRet")

    st.subheader("Demande de financement")
    montantDev = st.text_input("Montant du Devis", key="montantdevisRet")
    montantcred = st.text_input("Montant du Crédit", key="montantcreditRet")
    duree = st.text_input("Durée de Crédit ", key="dureecreditRet")

    st.subheader("Documents à fournir (Tous les documents doivent être de date récente)")
    cinRetFile = st.file_uploader("Copie du CIN", type=["pdf", "docx", "txt"])
    attestationRet = st.file_uploader("Attestation de pension (émise par la CNSS ou CNRPS", type=["pdf", "docx", "txt"])
    justificatifRet = st.file_uploader("Justificatif d'adresse Personnelle(Facture STEG/SONEDE ou certificat du residence",
                                 type=["pdf", "docx", "txt"])
    domiciliationRet = st.file_uploader("Domiciliation de la pension", type=["pdf", "docx", "txt"])
    if (typeCreditRet == "TAHSSIN"):
        st.text("Pour credit TAHSIN")
        devisRet = st.file_uploader(
            "Devis des travaux d'aménagement avec: Date, Montant en TTC, Nom de Client, Cachet et signature du Fournisseur",
            type=["pdf", "docx", "txt"])
    if (typeCreditRet == "CREDITAU"):
        st.text("Pour credit AUTO")
        factureRet = st.file_uploader("Facture pro_forma ou promesse de vente", type=["pdf", "docx", "txt"])

    # adding a checkbox
    agreeRet = st.checkbox('I agree to the given conditions.')

    if st.button('Valider'):
        if not bool(agreeRet):
            st.error("Veuillez accepter les conditions d'utilisation!")
            return False
        if checkRetraite():
            print("toute la check est valide")
            return True
        else:
            return False

def checkRetraite():
    if checkAttributes():
        if checkCompteJointes():
            if checkDemandeFinancement():
                if typeCreditRet == "CREDEX":
                    if checkFileCredex():
                        saveAttributes()
                        return True
                if typeCreditRet == "TAHSSIN":
                    if checkFileTahssin():
                        saveAttributes()
                        return True
                if typeCreditRet == "CREDITAU":
                    if checkFileCreditaux():
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
    if etatRet == 'Marie(e)':
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
    if cinRetFile is None:
        st.text("Veuillez entrez votre copie du CIN!")
        return False
    elif attestationRet is None:
        st.text("Veuillez entrez votre attestation de travail !")
        return False
    elif justificatifRet is None:
        st.text("Veuillez entrez votre justificatif d'adresse !")
        return False
    elif domiciliationRet is None:
        st.text("Veuillez entrez votre domiciliation du salaire !")
        return False
    else:
        save_uploadedfile(cinRetFile)
        save_uploadedfile(attestationRet)
        save_uploadedfile(justificatifRet)
        save_uploadedfile(domiciliationRet)
        st.success("Saved Files  to CreditFiles\\retraite\\" + str(cin))
        return True

def checkFileTahssin():
    if checkFileCredex():
        if devisRet is None:
            st.text("Veuillez entrez le devis des travaux d'amenagement!")
            return False
        else:
            save_uploadedfile(devisRet)
            return True
    else :
        return False

def checkFileCreditaux():
    if checkFileCredex():
        if factureRet is None:
            st.text("Veuillez entrez la facture pro_forma ou promesse de vente!")
            return False
        else:
            save_uploadedfile(factureRet)
            return True
    else:
        return False

def save_uploadedfile(uploadedfile):
    newpath = r'CreditFiles\retraite\\' + str(cin)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(os.path.join(newpath, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

def save_multipleUploadedFile(uploadedfiles):
    newpath = r'CreditFiles\retraite\\' + str(cin)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for uploadedfile in uploadedfiles:
        with open(os.path.join(newpath, uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())

def saveAttributes():

    @st.cache(allow_output_mutation=True)
    def get_data():
        return []

    get_data().append(
        {"Type": typeCreditRet, "RIB": rib, "nom": name, "date": date, "lieu": lieu, "nationnalite": nationnalite
            , "adresse": adresse, "code_postal": code, "cin": cin, "delivre": delivre
            , "etat_civile": etatRet, "profession": profession, "employeur": employeur
            , "revenu": revenu, "retenu": retenu, "nom_conjoint": nameConj, "date_naiss_conj": dateNaissConj
            , "lieu_conj": lieuConj, "nationnalite_conj": nationnaliteConj, "adresseConj": adresseConj,
         "cinConj": cinConj
            , "delivreConj": delivreConj, "profession_conj": professionConj, "employeur_conj": employeurConj,
         "revenu_conj": revenuConj
            , "retenu_conj": retenuConj, "montant_devis": montantDev, "montant_credit": montantcred, "duree": duree})
    df = pd.DataFrame(get_data())
    with open("credit.csv", "w", newline="") as file:
        df.to_csv(file, index=False)
    print("saved attributes")
