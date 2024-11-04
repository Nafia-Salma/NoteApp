# Application de Gestion de Notes

Cette application est une application web fullstack conçue pour gérer des notes personnelles avec une expérience utilisateur immersive. L'application permet aux utilisateurs de créer, modifier, supprimer et afficher des notes, avec la possibilité d'ajouter des tags pour une meilleure organisation. L'authentification est mise en œuvre avec JWT, garantissant l'accès sécurisé et privé à l'application.

## Table des Matières

1. [Aperçu du Projet](#aperçu-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Conception et UX](#conception-et-ux)
4. [Documentation de l'API](#documentation-de-lapi)
5. [Instructions d'Installation](#instructions-dinstallation)
6. [Exécution de l'Application](#exécution-de-lapplication)

---

### Aperçu du Projet

Ce projet est une application de prise de notes développée avec Django (backend) et React (frontend). L'objectif principal de l'application est d'offrir une expérience utilisateur fluide et intuitive. Les utilisateurs peuvent créer, gérer et supprimer des notes avec des tags qui leur sont spécifiques. L'application garantit la confidentialité en exigeant des identifiants de connexion pour accéder à la page d'accueil et aux notes.

### Fonctionnalités

- **Page d'Accueil** : Affiche une liste de toutes les notes de l'utilisateur connecté. Chaque note apparaît sous forme de carte, et en survolant une note, des icônes pour l'édition ou la suppression s'affichent.

- **Ajouter une Nouvelle Note** : Un bouton en haut de la page d'accueil ouvre une fenêtre pop-up pour créer une nouvelle note, avec des options pour ajouter des tags ou créer de nouveaux tags.

- **Tags** : Les tags sont spécifiques à chaque utilisateur et aident à classer les notes. Les utilisateurs peuvent ajouter ou créer des tags directement dans la fenêtre de création de note.

- **Authentification** :
  - Pages de **Connexion** et **Inscription** avec authentification basée sur JWT.
  - La connexion redirige vers la page d'accueil, tandis que l'inscription redirige vers la page de connexion.
  - L'accès à la page d'accueil est restreint aux utilisateurs authentifiés uniquement.
  - La fonction de déconnexion efface les identifiants et redirige vers la page de connexion.
  - Jeton d'accès de courte durée avec une expiration de 30 minutes.

- **Gestion des Erreurs** : Une page "Non Trouvée" est affichée pour les URL inexistantes.

> ### Conception et UX
>
> L'interface utilisateur (UI) et l'expérience utilisateur (UX) ont été pensées pour être simples et engageantes. Malheureusement, je n'ai pas eu le temps de travailler sur Figma en raison de ma cérémonie de remise de diplôme organisée par la Jadara Foundation hier pendant toute la journée. Ce projet a été réalisé en une journée, et je prévois d'apporter plusieurs améliorations par la suite. Pour voir mon travail précédent réalisé avec Figma, vous pouvez consulter ce lien : [lien vers le projet Figma]. Voici la réalisation finale de l'application.
>
> De plus, un espace administrateur a été mis en place pour gérer efficacement les utilisateurs, les notes et les tags.

### Documentation de l'API

Les API de cette application ont été créées à l'aide de Django REST Framework et sont disponibles via Insomnia et Swagger.

1. **Documentation Swagger** :
   - Accédez à la documentation Swagger à `http://localhost:8000/swagger/`.
   - Cette documentation fournit un aperçu de chaque point de terminaison avec des détails sur l'utilisation et des exemples de requêtes.

2. **Test des APIs avec Insomnia** :
   - Toutes les APIs ont été testées dans Insomnia, où les réponses, les codes d'état et la validation des données ont été vérifiés.
   - Des captures d'écran des requêtes et réponses API sont disponibles pour référence.

### Instructions d'Installation

1. **Cloner le Répertoire** :
   ```bash
   git clone <url_du_répertoire>
   cd note-management-app
   ```

2. **Configuration du Backend (Django)** :
   - Assurez-vous d'avoir Python installé, puis créez un environnement virtuel :
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Installez les packages requis :
     ```bash
     pip install -r requirements.txt
     ```
   - Exécutez les migrations et créez un super utilisateur :
     ```bash
     python manage.py migrate
     python manage.py createsuperuser
     ```
   - Démarrez le serveur Django :
     ```bash
     python manage.py runserver
     ```

3. **Configuration du Frontend (React)** :
   - Naviguez vers le répertoire frontend :
     ```bash
     cd frontend
     ```
   - Installez les dépendances :
     ```bash
     npm install
     ```
   - Démarrez le serveur React :
     ```bash
     npm start
     ```

### Exécution de l'Application

Pour exécuter l'application, démarrez d'abord le serveur Django, puis démarrez le serveur frontend React. L'application sera accessible à l'adresse `http://localhost:3000`.
