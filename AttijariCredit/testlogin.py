import streamlit as st

from database import login_user
from home import homePage
from login import loginPage

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()


def show_main_page():
    with mainSection:
        loginSection.empty()
        logOutSection.empty()
        homePage()
        # dataFile = st.text_input("Enter your Test file name: ")
        # Topics = st.text_input("Enter your Model Name: ")
        # ModelVersion = st.text_input("Enter your Model Version: ")
        # processingClicked = st.button("Start Processing", key="processing")
        # if processingClicked:
        #     st.balloons()


def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False


def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button("Log Out", key="logout", on_click=LoggedOut_Clicked)


def LoggedIn_Clicked(userName, password):
    if login_user(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False;
        st.error("Invalid user name or password")


def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            loginPage()
            # userName = st.text_input(label="5", value="5", placeholder="Enter your user name")
            # password = st.text_input(label="4", value="4", placeholder="Enter password", type="password")
            # st.button("Login", on_click=LoggedIn_Clicked, args=(userName, password))


with headerSection:
    # st.title("Streamlit Application")
    # first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_main_page()
        #show_login_page()
    else:
        if st.session_state['loggedIn']:
            show_login_page()
            # show_logout_page()
            # show_main_page()

        else:
            show_main_page()
            # show_login_page()





