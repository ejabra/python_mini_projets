<div align="center">

# 🐍 Python Mini-Projects Collection

**Une suite de 5 outils pratiques démontrant la maîtrise des structures de données et de la logique algorithmique en Python.**

_Projets réalisés dans le cadre de la formation JobInTech (Data Engineering)_.

[📂 Explorer le code](https://github.com/ejabra/python_mini_projets/tree/brahim) · [🐞 Signaler un bug](../../issues)

</div>

---

## 📌 Vue d'ensemble

Ce dépôt regroupe cinq mini-projets développés pour résoudre des problématiques concrètes de gestion de données, allant du système de point de vente à l'analyse de logs serveur.

L'objectif principal était de renforcer la maîtrise des concepts clés de Python :
* Manipulation de **Listes et Dictionnaires**.
* Parsing de chaînes de caractères (**String Manipulation**).
* Logique conditionnelle et boucles complexes.
* Architecture de code modulaire et validation des entrées.

---

## 📂 Liste des Projets

### 1. 🧾 Système de Génération de Reçus (POS)
Un script simulant un terminal de point de vente pour un café local.
* **Fonctionnalités :** Calcul du sous-total, application de codes promo (`SAVE10`, `5OFF`), ajout de la TVA et calcul des points de fidélité.
* **Concepts clés :** Dictionnaires imbriqués, logique conditionnelle pour les réductions.

### 2. 💬 Analyseur de Feedback Clients (Sentiment Analysis)
Un outil d'analyse de texte pour classer les retours clients.
* **Fonctionnalités :** Détection de mots-clés, calcul d'un "score de sentiment" et classification automatique (Positif, Négatif, Neutre, Mixte).
* **Concepts clés :** Algorithme de scoring (+1/-1), itération sur des listes de chaînes.

### 3. 📚 Système d'Inventaire (CRUD)
Une application console pour gérer le stock d'une librairie.
* **Fonctionnalités :** Ajout, modification, suppression et recherche d'articles. Inclut une alerte "Stock Faible" et une validation robuste des entrées numériques pour éviter les crashs.
* **Concepts clés :** Fonctions CRUD, validation des données (`try/except`), formatage de tableaux (`f-strings`).

### 4. 🕵️‍♂️ Analyseur de Logs Serveur
Un script conçu pour le Data Engineering afin d'extraire des insights de fichiers bruts.
* **Fonctionnalités :** Parsing ligne par ligne pour extraire les horodatages et les niveaux (INFO, WARNING, ERROR). Génère des statistiques par heure et isole les messages d'erreur uniques.
* **Concepts clés :** Parsing de fichiers texte, utilisation de `Set` pour les unicités, agrégation de données.

### 5. 💰 Outil de Budgétisation Amélioré
Une application de gestion financière personnelle.
* **Fonctionnalités :** Enregistrement des transactions, filtrage par catégorie, et génération d'un rapport financier avec calcul des pourcentages de dépenses.
* **Concepts clés :** Calculs statistiques simples, filtrage de données, architecture modulaire.

---

## 🛠️ Technologies & Compétences

| Domaine | Compétences Démontrées |
| :--- | :--- |
| **Langage** | Python 3.x |
| **Structures de Données** | Listes, Dictionnaires, Sets, Tuples |
| **Algorithmique** | Boucles (For/While), Conditions (If/Elif/Else), Gestion d'erreurs |
| **Data Processing** | Parsing de logs, Agrégation, Calculs statistiques |

---

## 🚀 Comment exécuter les projets

Chaque projet est indépendant. Pour en tester un :

1.  Clonez le dépôt :
   ```bash
    git clone [https://github.com/ejabra/python-mini-projects.git](https://github.com/ejabra/python-mini-projects.git)
    ```
2.  Accédez au dossier du projet et lancez le script :
    ```bash
    python nom_du_script.py
    ```

---

## 👥 Auteurs

Ce travail a été réalisé en binôme par :

* **Brahim DARGUI** - [https://github.com/ejabra]
* **Mohamed FEJJARY** - [https://github.com/fullStackMohamed]

---
<div align="center">
  <small>2025 - Formation JobInTech Data Engineering</small>
</div>
