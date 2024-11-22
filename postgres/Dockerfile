# Usa l'immagine ufficiale di Python come base
FROM python:3.11-slim

# Imposta la cartella di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nel container
COPY requirements.txt /app/

# Installa le dipendenze necessarie
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutti i file del progetto nella cartella di lavoro del container
COPY . /app/

# Espone la porta 8000 per l'app FastAPI
EXPOSE 8000

# Comando per avviare il server FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
