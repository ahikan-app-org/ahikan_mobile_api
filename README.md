# ahikan_mobile_api

Le projet backend qui mais en place l'environnement rest api pour les clients de AHIKAN
construite avec **Django et Django REST Framework**, utilisant **PostgreSQL** et **Docker**.

## 🚀 Fonctionnalités

- 🔐 **Authentification utilisateur** (`client`, `vendeur`, `admin`)
- 📄 **Gestion des utilisateurs** (CRUD)
- 📦 **Déploiement avec Docker et Docker Compose**
- ✅ **Tests automatisés**
- 🛠 **Linting avec Flake8**

---

## 🏗️ Installation et Configuration

### **1️⃣ Cloner le projet**

```sh
git clone https://github.com/ahikan-app-org/ahikan_mobile_api-api.git
cd ahikan_mobile_api
```

### **2️⃣ Lancer l'application avec Docker**

```sh
docker-compose up --build
```

Ce processus :
✅ **Crée et démarre PostgreSQL**  
✅ **Attend que la base de données soit prête**  
✅ **Applique les migrations**  
✅ **Démarre le serveur Django sur `http://localhost:8000`**

### **3️⃣ Appliquer les migrations (si nécessaire)**

```sh
docker-compose run --rm app sh -c "python manage.py migrate"
```

### **4️⃣ Créer un superutilisateur**

```sh
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

---

## 🔥 Variables d’environnement

Dans ton fichier **`docker-compose.yml`**, les variables sont définies comme suit :

```yaml
services:
  app:
    environment:
      - DB_HOST=db
      - DB_NAME=ahikan_db
      - DB_USER=admin
      - DB_PASSWORD=ahikanOrlanE2002!
      - DB_PORT=5432
```

Tu peux les modifier dans **`docker-compose.yml`** directement.

---

## 🔥 Utilisation de l'API

| Méthode | Endpoint              | Description                    |
| ------- | --------------------- | ------------------------------ |
| `POST`  | `/api/auth/login/`    | Connexion utilisateur          |
| `POST`  | `/api/auth/register/` | Inscription                    |
| `GET`   | `/api/users/`         | Liste des utilisateurs (admin) |

**Exemple d’authentification :**

```json
{
  "email": "test@example.com",
  "password": "Testpass123"
}
```

---

## 🧪 Tests & Qualité du Code

### **Exécuter les tests**

```sh
docker-compose run --rm app sh -c "python manage.py test"
```

### **Exécuter Flake8**

```sh
docker-compose run --rm app sh -c "flake8"
```

---

## 🛠 Développement

### **Activer un shell Django**

```sh
docker-compose run --rm app sh -c "python manage.py shell"
```

### **Appliquer les migrations**

```sh
docker-compose run --rm app sh -c "python manage.py makemigrations && python manage.py migrate"
```

---

## 🏁 Déploiement

### **1️⃣ Construire l'image Docker**

```sh
docker build -t ahikan-api .
```

### **2️⃣ Lancer le conteneur**

```sh
docker run -p 8000:8000 ahikan-api
```

---

## 📜 License

Projet sous licence **MIT**.

---

## 📞 Support

Si tu rencontres un problème, ouvre une **issue** sur GitHub.

```

```
