import requests
import streamlit as st
from PIL import Image



def homePage():
    # loginSection.empty();
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
    st.image(logo)

    # ---- BIENVENU ----
    with st.container():
        left_column, right_column = st.columns((4, 1))
        with left_column:
            st.title("BIENVENUE A L'AGENCE DE REMADA")
            st.subheader("Croire en vous")
        with right_column:
            st.write("##")
            if st.button("Demander un Credit"):
                st.info("Vous devez connecter !")
    # ---- CREDEX ----
    with st.container():
        st.write("---")
        st.header("NOS CREDITS")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.image(credex)
            st.image(credex2)
            # st_lottie(lottie_coding, height=300, key="coding")
            # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st.header("CREDEX")
            st.write("##")
            st.write(
                """
                - Aussitôt exprimé, aussitôt satisfait...
                - Vous êtes salarié ou retraité?  
                - Vous faites vos débuts dans le milieu professionnel?
                - Le crédit à la consommation CREDEX est la solution rapide à vos dépenses planifiées ou imprévues. 
                - Dans la limite de votre capacité de remboursement, le montant peut atteindre 10 mD. Durée de remboursement: sur 3 ans.
                """
            )
            st.subheader("Formalités rapides")
            st.write("""
                    - Copie de la CIN
                    - Document de demande du crédit rempli et signé par le client
                    - Attestation de pension (en originale) émise par un organisme public datant d’au moins un mois (pour les retraités)
                    - Attestation de travail (en originale) datant d’un mois au maximum indiquant la titularisation de la relation et son ancienneté dans la société.
                    - Les 3 derniers bulletins de paie (en originale) de date récente (pour le secteur privé) ; 1 bulletin de paie de date récente (pour le secteur public).
                    """)
        st.write("---")

    # ---- CREDITAU ----
    with st.container():
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.image(creditau1)
            st.image(creditau2)
        with right_column:
            st.header("CREDITAU")
            st.write("##")
            st.write(
                """
                - Vous êtes salariés dans une société étatique, semi-étatique ou privée... 
                - Vous exercez une profession libérale... Vous faites vos débuts dans le milieu professionnel...
                - CREDITAU est la formule de financement qui vous convient
                """
            )
            st.subheader("Montant")
            st.write("""
                    - Dans la limite de votre capacité de remboursement, le montant peut atteindre 80% du prix de la voiture avec un maximum de 50.000 Dinars.
                    """)
            st.subheader("Formalités simples")
            st.write("""
                    - Facture proforma.
                    - Domiciliation de salaire pour les salariés.
                    - Déclaration des revenus pour les professionnels libéraux (*).
                    - Assurance vie + vol et incendie.
                    - Transcription de privilège sur la carte grise de la voiture.
                        """)
        st.write("---")

        # ---- TAHSSIN ----

    # ---- TAHSSIN ----
    with st.container():
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.image(creditau1)
            st.image(creditau2)
            with right_column:
                st.header("TAHSSIN")
                st.write("##")
                st.write(
                    """
                   - Vous voulez rénover votre intérieur? Vous rêvez d'une nouvelle cuisine?
                   - Vous souhaitez installer le chauffage central?
                   - TAHSSIN est la solution adaptée à vos besoins. 
                   - TAHSSIN est un crédit de rénovation pour tous les travaux de votre intérieur.
                       """
                )
                st.subheader("Un prêt adapté")
                st.write("""
                            - 80% du coût de l’investissement pouvant atteindre 20 mD pour un compte individuel 
                            - Durée de remboursement: sur 5 ans.
                            """)
                st.subheader("Formalités simples")
                st.write("""
                            - Un simple devis des travaux à réaliser.
                            - Une domiciliation irrévocable du salaire ou de la pension ou la déclaration du revenu pour les professionnels libéraux.
                            - Une assurance vie.
                        """)

    st.write("---")
    st.header("Nos offres")

    # ---- AWLEDI ----
    with st.container():
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(awledi)
        with text_column:
            st.subheader("Epargne AWLEDI")
            st.write(
                """
                - Vous souhaitez garantir à vos enfants un cursus scolaire sans soucis financiers et assurer leur avenir?
                - Leur permettre de poursuivre des études supérieures dans les meilleurs écoles nationales ou internationales de leurs choix?
                - Faciliter leur insertion dans la vie active ? 
                - Attijari bank vous propose l''Epargne AWLEDI garanti par Attijari Assurance, une solution qui vous permet de constituer progressivement une épargne au profit de vos enfants et de faire face aux imprévus.
                """
            )
            st.markdown("[savoir plus...](https://www.attijaribank.com.tn/mobile/Fr/Epargne_AWLEDI_11_311)")

    # ---- ETRANGER ----
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(etranger)
        with text_column:
            st.subheader("Tunisiens à l´étranger")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[savoir plus...](https://www.attijaribank.com.tn/Fr/Tunisiens_a_letranger_11_10)")

    # ---- ENLIGNE ----
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(sept)
        with text_column:
            st.subheader("Espace Service Express 24h/24 - 7j/7")
            st.write(
                """
                Attijari bank met à votre disposition quatre espaces « Libre-Service Bancaire » qui vous proposent des services accessibles 24h/24 et 7j/7.
                Grâce à leurs équipements modernes en GAB et en bornes interactives, les LSB permettent d´effectuer en self-service et en toute sécurité différentes opérations bancaires telles que:
                - Les transactions de retrait et de dépôt d’espèces,
                - Les opérations de change,
                - L’édition des extraits de compte, RIB ou IBAN
                - La commande et les dépôts de chèque,
                - La recharge de cartes prépayées et de ligne GSM
                - La consultation de solde…"""
            )
            st.markdown(
                "[savoir plus...](https://www.attijaribank.com.tn/Fr/Espace_Service_Express__24h_24_-_7j_7__7_182_D528)")

    # ---- CONTACT ----
    with st.container():
        st.write("---")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
                    <form action="https://formsubmit.co/yassineguenidi99@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Votre nom" required>
                    <input type="email" name="email" placeholder="Vote email" required>
                    <textarea name="message" placeholder="Votre message içi" required></textarea>
                    <button type="submit">Envoyer</button>
                </form>
                """
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Vous avez une question?")
            st.write("##")
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.image(question)

    # ---- A PROPOS ----
    with st.container():
        st.write("---")
        st.header("A props notre agence")
        st.write("##")
        left_column, right_column = st.columns((1.5, 1.5))
        with left_column:
            st.image(logo)
        with right_column:
            """
            - Adresse Email : Remada@attijaribank.com.tn
            - Num Tel : 70640780
            - Num Fax : 70640780
            - Adresse : Place de l'independance, 3240-Remada
            """
homePage()