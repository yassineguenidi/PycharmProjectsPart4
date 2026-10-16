import streamlit as st
import os
from PIL import Image
import pandas as pd

def prive():
    global id
    global rib
    global typeCreditPriv

    global name
    global date
    global lieu
    global nationnalite
    global adresse
    global code
    global cin
    global delivre
    global etatPriv
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

    global cinPrivFile
    global cdiPriv
    global attestationPriv
    global justifPriv
    global domiciliationPriv
    global bulletinPriv
    global devisPriv
    global facturePriv
    global extraitPriv

    global agreePriv
    # imagePriv = Image.open(r'images\attijari.gif')
    # st.image(imagePriv, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB',
    #          output_format='auto')
    # st.title("SECTEUR PRIVE")

    typeCreditPriv = st.selectbox(
        'Quel type du credit voulez vous',
        ('CREDEX', 'TAHSSIN', 'CREDITAU', 'Rachat Externe(prospect)'))
    st.write('Vous avez choisi:', typeCreditPriv)

    rib = st.text_input("RIB", key="ribPriv")
    name = st.text_input("Nom & prenom", key="namePriv")
    date = st.text_input("Date du naissance", key="dateNaissPriv")
    lieu = st.text_input("Lieu du naissance", key="lieuPriv")
    nationnalite = st.text_input("Nationnalité", key="NationnalitePriv")
    adresse = st.text_input("Adresse", key="adressePriv")
    code = st.text_input("Code postal", key="codePriv")
    cin = st.text_input("CIN", key="cinPriv")
    delivre = st.text_input("Delivré Le", key="delivrePriv")
    etatPriv = st.selectbox(
        'Etat civil',
        ('Célibataire', 'Marie(e)', 'Divorce(e)', 'Veuf(e)'))

    st.write('Vous avez choisi:', etatPriv)

    profession = st.text_input("Profession", key="professionPriv")
    employeur = st.selectbox(
        'Votre Employeur',
        ('Ministre d\'education', 'Ministre de santé', 'Ministre d\'agriculture', 'Telecom','Fonctionnaire d\'etat','Ministre de Jeunesse & du Sport','SSC','Autre'))
    st.write('Vous avez choisi:', employeur)
    revenu = st.text_input("Revenu mensuel(Net)", key="revenuPriv")
    retenu = st.text_input("Retenu ", key="retenuPriv")

    if etatPriv == 'Marie(e)':
        st.subheader("Veuillez saisir les informations du compte joint")
        nameConj = st.text_input("Nom & prenom du conjoint(e)", key="nameconjointPriv")
        dateNaissConj = st.text_input("Date du naissance", key="dateNaissConjPriv")
        lieuConj = st.text_input("Lieu du naissance", key="lieuConjPriv")
        nationnaliteConj = st.text_input("Nationnalité", key="NationnaliteConjPriv")
        adresseConj = st.text_input("Adresse", key="adresseConjPriv")
        cinConj = st.text_input("CIN", key="cinConjPriv")
        delivreConj = st.text_input("Delivré Le", key="delivreConj")

        professionConj = st.text_input("Profession", key="professionConjPriv")
        employeurConj = st.text_input("Employeur", key="employeurConjPriv")
        revenuConj = st.text_input("Revenu mensuel(Net)", key="revenuConjPriv")
        retenuConj = st.text_input("Retenu ", key="retenuConjPriv")

    st.subheader("Demande de financement")
    montantDev = st.text_input("Montant du Devis", key="montantdevisPriv")
    montantcred = st.text_input("Montant du Crédit", key="montantcreditPriv")
    duree = st.text_input("Durée de Crédit ", key="dureecreditPriv")

    st.subheader("Documents à fournir (Tous les documents doivent être de date récente)")
    cinPrivFile = st.file_uploader("Copie du CIN", type=["pdf", "docx", "txt"])
    st.text(cinPrivFile)
    cdiPriv = st.file_uploader("Contrat de travail CDI si l'ancecienneté est inférieure à l'année",
                               type=["pdf", "docx", "txt"])
    attestationPriv = st.file_uploader(
        "Attestation de travail avec la mention \"Tutulaire\" avec la date de recrutement",
        type=["pdf", "docx", "txt"])
    justifPriv = st.file_uploader("Justificatif d'adresse Personnelle(Facture STEG/SONEDE ou certificat du residence",
                                  type=["pdf", "docx", "txt"])
    domiciliationPriv = st.file_uploader("Domiciliation salaire", type=["pdf", "docx", "txt"])
    bulletinPriv = st.file_uploader("(03) Derniers Bulletins de paie", type=["pdf", "docx", "txt"],
                                    accept_multiple_files=True)
    if typeCreditPriv == "TAHSSIN":
        st.text("Pour credit TAHSIN")
        devisPriv = st.file_uploader(
            "Devis des travaux d'aménagement avec: Date, Montant en TTC, Nom de Client, Cachet et signature du Fournisseur",
            type=["pdf", "docx", "txt"])
    if typeCreditPriv == "CREDITAU":
        st.text("Pour credit AUTO")
        facturePriv = st.file_uploader("Facture pro_forma ou promesse de vente", type=["pdf", "docx", "txt"])
    if typeCreditPriv == "Rachat Externe(prospect)":
        st.text("Pour Rachat Externe")
        extraitPriv = st.file_uploader(
            "Derniers (06) extraits de compte de la banque concoeur + tableau(x) d'amortissement+ Attestation d'engagement ",
            type=["pdf", "docx", "txt"], accept_multiple_files=True)
    # adding a checkbox
    agreePriv = st.checkbox('I agree to the given conditions.')

    if st.button('Valider'):
        if not bool(agreePriv):
            st.error("Veuillez accepter les conditions d'utilisation!")
            return False
        checkPrivate()

