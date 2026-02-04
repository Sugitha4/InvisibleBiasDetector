import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


def train_model():
    data = pd.read_csv("training_data.csv")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["resume_text"])
    y = data["selected"]

    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model,"trained_model.pkl")
    joblib.dump(vectorizer,"vectorizer.pkl")

    return model, vectorizer