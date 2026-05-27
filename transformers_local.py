import torch
from transformers import pipeline

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Usando dispositivo: {device}")

nlp = pipeline("sentiment-analysis", device=device)

textos = ["Me encanta el procesamiento del lenguaje Natural, es fascinante",
          "Esta materia me parece muy difícil y no entiendo nada",
          "El profesor muestra clases divertidas",
          "El examen estuvo mas o menos bien, aunque algunas preguntas fueron raras"]

for texto in textos:
    resultado = nlp(texto)[0]
    print(f"Texto: '{texto}'")
    print(f"Sentimiento: {resultado['label']} (Confianza: {resultado['score']:.4f})\n")
    print("-"*60)
