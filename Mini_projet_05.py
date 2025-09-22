#Outil de gestion de budget
transactions = []

#Fonction main pour afficher le menu principal
def main():
    while True:
        input(f"\nAppuyez sur une touche pour Afficher le Menu Principal.. ")
        print("\n====== Menu Budget ======")
        print("1. Ajouter une transaction")
        print("2. Voir toutes les transactions")
        print("3. Voir transactions par catégorie")
        print("4. Imprimer rapport récapitulatif")
        print("5. Quitter")
        print("="*28)
        choix = input(f"• Entrez Votre choix : ").strip()

        if not choix.isdigit():
            print("Entrée invalide ! Veuillez entrer un nombre.")
            continue
        #convirtir en nombre entier
        choix = int(choix)  #convirter en chiffre entier

        if choix == 1:
            ajouter_transaction()
        elif choix == 2:
            voir_toutes_transactions()
        elif choix == 3:
            voir_transactions_par_cat()
        elif choix == 4:
            resume = calculer_resume()
            imprimer_rapport(resume)
        elif choix == 5:
            #confirmation avant Quiter
            confirmation_quit = input(f"Voulez vous vraiment quitter le programme ? (Y/N) ")
            if confirmation_quit.lower() == "n":
                continue
            elif confirmation_quit.lower() == "y":
                print("Au revoir !")
                break
        else:
            print("Choix invalide, veuillez réessayer.")

#fonction ajout de nouvelle transaction
def ajouter_transaction():
    print("\n*** Ajouter transaction ***")
    print('-'*28)
    #Type transaction 'revenu' ou 'depense'
    while True:
        type_entree = input("Entrer le Type 'revenu' ou 'depense' ? : ").strip().lower()
        if type_entree in ("revenu","depense"):
            break
        print(f"Entrée invalide! Tapez 'revenu' ou 'depense'.")

    #Montant de transaction
    while True:
        montant_entree = input("Entrer le montant de la transaction (ex: 123.45) : ").strip()
        montant_transaction = montant_entree.replace(' ', '').replace(',', '.')
        try:
            montant = float(montant_transaction)
            if montant > 0:
                break  # valide, on sort de la boucle
            else:
                print("Montant invalide. Entrez un nombre positif et non nul.")
        except ValueError:
            print("Montant invalide. Veuillez entrer un mantant valide.")

    #Categorie
    while True:
        categorie = input("Catégorie (ex: Loyer, Nourriture) : ").strip()
        if categorie:
            break
        print(f"Veuillez saisir la catégorie.*")

    description = input("Description (optionnelle) : ").strip()

    transaction = {'type' : type_entree,
                   'montant' : montant,
                   'categorie' : categorie,
                   'description' : description}

    transactions.append(transaction)
    print("Transaction ajoutée avec succès.")

#Fonction Affichage de transactions
def voir_toutes_transactions():
    print(f"\n *** {'Voir toutes transactions'.upper()} ***")
    if not transactions:
        print('-' * 34)
        print(f"Aucune transaction enregistrée.")
        return
    #entête
    print('-' * 75)
    print(f"{'Num':<5} {'Type':<20} {'Catégorie':<20} {'montant':<14} {'Description':<40}")
    print('-'*75)
    for i, transaction in enumerate(transactions, 1):
        sign = "-" if transaction['type'] == 'depense' else ""
        montant_formatee = f"{sign}{transaction['montant']:.2f}€"
        print(f"{i:<5} {transaction['type']:<20} {transaction['categorie']:<20} {montant_formatee:<14} {transaction['description']:<40}")

def voir_transactions_par_cat():
    print("\n*** Voir transactions par catégorie ***")
    if not transactions:
        print('-' * 40)
        print(f"Aucune transaction enregistrée.")
        return

    cat = input("Entrez le nom de la catégorie à filtrer : ").strip().lower()
    filtres = [trans for trans in transactions if trans['categorie'].strip().lower() == cat]

    if not filtres:
        print(f"Aucune transaction trouvée pour la catégorie '{cat}'.")
        return

    print(f"\nTransactions dans la catégorie '{cat}':")
    print('-' * 75)
    print(f"{'Num':<5} {'Type':<20} {'Catégorie':<20} {'montant':<14} {'Description':<40}")
    print('-' * 75)
    for i, transaction in enumerate(filtres,1):
        sign = "-" if transaction['type'] == 'depense' else ""
        montant_formatee = f"{sign}{transaction['montant']:.2f}€"
        print(f"{i:<5} {transaction['type']:<20} {transaction['categorie']:<20} {montant_formatee:<14} {transaction['description']:<40}")

def calculer_resume():
    total_revenus = 0.0
    total_depenses = 0.0
    depenses_par_categorie = {}

    for trans in transactions:
        if trans['type'] == 'revenu':
            total_revenus += trans['montant']
        else:  #depense
            total_depenses += trans['montant']
            cat = trans['categorie'].strip()
            depenses_par_categorie[cat] = depenses_par_categorie.get(cat, 0.0) + trans['montant']

    epargne = total_revenus - total_depenses
    # Pourcentages par catégorie
    pourcentages = {}
    if total_depenses > 0:
        for cat, subtotal in depenses_par_categorie.items():
            pourcentages[cat] = (subtotal / total_depenses) * 100
    else:
        for cat in depenses_par_categorie:
            pourcentages[cat] = 0.0

    resume = {
        'total_revenus': total_revenus,
        'total_depenses': total_depenses,
        'epargne': epargne,
        'depenses_par_categorie': depenses_par_categorie,
        'pourcentages_depenses': pourcentages
    }
    return resume

def imprimer_rapport(resume):
    print("\n======= Résumé Financier =======")
    print(f"{'Revenu Total:':<20} {resume['total_revenus']:>10.2f}€")
    # afficher les dépenses comme valeurs négatives pour clarifier
    print(f"{'Dépenses Totales:':<20} {-resume['total_depenses']:>10.2f}€")
    print("-" * 33)
    print(f"{'Épargne Nette:':<20} {resume['epargne']:>10.2f}€")
    print("\n--- Dépenses par Catégorie ---")
    if not resume['depenses_par_categorie']:
        print("Aucune dépense enregistrée.")
    else:
        # Trier par montant décroissant pour lisibilité
        items = sorted(resume['depenses_par_categorie'].items(), key=lambda x: x[1], reverse=True)
        for cat, montant in items:
            pct = resume['pourcentages_depenses'].get(cat, 0.0)
            print(f"{cat:<12} {montant:>10.2f}€ ({pct:>5.1f}%)")
    print("=" * 32)

#Appel fonction main()
main()
