from bs4 import BeautifulSoup
import requests
url = "https://quotes.toscrape.com/"
#url = "http://127.0.0.1:5500/"
respuesta = requests.get(url)
print(respuesta.content)

sopa = BeautifulSoup(respuesta.content, 'html.parser')
# 1.- buscamos solo un elemento (El titulo del sitio)
titulo = sopa.find('h1').get_text(strip=True)
print(f"Titulo del sitio: {titulo}")

titulo2 = sopa.find('h2').get_text(strip=True)
print(f"Subtitulo del sitio: {titulo2}")
#2 Buscamos multiples elementos (Todas las citas)
citas = sopa.find_all('small', class_='author')
print("\n--- Autores Encontrados ---")
for i, cita in enumerate(citas, 1):
    print(f"{i}. {cita.get_text(strip=True)}")