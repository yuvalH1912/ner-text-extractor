from flask import Flask, render_template, request
import spacy

nlp = spacy.load('en_core_web_sm')


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text']
        doc = nlp(text_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return render_template('index.html', entities=entities, input_text=text_input)
    return render_template('index.html', entities=None, input_text=None)


if __name__ == '__main__':
    app.run(debug=True)
