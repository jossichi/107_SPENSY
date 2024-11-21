from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BertForSequenceClassification, BertTokenizer, MarianMTModel, MarianTokenizer
import torch
import time

# Load translation model
translation_model_name = "Helsinki-NLP/opus-mt-vi-en"
tokenizer_translate = MarianTokenizer.from_pretrained(translation_model_name)
model_translate = MarianMTModel.from_pretrained(translation_model_name)

# Load classification model and tokenizer
classification_model_path = r"src/python/model"
model = BertForSequenceClassification.from_pretrained(classification_model_path)
tokenizer = BertTokenizer.from_pretrained(classification_model_path)

# Define Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Helper functions
def translate_vi_to_en(text):
    """
    Translates Vietnamese text to English using the translation model.
    """
    inputs = tokenizer_translate(text, return_tensors="pt", truncation=True)
    translated = model_translate.generate(**inputs)
    translated_text = tokenizer_translate.decode(translated[0], skip_special_tokens=True)
    return translated_text

def classify_text(text):
    """
    Classifies text sentiment using the BERT model.
    Returns the predicted class.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

@app.route('/add_comment', methods=['POST'])
def add_comment():
    """
    Receives a comment from the frontend, processes it through the AI model,
    and returns the translated text and classification result.
    """
    try:
        # Parse JSON request
        data = request.get_json()
        comment = data.get('text', None)  # Get the user's comment

        if comment:  # If comment is valid
            print(f"New Comment Received: {comment}")  # Log to console

            # Translation
            start_translate = time.time()
            translated_text = translate_vi_to_en(comment)
            end_translate = time.time()
            print(f"Translated Text: {translated_text}")
            print(f"Translation Time: {end_translate - start_translate:.2f} seconds")

            # Classification
            start_classify = time.time()
            prediction = classify_text(translated_text)
            end_classify = time.time()
            print(f"Prediction Result: {prediction}")
            print(f"Classification Time: {end_classify - start_classify:.2f} seconds")

            # Response
            return jsonify({
                "status": "success",
                "original_comment": comment,
                "translated_text": translated_text,
                "prediction": prediction,
                "translation_time": end_translate - start_translate,
                "classification_time": end_classify - start_classify
            }), 200
        else:
            print("No comment provided or empty comment received.")
            return jsonify({"status": "error", "message": "No comment provided."}), 400
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": "Invalid request."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
