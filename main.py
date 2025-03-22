from flask import Flask, request, jsonify
import spacy
import os
from nlp_config import MODEL_DIR, train_model

if not os.path.exists(MODEL_DIR):
    print("🔄 Modelo não encontrado. Treinando agora...")
    train_model()
else:
    print(f"✅ Modelo já existe em '{MODEL_DIR}'. Pulando treinamento.")

# Carregar o modelo treinado
nlp = spacy.load(MODEL_DIR)

# Inicializar Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de Reconhecimento de Intenções Ativa!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Texto não fornecido!"}), 400

    doc = nlp(text)
    scores = doc.cats
    predicted_intent = max(scores, key=scores.get)

    return jsonify({"intent": predicted_intent, "scores": scores})

if __name__ == "__main__":
    app.run(debug=True)