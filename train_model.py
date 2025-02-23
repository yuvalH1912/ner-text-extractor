import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import random

def load_data():
    from prepare_data import TRAIN_DATA  # Ensure this imports your training data correctly
    return TRAIN_DATA

def train_ner(TRAIN_DATA):
    nlp = spacy.blank('en')  # Create a blank English model
    if 'ner' not in nlp.pipe_names:
        ner = nlp.add_pipe('ner', last=True)

    # Add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations['entities']:
            ner.add_label(ent[2])

    # Begin training
    nlp.begin_training()
    for itn in range(100):  # Set the number of training iterations
        random.shuffle(TRAIN_DATA)
        losses = {}

        # Batch up the examples using spaCy's minibatch
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                examples.append(example)
            nlp.update(examples, drop=0.5, losses=losses)
        print(f"Losses at iteration {itn}: {losses}")

    # Save the trained model to a directory
    model_dir = "C:/Users/97252/PycharmProjects/AppTextReader/model"
    nlp.to_disk(model_dir)
    print(f"Model saved to {model_dir}")

if __name__ == "__main__":
    TRAIN_DATA = load_data()
    train_ner(TRAIN_DATA)
