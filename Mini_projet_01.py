#POS pour une coffee shop local

#La commande client
commande_client = [
    {'nom': 'Latte', 'prix': 4.25, 'quantite': 2},
    {'nom': 'Muffin', 'prix': 3.25, 'quantite': 1}
]

#La fonction pour generer le reçu de la commande
def generer_recu(liste_commande, taux_taxe, code_reduction=None):
    sous_total = 0.0
    for commande in liste_commande:
        prix = commande['prix']
        quantite = commande['quantite']
        sous_total += prix * quantite

    #Appliquer la reduction si existe
    montant_reduction = 0.0
    rate_reduction = None
    if code_reduction:
        if code_reduction == 'SAVE10':  #code 'SAVE10' pour reduire 10%
            montant_reduction = sous_total * 0.10
            rate_reduction = '10%'
        elif code_reduction == '5OFF':  #code '5OFF' pour -5€
            montant_reduction = 5.0
            rate_reduction = '5€'
            if sous_total < montant_reduction:  #si le montant réduction > sous-total
                montant_reduction = sous_total
        elif code_reduction == '' or code_reduction is None:  #code vide ou non declaré
            montant_reduction = 0.0
        else:     #si un code inconnu
            montant_reduction = 0.0
    #Calculs
    montant_avec_reduction = sous_total - montant_reduction
    montant_taxe = montant_avec_reduction * taux_taxe
    grand_total = montant_avec_reduction + montant_taxe
    points_fedilite = int(grand_total // 5) # 1 point /5€

    #Imprimer le reçu formaté
    print("===== Reçu du Café =====")
    for commande in liste_commande:
        print(f"{commande['nom']}\t\t x {commande['quantite']}\t{commande['quantite']*commande['prix']:.2f}€")
    print('-'*26)
    print(f"Sous_total: \t\t{sous_total:.2f}€")
    print(f"Réduction ({rate_reduction}):\t-{montant_reduction:.2f}€" if montant_reduction != 0 else "Réduction:\t\t\t 0.00€")
    print(f"Taxe ({taux_taxe*100:.0f}%):\t\t\t {montant_taxe:.2f}€")
    print(f"Total:\t\t\t\t{grand_total:.2f}€")
    print('=' * 26)
    print(f"Points de fidélité gagnés: {points_fedilite}\n")
    #Return le Grand total
    return round(grand_total, 2)


#Test sans code reduction
Test01 = generer_recu(commande_client, 0.07)

#Test avec code reduction 'SAVE10'
# Test02 = generer_recu(commande_client, 0.07, 'SAVE10')

#Test avec code reduction '5OFF'
# Test03 = generer_recu(commande_client, 0.07, '5OFF')

#Test avec code reduction Non definé
# Test04 = generer_recu(commande_client, 0.07, 'RED10')
