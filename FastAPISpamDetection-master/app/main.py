import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI

app = FastAPI()

model = joblib.load('spam_classifier.joblib')

def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text

def classify_message(model, message):

	message = preprocessor(message)
	label = model.predict([message])[0]
	spam_prob = model.predict_proba([message])

	return {'label': label, 'spam_probability': spam_prob[0][1]}

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"Hello": "Spam Classification"}

# Define a route for the "/classify" endpoint accepting POST requests
@app.post("/classify")
async def classify_api(message: str):
    result = classify_message(message)
    return result