from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

spacy.cli.download("it_core_news_sm")
nlp = spacy.load("it_core_news_sm")
print(nlp._path)

@app.route('/lemmatize', methods=['POST'])
def lemmatize_word():
    data = request.get_json()
    if data is None:
        return jsonify({"lemmatized_words": []})
    
    if "word" not in data:
        return jsonify({"lemmatized_words": []})
    
    word = data.get("word", "")
    
    if word == "":
        return jsonify({"lemmatized_words": []})
    
    words = word.split(" ")
    lemmatized_words = []
    
    if len(words) == 0:
        return jsonify({"lemmatized_words": lemmatized_words})
    
    for word in words:
        doc = nlp(word)
        for token in doc:
            lemmatized_words.append(token.lemma_)
    return jsonify({"lemmatized_words": lemmatized_words})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
    
