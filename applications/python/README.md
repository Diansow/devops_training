# python_app

Ce projet est une application Flask simple qui peut être lancée de différentes manières : en exécutant localement avec Python et Flask, en utilisant Docker et Docker Compose ou en utilisant directement une image Docker pré-construite.

## Exécution locale

Pour exécuter l'application localement, suivez les étapes suivantes :

1. Clonez le projet en utilisant la commande :
   ```
   git clone git@github.com:Diansow/python_app.git
   ```

2. Accédez au répertoire du projet :
   ```
   cd python_app
   ```

3. Créez un environnement virtuel (venv) pour isoler les dépendances de votre système :
   ```
   python -m venv venv
   ```

4. Activez l'environnement virtuel :
   - Sur Windows :
   ```
   venv\Scripts\activate
   ```
   - Sur macOS et Linux :
   ```
   source venv/bin/activate
   ```

5. Installez les dépendances du projet à l'aide de la commande pip :
   ```
   pip install -r requirements.txt
   ```

6. Lancez l'application Flask en utilisant la commande :
   ```
   flask run
   ```

L'application Flask devrait être accessible à l'adresse `http://localhost:5000` dans votre navigateur.

## Utilisation de Docker et Docker Compose

Pour lancer l'application en utilisant Docker et Docker Compose, suivez ces étapes :

1. Clonez le projet en utilisant la commande :
   ```
   git clone git@github.com:Diansow/python_app.git
   ```

2. Accédez au répertoire du projet :
   ```
   cd python_app
   ```

3. Assurez-vous que Docker et Docker Compose sont installés sur votre système.

4. Lancez l'application à l'aide de Docker Compose en utilisant la commande :
   ```
   docker-compose up -d
   ```

L'application Flask sera accessible à l'adresse `http://localhost:5000` dans votre navigateur.

## Utilisation de l'image Docker pré-construite

Si vous souhaitez exécuter l'application sans apporter de modifications, vous pouvez utiliser directement l'image Docker pré-construite disponible sur Docker Hub :

```
docker run -it --rm -p 5000:5000 diandev/flask_app:0.0.1
```

L'application Flask sera accessible à l'adresse `http://localhost:5000` dans votre navigateur.

N'hésitez pas à explorer et à apporter des modifications à ce projet Flask selon vos besoins. Si vous avez des questions ou des problèmes, n'hésitez pas à nous contacter.
