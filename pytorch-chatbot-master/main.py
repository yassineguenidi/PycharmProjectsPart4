"""
Importing libraries: The first few lines of the code import required libraries such as NumPy,
Streamlit, Random, JSON, and PyTorch.
"""
import numpy as np
import streamlit as st
import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

"""
load_data() reads a JSON file named "intents.json" that contains the intents of the chatbot. 
It also loads a pre-trained model and retrieves important information about the model, 
such as input size, hidden size, output size, all words, and tags. 
It returns all this information to the calling function.
"""
def load_data():
    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']

    return intents, input_size, hidden_size, output_size, all_words, tags

"""
load_model() loads the pre-trained model state into a new instance of the NeuralNet class 
defined in the model.py file. 
It returns the loaded model instance.
"""
def load_model(input_size, hidden_size, output_size, model_state):
    model = NeuralNet(input_size, hidden_size, output_size)
    model.load_state_dict(model_state)
    model.eval()
    return model

"""
Defining the main function: The main() function is defined, which is the main entry point for the application.
"""
def main():
    # Streamlit's set_page_config() function is called to set the page title, icon, and layout for the web page.
    st.set_page_config(page_title="ChatBot", page_icon=":guardsman:", layout="wide")
    st.title("Chat with ChatBot")

    # Load the data and the model
    intents, input_size, hidden_size, output_size, all_words, tags = load_data()
    model_state = torch.load("data.pth")["model_state"]
    model = load_model(input_size, hidden_size, output_size, model_state)

    # Create a text input for user input
    user_input = st.text_input("You:", "")

    if user_input:
        if user_input.lower() == "quit":
            st.stop()

        sentence = tokenize(user_input)
        X = bag_of_words(sentence, all_words)
        X = np.array(X, dtype=np.float32).reshape(1, -1)
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.65:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    response = random.choice(intent['responses'])
                    st.text_area("ChatBot:", response)

# Calling the main function: Finally, the main() function is called to start the application.
main()