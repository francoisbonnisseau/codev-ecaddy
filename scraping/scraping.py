"""
Ce fichier a pour but de rassembler les données scrapées dans chaque fichier "site", et de les télécharger dans des fichiers csv, dans un dossier avec la date du jour. Ainsi, chaque csv sera rangé dans un dossier "jj/mm/aaaa" et aura pour nom "nom_du_site_nom_du_produit"
"""

import csv
import boulanger, materiel


sites = [boulanger, materiel]

product = "ecouteurs"

product_data = {}

for site in sites:
    product_data[site] = site.get_infos(product)



# Enregistrer les données dans un fichier CSV
csv_file = open('products.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)



with open('products.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Écrire l'en-tête du fichier CSV
    writer.writerow(['Name', 'Description', 'Price', 'link', 'Image link'])
    
    # Écrire chaque ligne de données dans le fichier CSV
    for product in products_data:
        writer.writerow([product['Name'], product['Description'], product['Price'], product['Link'], product['Image link']])

# Fermer le fichier CSV
csv_file.close()
