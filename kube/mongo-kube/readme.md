# README

Ce référentiel contient des fichiers YAML pour le déploiement d'applications avec Kubernetes.

## Fichiers YAML

### mongo-configmap.yml

Ce fichier définit un ConfigMap pour Mongo Express contenant une variable `databaseurl`.

### mongo-secret.yml

Ce fichier définit un Secret pour Mongo Express contenant des informations d'authentification (`basic_auth_username` et `basic_auth_password`).

### mongo-deployment.yml

Ce fichier spécifie le déploiement d'une instance MongoDB avec un conteneur utilisant l'image `mongo:7.0.3`. Il inclut également un service associé.

### mongo-express-deployment.yml

Ce fichier spécifie le déploiement d'une instance Mongo Express avec des variables d'environnement provenant d'un ConfigMap et d'un Secret. Il inclut également un service de type LoadBalancer.

## Comment utiliser

1. Assurez-vous que Kubernetes est installé et configuré sur votre cluster.
2. Appliquez ces fichiers YAML en utilisant la commande `kubectl apply -f [nom-du-fichier.yml]`.
   - Par exemple, pour appliquer le fichier `mongo-configmap.yml`, utilisez `kubectl apply -f mongo-configmap.yml`.
3. Vérifiez le statut des déploiements et services avec `kubectl get deployments` et `kubectl get services`.
4. Accédez à l'application Mongo Express via le service exposé. Utilisez les informations d'authentification du Secret lors de la connexion.

N'oubliez pas d'adapter ces fichiers selon vos besoins, en particulier en ce qui concerne les informations sensibles dans les Secrets.

---

**Note :** Ces fichiers sont fournis à des fins éducatives et doivent être adaptés à des environnements de production en suivant les meilleures pratiques en matière de sécurité.