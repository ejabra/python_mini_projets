#Rapport d'Analyse de Log Complet

log_data = """
2025-09-18 09:15:23 [INFO] - L'utilisateur 'admin' s'est connecté.
2025-09-18 09:22:41 [ERROR] - Échec de la connexion à la base de données.
2025-09-18 09:23:15 [WARNING] - Le temps de réponse du disque est élevé.
2025-09-18 10:05:00 [INFO] - Sauvegarde nocturne terminée.
2025-09-18 10:11:34 [ERROR] - Expiration de l'authentification de l'utilisateur.
"""

def analyser_fichier_log(donnees):
    comptes_par_niveau = {}
    comptes_horaires = {}
    erreurs_uniques = set()

    lignes = donnees.strip().split("\n")

    for ligne in lignes:
        # Découper horodatage et reste
        horodatage, reste = ligne.split(" [", 1)
        heure = horodatage[11:13]  # ex: "09"

        # Découper niveau et message
        niveau, message = reste.split("] - ", 1)
        niveau = niveau.strip()

        # Mettre à jour les structures
        comptes_par_niveau[niveau] = comptes_par_niveau.get(niveau, 0) + 1
        comptes_horaires[heure] = comptes_horaires.get(heure, 0) + 1
        if niveau == "ERROR":
            erreurs_uniques.add(message)

    return {
        "comptes_par_niveau": comptes_par_niveau,
        "comptes_horaires": comptes_horaires,
        "erreurs_uniques": erreurs_uniques
    }

# ------ Utilisation ------
resultats = analyser_fichier_log(log_data)

print("===== Rapport d'Analyse de Log Complet =====\n")

print("--- Comptes par Niveau de Log ---")
for niveau, count in resultats["comptes_par_niveau"].items():
    print(f"{niveau}: {count}")

print("\n--- Événements par Heure ---")
for heure, count in resultats["comptes_horaires"].items():
    print(f"Heure {heure}: {count} événements")

print("\n--- Messages d'Erreur Uniques ---")
for err in resultats["erreurs_uniques"]:
    print(f"- {err}")

print("====================================")