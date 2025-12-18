import csv

def afficher_inventaire(liste_produits=None):
    """Affiche les produits. Si une liste est fournie, affiche celle-là, sinon lit le fichier."""
    print("\n--- INVENTAIRE ---")
    try:
        if liste_produits is None:
            with open('produits.csv', mode='r', encoding='utf-8') as fichier:
                liste_produits = list(csv.DictReader(fichier))
        
        for ligne in liste_produits:
            print(f"ID {ligne['id']} : {ligne['nom']} | {ligne['prix']}€ | Stock: {ligne['quantité']}")
    except FileNotFoundError:
        print("Erreur : Le fichier produits.csv est introuvable !")

def ajouter_produit():
    print("\n--- AJOUTER UN PRODUIT ---")
    id_p = input("ID : ")
    nom = input("Nom : ")
    desc = input("Description : ")
    try:
        prix = float(input("Prix : "))
        quantite = int(input("Quantité : "))
    except ValueError:
        print("❌ Erreur : Le prix et la quantité doivent être des nombres.")
        return

    with open('produits.csv', mode='a', newline='', encoding='utf-8') as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow([id_p, nom, desc, prix, quantite])
    print("✅ Produit ajouté !")

def rechercher_produit():
    nom_recherche = input("\nNom du produit à chercher : ").lower()
    trouve = False
    with open('produits.csv', mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            if nom_recherche in ligne['nom'].lower():
                print(f"🔍 Trouvé : {ligne['nom']} - {ligne['prix']}€ (Stock: {ligne['quantité']})")
                trouve = True
    if not trouve:
        print("❌ Aucun produit ne correspond à ce nom.")

def trier_produits():
    print("\n1. Trier par prix (Croissant)")
    print("2. Trier par quantité (Croissant)")
    choix_tri = input("Votre choix : ")
    
    with open('produits.csv', mode='r', encoding='utf-8') as fichier:
        produits = list(csv.DictReader(fichier))
    
    if choix_tri == "1":
        # On trie par prix (on convertit en float pour que 10 soit après 2)
        produits.sort(key=lambda x: float(x['prix']))
    elif choix_tri == "2":
        # On trie par quantité (reverse=True pour avoir le plus grand en haut)
        produits.sort(key=lambda x: int(x['quantité']), reverse=True)
    
    afficher_inventaire(produits)

# --- MENU PRINCIPAL ---
while True:
    print("\n--- MENU GESTION STOCK ---")
    print("1. Voir tous les produits")
    print("2. Ajouter un produit")
    print("3. Rechercher un produit")
    print("4. Trier les produits")
    print("5. Quitter")
    
    choix = input("Votre choix : ")
    if choix == "1": afficher_inventaire()
    elif choix == "2": ajouter_produit()
    elif choix == "3": rechercher_produit()
    elif choix == "4": trier_produits()
    elif choix == "5": break