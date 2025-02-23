import spacy

# Path where the model is saved
model_dir = "C:/Users/97252/PycharmProjects/AppTextReader/model"
nlp = spacy.load(model_dir)

# Use the model
text = """Hi Inbal

My name is Yuval Hadad, and I’m reaching out because I’m very interested in the Computer Vision Engineer position at Riverside.fm.

I hold a master degree in Electrical Engineering from Ben Gurion University, where my research focuses on radar signals classification using deep learning and adversarial attacks.
I have developed practical deep learning models, including modifying existing neural networks to incorporate additional features, semi-supervised segmentation models, and super-resolution techniques for cardiac ultrasound imaging.
Professionally, I have worked on image acquisition optimization and computer vision-based analysis at Applied Materials.

I would love the opportunity to learn more about UVeye’s work and discuss how my expertise in Python, PyTorch, TensorFlow, and computer vision algorithms could contribute to your team.
I would like to send you my resume 

Looking forward to hearing from you

Best regards,
Yuval Hadad
"""


# Process the text with the trained model
doc = nlp(text)

# Print out extracted entities
print("\nExtracted Entities:\n")
for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")

