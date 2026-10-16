# Inorder to access Frontend web app, Run "streamlit run Streamlit_app.py"
import streamlit
import requests
import json
        
def run():
    streamlit.title("Campus Placement Classifier")
    sl_no = streamlit.text_input("Serial Number")

    ssc_p = streamlit.slider("SSC (10th) Percentage", min_value=0.0, max_value=100.0, step=0.1)
    hsc_p = streamlit.slider("HSC (12th) Percentage", min_value=0.0, max_value=100.0, step=0.1)
    degree_p = streamlit.slider("Degree Percentage", min_value=0.0, max_value=100.0, step=0.1)
    etest_p = streamlit.slider("employability test percentage (conducted by the college)")
    mba_p = streamlit.slider("MBA percentage",min_value=0.0, max_value=100.0, step=0.1)
    gender = streamlit.selectbox("Gender", ['Male', 'Female'])
    ssc_b = streamlit.selectbox("SSC Board of Education", ['Central', 'Others'])
    hsc_b = streamlit.selectbox("HSC Board of Education", ['Central', 'Others'])
    hsc_s = streamlit.selectbox("Specialization in HSC", ['Commerce', 'Science', 'Arts'])
    degree_t = streamlit.selectbox("Under Graduation (Degree type)", ['Sci&Tech', 'Comm&Mgmt'])
    workex = streamlit.selectbox("Work Experience", ['Yes', 'No'])
    specialisation = streamlit.selectbox("Post Graduation(MBA)- Specialization", ['Mkt&HR', 'Mkt&Fin'])
    
    data = { 
        'sl_no': sl_no,
        'ssc_p': ssc_p,
        'hsc_p': hsc_p,
        'degree_p': degree_p,
        'etest_p': etest_p,
        'mba_p': mba_p,
        'gender': gender,
        'ssc_b': ssc_b,
        'hsc_b': hsc_b,
        'hsc_s': hsc_s,
        'degree_t': degree_t,
        'workex': workex,
        'specialisation': specialisation 
        }
    
    if streamlit.button("Predict"):
        # response = requests.post("http://0.0.0.0:8085/predict", json=data)
        # response = requests.post("http://127.0.0.1: 8085/predict", json=data)
        response = requests.post("http://127.0.0.1:8085/predict", json=data)

        prediction =response.text
        streamlit.success(f"The prediction from model: {prediction}")
    
if __name__ == '__main__':
    run()
