from transformers import pipeline

def extract_entities(text):
    ner = pipeline("ner")
    entities = ner(text)
    return entities
