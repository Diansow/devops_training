# Utilisez une image Python officielle comme image de base
FROM python:3.9.10-alpine3.15

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

ENV FLASK_APP=saguitorde.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt requirements.txt

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du contenu de votre application dans le conteneur
COPY . .

# Exposez le port 5000 pour permettre l'accès à l'application Flask
EXPOSE 5000

# Définissez la commande à exécuter lorsque le conteneur démarre
CMD ["flask", "run"]
