import csv

# On ouvre le fichier 'produits.csv' en mode lecture ('r' pour read)
print("--- LISTE DES PRODUITS ---")

try:
    with open('produits.csv', mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        
        # Pour chaque ligne dans le fichier, on l'affiche
        for ligne in lecteur:
            print(f"Produit {ligne['id']} : {ligne['nom']} - {ligne['prix']} €")

except FileNotFoundError:
    print("Erreur : Le fichier produits.csv est introuvable !")