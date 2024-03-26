"""
Ce fichier a pour but de rassembler les données scrapées dans chaque fichier "site", et de les télécharger dans des fichiers csv, dans un dossier avec la date du jour. Ainsi, chaque csv sera rangé dans un dossier "jj_mm_aaaa" et aura pour nom "nom_du_site_nom_du_produit"
"""

import csv
from datetime import date
import os
from bs4 import BeautifulSoup
import requests

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

class Site:
    def __init__(self, nom, base_url, search_url, selectors):
        self.nom = nom
        self.base_url = base_url
        self.search_url = search_url
        self.selectors = selectors
        self.data_list = []

    def get_infos(self, product_name):
        url = f"{self.search_url}{product_name}"
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")

        products = soup.select(self.selectors['products'])

        for product in products:
            name = self._extract_text(product, self.selectors['name'])
            brand = self._extract_text(product, self.selectors['brand'])
            price = self._extract_text(product, self.selectors['price'])
            description = self._extract_text(product, self.selectors['description'])
            url_product = self._extract_attribute(product, self.selectors['url_product'], 'href')
            url_image = self._extract_attribute(product, self.selectors['url_image'], 'src')
            
            if self.nom == 'materiel':
                brand = brand.split(" ")[0]
                
            data = {
                'Nom': name,
                'Marque': brand,
                'Prix': price,
                'Description': description,
                'Url': url_product,
                'Url_image': url_image
            }
            
            self.data_list.append(data)
        return self.data_list

    def _extract_text(self, element, selector):
        selected_element = element.select_one(selector)
        return selected_element.get_text(strip=True) if selected_element else None

    def _extract_attribute(self, element, selector, attribute):
        selected_element = element.select_one(selector)
        return selected_element.get(attribute) if selected_element else None
    
    def _save_data_in_csv(self, product_name):
        # Enregistrer les données dans un fichier CSV
        csv_file = open(f'{self.nom}_{product_name}.csv', 'w', encoding='utf-8', newline='')
        writer = csv.writer(csv_file)

        with open(f'{self.nom}_{product_name}.csv', 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Écrire l'en-tête du searched_fichier CSV
            writer.writerow(['Nom', 'Marque', 'Prix', 'Description', 'Url', 'Url_image'])

            # Écrire chaque ligne de données dans le fichier CSV
            for product in self.data_list:
                writer.writerow([product['Nom'], product['Marque'], product['Prix'], product['Description'], product['Url'], product['Url_image']])

            # Fermer le fichier CSV
            csv_file.close()
            
    def write_data(self, product_name):
        today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")
        self.get_infos(product_name)
        if os.path.isdir(today_date):
            os.chdir(today_date)
            self._save_data_in_csv(product_name)
            os.chdir('..')
        else:
            os.mkdir(today_date)
            os.chdir(today_date)
            self._save_data_in_csv(product_name)
            os.chdir('..')


if __name__ == "__main__":
    # Define the base URL and selectors for the Materiel.net website
    base_url = "https://www.materiel.net"
    search_url = "https://www.materiel.net/recherche/"
    selectors = {
        'products': '.c-products-list__item',
        'name': '.c-product__title',
        'brand': '.c-product__title',  # Assuming brand is also inside title element
        'price': '.o-product__price',
        'description': '.c-product__description',
        'url_product': '.c-product__link',
        'url_image': '.c-product__thumb > a > img.img-fluid'
    }

    # Create an instance of the Site class for Materiel.net
    materiel_net_site = Site('materiel', base_url, search_url, selectors)

    # Get product information
    product = "ecouteurs"
    materiel_net_site.write_data(product_name=product)