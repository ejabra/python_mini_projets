#=== Menu Inventaire ===
inventaire = { 'Dune': 15, '1984': 5, 'Fondation': 3 }

#Fonction Affichage de menu
def afficher_menu():
    while True:
        input(f"\nAppuyez sur une touche pour Afficher le Menu Principal.. ")
        print("\n====== Menu Inventaire ======")
        print("1. Voir tout l'inventaire")
        print("2. Ajouter un article")
        print("3. Mettre à jour un article")
        print("4. Supprimer un article")
        print("5. rechercher_article")
        print("6. Rapport de Stock Faible")
        print("7. Quitter")
        print("="*28)
        choix = input(f"• Entrez Votre choix : ").strip()

        if not choix.isdigit():
            print("Entrée invalide ! Veuillez entrer un nombre.")
            continue

        choix = int(choix)  #convirter en chiffre entier

        if choix == 1:
            afficher_inventaire()
        elif choix == 2:
            ajouter_article()
        elif choix == 3:
            update_article()
        elif choix == 4:
            supprimer_article()
        elif choix == 5:
            rechercher_article()
        elif choix == 6:
            rapport_stock_faible()
        elif choix == 7:
            #confirmation avant Quiter
            confirmation_quit = input(f"Voulez vous vraiment quitter le programme ? (Y/N) ")
            if confirmation_quit.lower() == "n":
                continue
            elif confirmation_quit.lower() == "y":
                print("Au revoir !")
                break
        else:
            print("Choix invalide, veuillez réessayer.")


#--- Appel au fonctions de menu ---#

#la fonction pour afficher le stock actuel
def afficher_inventaire ():
    print("\n**** Inventaire Actuel ****")
    print("-" * 28)
    if not inventaire:
        print("Inventaire est vide !")
    else:
        print(f" • {'Article':<12} | {'Quantité'}")
        print('-'*28)
        for article, quantite in inventaire.items():
            print(f" • {article:<12} | Stock: {quantite}")
        print('-'*28)

#La fonction pour ajouter un article
def ajouter_article ():
    print("\n**** Ajouter un article ****")
    print("-" * 28)
    nom_product = ''
    while not nom_product:
        nom_product = input("Entrez le nom de l'article à ajouter: ").strip()
        if not nom_product:
            print("Vieulliez entrer un nom de produit valide !") #entré vide!
            continue
        inventaire_lowercase = {key.lower(): key for key in inventaire}
        if nom_product.lower() not in inventaire_lowercase:
                while True:
                    quantity = input(f"Entrez la nouvelle quantité pour '{nom_product}': ").strip()
                    if quantity.isdigit():
                        inventaire[nom_product] = int(quantity)
                        print(f"Produit ajouté avec succès!  '{nom_product}' | Quantité: {quantity}")
                        break
                    else:
                        print("Entrée invalide. Veuillez entrer un nombre.")
                        continue
        else:
            print("Article déja exist !")

#La fonction pour mettre à jour un article
def update_article ():
    print("\n*** Mettre à jour d'un article ***")
    print("-" * 34)
    inventaire_lowercase =  {key.lower(): key for key in inventaire}
    nom_product = input("Entrez le nom de l'article à mettre à jour: ").lower().strip()

    if nom_product in inventaire_lowercase:
        nom_original = inventaire_lowercase[nom_product]
        while True:
            quantity = input("Entrez la nouvelle quantité: ").strip()
            if quantity.isdigit():
                inventaire[nom_original] = int(quantity)
                print(f"Quantité mis à jour pour {nom_original}! (Quantité: {quantity})")
                break
            else:
                print("Entrée invalide. Veuillez entrer un nombre.")
                continue
    else:
        print("Article not exist !")

#La fonction pour supprimer un article
def supprimer_article ():
    print("\n*** Supprimer un article ***")
    print("-" * 28)
    inventaire_lowercase = {key.lower(): key for key in inventaire}
    nom_produit = input("Entrez le nom de l'article à Supprimer : ").lower().strip()
    if nom_produit in inventaire_lowercase:
        nom_original = inventaire_lowercase[nom_produit]
        confirmation_quit = input(f"Voulez vous vraiment supprimer l'article '{nom_original}' ? (Y/N) ")
        if confirmation_quit.lower() == "y":
            del inventaire[nom_original]
            print(f"Article '{nom_original}' suprimé.")

    else:
        print("Article non trouvé !")

#La fonction pour Rechercher un article
def rechercher_article():
    print("\n**** Rechercher un article ****")
    print("-" * 30)
    inventaire_lowercase = {key.lower(): key for key in inventaire}

    nom_rechercher = input("Nom de l'article à rechercher : ").lower().strip()
    if nom_rechercher in inventaire_lowercase:
        nom_original = inventaire_lowercase[nom_rechercher]
        print("-" * 30)
        print(f" '{nom_original}' | Quantité: {inventaire[nom_original]} unités.")
        print("-" * 30)
    else:
        print(f"'{nom_rechercher}' n'est pas dans l'inventaire !")

#Afficher le Rapport Stock faible
def rapport_stock_faible ():
    print("\n**** Rapport de Stock Faible ****")
    print("-" * 34)
    while True:
        seuil = input("Entrez le seuil de Stock faible: ").strip()
        if seuil.isdigit():
            seuil = int(seuil)
            break
        else:
            print("Entrée invalide. Veuillez entrer un nombre.")
    stock_faible = {key: value for key,value in inventaire.items() if value <= seuil}
    print(f"\n•• Stock faible : {len(stock_faible)} articles trouvés. ••")
    print("-" * 40)
    if not stock_faible:
        print("Aucun article avec stock faible !")
    else:
        for article, quantite in stock_faible.items():
            print(f"{article:<22} | Quantité: {quantite}")
        print("-" * 40)

# -- Lancement de Menu --
afficher_menu()