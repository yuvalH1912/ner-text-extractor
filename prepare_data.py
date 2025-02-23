import spacy
import json

# Path to your JSONL file
file_path = "C:/Users/97252/PycharmProjects/AppTextReader/admin.jsonl"

# Load the data
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))



# Prepare the training data
TRAIN_DATA = []
for entry in data:
    entities = []
    text = entry['text']
    for label in entry['label']:  # Corrected from 'annotations' to 'label'
        start, end, label_name = label  # Assumes label is a list with [start, end, label_name]
        entities.append((start, end, label_name))
    TRAIN_DATA.append((text, {'entities': entities}))

# Print the converted data to check
print(TRAIN_DATA[8:15])
