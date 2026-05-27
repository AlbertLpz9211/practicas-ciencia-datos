import spacy
nlp = spacy.load("es_core_news_sm")

oraciones = ["El banco esta cerca del parque",
            "El banco me dio un préstamo",
            "El banco estaba ocupado",
            ]

for oracion in oraciones:
    doc = nlp(oracion)
    print(f"\nOración: '{oracion}'")
    print(f"Tokens: {[token.text for token in doc]}")
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Entidades reconocidas: {entidades if entidades else 'Ninguna encontrada'}")