#Rapport d'Analyse de Sentiment Détaillé
feedback_clients = [
    "Le service était excellent et la nourriture était super!",
    "J'adore le design, mais j'ai été déçu par l'autonomie de la batterie.",
    "Le café est correct, sans plus.",
]

mots_cles_positifs = ['excellent', 'super', 'adore', 'génial', 'satisfait']
mots_cles_negatifs = ['déçu', 'mauvais', 'terrible', 'horrible', 'problème']

#Fonction analyse feedback
def analyser_feedback(donnees_feedback):
    resultats_analyse = []

    for commentaire in donnees_feedback:
        score = 0
        mots_cles_trouves = []

        # Vérifier les positifs
        for mot in mots_cles_positifs:
            if mot in commentaire.lower():
                score += 1
                mots_cles_trouves.append(mot)

        # Vérifier les négatifs
        for mot in mots_cles_negatifs:
            if mot in commentaire.lower():
                score -= 1
                mots_cles_trouves.append(mot)

        # Catégorisation finale
        if score > 0:
            sentiment_final = "Positif"
        elif score < 0:
            sentiment_final = "Négatif"
        elif score == 0 and mots_cles_trouves:
            sentiment_final = "Mixte"
        else:
            sentiment_final = "Neutre"

        # Construire le résultat pour ce commentaire
        resultat = {
            "commentaire": commentaire,
            "sentiment": sentiment_final,
            "score": score,
            "mots_cles": mots_cles_trouves
        }
        resultats_analyse.append(resultat)

    return resultats_analyse


# Utilisation
liste_retournee = analyser_feedback(feedback_clients)

# Rapport détaillé
print("===== Rapport d'Analyse de Sentiment Détaillé =====\n")
for item in liste_retournee:
    print(f"""Commentaire: "{item['commentaire']}"
- Sentiment: {item['sentiment']} (Score: {item['score']})
- Mots-clés trouvés: {item['mots_cles']}
{'-' * 48}""")

####################END#####################