from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

spacy.cli.download("it_core_news_sm")
nlp = spacy.load("it_core_news_sm")
print(nlp._path)

@app.route('/lemmatize', methods=['POST'])
def lemmatize_word():
    data = request.get_json()
    word = data.get("word", "")

    if not word:
        return jsonify({"error": "No word provided"}), 400
    doc = nlp(word)
    lemmatized_word = doc[0].lemma_
    return jsonify({"original": word, "lemmatized": lemmatized_word})

if __name__ == '__main__':
    app.run(debug=True)
