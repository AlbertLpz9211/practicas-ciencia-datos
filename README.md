# Prácticas de Ciencia de Datos

Repositorio de scripts y notebooks desarrollados durante el curso de Ciencia de Datos. Los ejercicios van desde fundamentos de Python hasta aprendizaje automático y procesamiento de lenguaje natural, con datasets orientados al contexto agrícola y biológico de Nayarit.

---

## Estructura del repositorio

```
📁 pythonera/
├── 📓 Notebooks
│   ├── AprendizajeAutomatico.ipynb   # ML supervisado, métricas y NLP con Transformers
│   ├── Clases.ipynb                  # POO, pandas, scraping, SQL y regresión lineal
│   ├── ProcesamientoLengNat.ipynb    # NLP: sentimientos, NER y tokenización
│   ├── taller1.ipynb                 # Tipos de datos en Python
│   └── taller1-mineria.ipynb         # POO aplicada a minería de datos
│
├── 🐍 Scripts
│   ├── beautifulsoap.py              # Web scraping con BeautifulSoup
│   ├── script_db.py                  # Carga de CSV a SQLite
│   ├── tallerDiccionarios.py         # Validación de datos con diccionarios
│   ├── transformers_local.py         # Análisis de sentimientos + NER con spaCy
│   └── transformes2.py               # Análisis de sentimientos (Transformers)
│
└── 📊 Datos
    ├── datos_campo.csv               # Parcelas, cultivos y niveles de humedad
    ├── biologia_marina.csv           # Estanques: temperatura y salinidad
    ├── exportaciones.csv             # Lotes de exportación (toneladas, precio USD)
    ├── catalogo.json                 # Catálogo de productos agrícolas (Mango, Aguacate)
    └── staff.json                    # Personal de estaciones de monitoreo
```

---

## Contenido por notebook

### `AprendizajeAutomatico.ipynb`
El notebook más extenso. Cubre el flujo completo de un proyecto de ML:

- **Análisis de sentimientos** con `transformers` (HuggingFace pipeline) sobre opiniones en español
- **Supervisado vs. no supervisado** con el dataset Iris: Regresión Logística vs. KMeans
- **Clasificación de cáncer de mama** (Wisconsin Breast Cancer Dataset):
  - Preprocesamiento y escalado con `StandardScaler`
  - Matriz de confusión, precision, recall, F1-score y AUC-ROC
  - Por qué la accuracy sola es insuficiente en medicina
- **`DummyClassifier` como baseline**: demuestra que un modelo que siempre predice la clase mayoritaria puede tener 99% de accuracy en datos desbalanceados, pero recall = 0

### `Clases.ipynb`
Notebook de clases del curso, con ejemplos aplicados:

- **Tipos y errores de tipo** en Python (`str`, `int`, `float`, `bool`)
- **POO**: clase `ParcelaMango` con validación automática de humedad (0–100%) y zonas geográficas válidas
- **Pandas y NumPy**: carga de CSV, vectorización, estadísticas descriptivas
- **SQLite**: creación de tabla `monitoreo` e inserción desde CSV
- **JSON**: parsing de datos de estaciones meteorológicas
- **Web scraping**: `requests` + `BeautifulSoup` sobre `quotes.toscrape.com`; automatización con `Selenium` en Firefox
- **Regresión Lineal**: predicción de precio de casas por metros cuadrados
- **Escalado de features**: `StandardScaler` (Z-score) con datos inmobiliarios de Nayarit
- **NLP**: análisis de sentimientos con `transformers` y NER con `spaCy` (modelo `es_core_news_sm`)

### `ProcesamientoLengNat.ipynb`
Introducción práctica a NLP en español:

- **Análisis de sentimientos** con `distilbert-base-uncased-finetuned-sst-2-english` acelerado en Apple Silicon (MPS)
- **Reconocimiento de entidades (NER)** con spaCy en español
- **Tokenización y stopwords** con NLTK: `word_tokenize`, `sent_tokenize`, filtrado de palabras vacías

### `taller1-mineria.ipynb`
Transición de POO a análisis de datos:

- Clase `Alumno` con atributos académicos
- Clase `LecturaEnergia` con categorización automática (Bajo/Medio/Alto)
- Conversión de listas de objetos a `DataFrame` de pandas para análisis estadístico

---

## Scripts

| Script | Descripción |
|---|---|
| `beautifulsoap.py` | Extrae título, subtítulo y autores de `quotes.toscrape.com` |
| `script_db.py` | Lee `datos_campo.csv` y carga los registros en SQLite (`agrocorita.db`) |
| `tallerDiccionarios.py` | Valida lecturas de sensores de humedad de parcelas en Tepic, Santiago y San Blas |
| `transformers_local.py` | Clasifica sentimientos y detecta entidades en oraciones con ambigüedad léxica ("el banco") |
| `transformes2.py` | Análisis de sentimientos sobre textos académicos usando MPS (Apple Silicon) |

---

## Datasets

| Archivo | Columnas | Descripción |
|---|---|---|
| `datos_campo.csv` | `id_parcela, cultivo, humedad` | Monitoreo de humedad en parcelas de Mango, Limón, Naranja, etc. |
| `biologia_marina.csv` | `id_estanque, temperatura, salinidad_ppm` | Lecturas de 5 estanques para análisis estadístico con SciPy |
| `exportaciones.csv` | `id_lote, toneladas, precio_usd` | 50 lotes de exportación generados aleatoriamente |
| `catalogo.json` | `id_lote, tipo, calidad` | Catálogo de 50 lotes (Mango y Aguacate, calidad Premium) |
| `staff.json` | `id_est, nombre, turno` | Ingenieros responsables por estación y turno |

---

## Tecnologías utilizadas

- **Python 3.9**
- **Machine Learning**: `scikit-learn` (LogisticRegression, KMeans, DummyClassifier, métricas)
- **NLP**: `transformers` (HuggingFace), `spaCy`, `nltk`
- **Datos**: `pandas`, `numpy`, `scipy`
- **Visualización**: `matplotlib`, `seaborn`
- **Bases de datos**: `sqlite3`
- **Web scraping**: `beautifulsoup4`, `requests`, `selenium`
- **Aceleración**: Apple Silicon MPS (`torch.backends.mps`)

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/AlbertLpz9211/practicas-ciencia-datos.git
cd practicas-ciencia-datos

# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias principales
pip install pandas numpy scikit-learn matplotlib seaborn
pip install transformers torch spacy nltk
pip install beautifulsoup4 requests selenium
pip install notebook

# Descargar modelo de spaCy en español
python -m spacy download es_core_news_sm
```
