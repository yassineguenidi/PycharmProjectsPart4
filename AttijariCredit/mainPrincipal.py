import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import streamlit as st

def mainPrincip():

    image = Image.open(r'images\attijari.gif')
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
    st.title("Demander un credit")
    image1 = Image.open(r'images\credit1.jpg')
    image2 = Image.open(r'images\recrute.jpg')
    images = [image1, image2]
    st.image(images, use_column_width=True, caption=["some generic text"] * len(images))