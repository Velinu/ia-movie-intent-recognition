import spacy
import os
from spacy.training import Example
from train_data import TRAIN_DATA_EN, TRAIN_DATA_PT

MODEL_DIR = "intent_movies_model"

def train_model():
    nlp = spacy.blank("xx")  # Criar modelo multilíngue

    textcat = nlp.add_pipe("textcat")

    labels = ["Predator", "RoboCop", "Terminator", "Alien", "Rambo"]
    for label in labels:
        textcat.add_label(label)

    nlp.begin_training()

    TRAIN_DATA = TRAIN_DATA_EN + TRAIN_DATA_PT

    for epoch in range(10):
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, losses=losses)
        print(f"Época {epoch+1}: Perda = {losses}")

    nlp.to_disk(MODEL_DIR)
    print(f"✅ Modelo treinado e salvo em '{MODEL_DIR}'!")