def checkPrivate():
    if checkAttributes():
        if checkCompteJointes():
            if checkDemandeFinancement():
                if typeCreditPriv == "CREDEX":
                    if checkFileCredex():
                        saveAttributes()
                        return True
                if typeCreditPriv == "TAHSSIN":
                    if checkFileTahssin():
                        saveAttributes()
                        return True
                if typeCreditPriv == "CREDITAU":
                    if checkFileCreditaux():
                        saveAttributes()
                        return True
                if typeCreditPriv == "Rachat Externe(prospect)":
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
    if etatPriv == 'Marie(e)':
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
    if cinPrivFile is None:
        st.text("Veuillez entrez votre copie du CIN!")
        return False
    elif cdiPriv is None:
        st.text("Veuillez entrez votre Contrat de travail CDI !")
        return False
    elif attestationPriv is None:
        st.text("Veuillez entrez votre attestation de travail !")
        return False
    elif justifPriv is None:
        st.text("Veuillez entrez votre justificatif d'adresse !")
        return False
    elif domiciliationPriv is None:
        st.text("Veuillez entrez votre domiciliation du salaire !")
        return False
    elif bulletinPriv is None:
        st.text("Veuillez entrez les (03) bulletins de paie !")
        return False
    else:
        save_uploadedfile(cinPrivFile)
        save_uploadedfile(attestationPriv)
        save_uploadedfile(justifPriv)
        save_uploadedfile(domiciliationPriv)
        save_multipleUploadedFile(bulletinPriv)
        st.success("Saved Files  to CreditFiles\\" + str(cin))
        return True

def checkFileTahssin():
    if checkFileCredex():
        if devisPriv is None:
            st.text("Veuillez entrez le devis des travaux d'amenagement!")
            return False
        else:
            save_uploadedfile(devisPriv)
            return True
    else :
        return False

def checkFileCreditaux():
    if checkFileCredex():
        if facturePriv is None:
            st.text("Veuillez entrez la facture pro_forma ou promesse de vente!")
            return False
        else:
            save_uploadedfile(facturePriv)
            return True
    else:
        return False

def checkFileRachat():
    if checkFileCredex():
        if extraitPriv is None:
            st.text("Veuillez entrez les derniers (06) extraits de compte de la banque concoeur + tableau(x) d'amortissement+ Attestation d'engagement !")
            return False
        else:
            save_multipleUploadedFile(extraitPriv)
            return True
    else:
        return False

def save_uploadedfile(uploadedfile):
    newpath = r'CreditFiles\private\\' + str(cin)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(os.path.join(newpath, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

def save_multipleUploadedFile(uploadedfiles):
    newpath = r'CreditFiles\private\\' + str(cin)
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
        {"Type": typeCreditPriv, "RIB": rib, "nom": name, "date": date, "lieu": lieu, "nationnalite": nationnalite
            , "adresse": adresse, "code_postal": code, "cin": cin, "delivre": delivre
            , "etat_civile": etatPriv, "profession": profession, "employeur": employeur
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

prive()