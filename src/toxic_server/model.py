from transformers import pipeline

classifier = pipeline("text-classification", model="unitary/toxic-bert")


def predict(text):
    return classifier(text)[0]["score"] >= 0.5
