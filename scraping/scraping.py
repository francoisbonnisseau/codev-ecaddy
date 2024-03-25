"""
Ce fichier a pour but de rassembler les données scrapées dans chaque fichier "site", et de les télécharger dans des fichiers csv, dans un dossier avec la date du jour. Ainsi, chaque csv sera rangé dans un dossier "jj_mm_aaaa" et aura pour nom "nom_du_site_nom_du_produit"
"""

import csv
from datetime import date
import boulanger, materiel
import os

sites = ["boulanger", "materiel"]

searched_product = "ecouteurs"


today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")


    
def save_data_in_csv(data, name, site_name):
    # Enregistrer les données dans un fichier CSV
    csv_file = open(f'{site_name}_{name}.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)


    with open(f'{site_name}_{name}.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Écrire l'en-tête du searched_fichier CSV
        writer.writerow(['Nom', 'Marque', 'Prix', 'Description', 'Url', 'Url_image'])
        
        # Écrire chaque ligne de données dans le fichier CSV
        for product in data[site_name]:
            writer.writerow([product['Nom'], product['Marque'], product['Prix'], product['Description'], product['Url'], product['Url_image']])

    print(f"données de {name} du site {site_name} sauvegardées")
    # Fermer le fichier CSV
    csv_file.close()

def get_data_from_sites(sites_list, product):
    product_data = {}
    if "boulanger" in sites_list:
        product_data["boulanger"] = boulanger.get_products(product)

    if "materiel" in sites_list:
        product_data["materiel"] = materiel.get_products(product)
    return product_data

product_data = get_data_from_sites(sites, searched_product)
print(product_data)

for site in sites:
    try:
        os.mkdir(today_date)
        os.chdir(today_date)
        save_data_in_csv(product_data, searched_product, site)
    except:
        os.chdir(today_date)
        save_data_in_csv(product_data, searched_product, site)
    
    
