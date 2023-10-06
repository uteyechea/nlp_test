from flask import Flask, request, jsonify
import spacy

# Inicializa una nueva aplicación Flask
app = Flask(__name__)

# Carga el modelo pequeño de SpaCy para español
nlp = spacy.load("es_core_news_sm")

# Define una ruta con el método POST para reconocer entidades
@app.route('/', methods=['POST'])
def recognize_entities():
    # Obtiene la lista de oraciones del payload JSON
    sentences = request.json.get('sentences')

    # Verifica si se proporcionó una lista de oraciones
    if not sentences or not isinstance(sentences, list):
        return jsonify({'error': 'No se proporcionó una lista de oraciones'}), 400

    results = []

    # Recorre cada oración y reconoce las entidades
    for sentence in sentences:
        doc = nlp(sentence)
        entities = {ent.text: ent.label_ for ent in doc.ents}
        results.append({'oración': sentence, 'entidades': entities})

    # Devuelve los resultados en formato JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
    
