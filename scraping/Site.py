"""
Cette classe a pour but de scraper les données de chaque site, et de les télécharger dans des fichiers csv, dans un dossier avec la date du jour. Ainsi, chaque csv sera rangé dans un dossier "jj_mm_aaaa" et aura pour nom "nom_du_site_nom_du_produit"
"""

import csv
from datetime import date
import os
from bs4 import BeautifulSoup
import requests
import json
import time
# import sys
# sys.path.append("..")
# from interface.windowError import WindowError

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
        name_for_research=product_name.replace("_","%20")
        url = f"{self.search_url}{name_for_research}"
        #requête de la page demandée
        page = requests.get(url, headers=headers)
        if page.status_code != 200:
            print(f"Erreur en tentant d'accéder à la page : {url}")
            WindowError(f"Erreur en tentant d'accéder à la page : {url}")
            return None
        soup = BeautifulSoup(page.text, "html.parser")

        #on récupère la structure principale où sont stockés tous les produits sur la page
        try:
            products = soup.select(self.selectors['products'])
        except Exception as e:
            print(f"Erreur en tentant de récupérer les éléments de la page: {e}")
            WindowError(f"Erreur en tentant de récupérer les éléments de la page: {e}")
            return None

        for product in products: #cas général plus gestion de qq exceptions selon le site
            name = self._extract_text(product, self.selectors['name'])
            if self.nom == 'materiel':
                brand = self._extract_text(product, self.selectors['brand']).split(" ")[0]
            else:
                brand = self._extract_text(product, self.selectors['brand'])
            #récupération du prix
            price = self._extract_text(product, self.selectors['price'])
            #récupération de la description du produit
            description = self._extract_text(product, self.selectors['description'])
            #? gestion des cas particuliers en fonction de la configuration des sites - ici pour alternate
            if self.nom == 'alternate':
                url_product = product.get('href')
            else:
                url_product = self._extract_attribute(product, self.selectors['url_product'], 'href')
            url_image = self._extract_attribute(product, self.selectors['url_image'], 'src')
                
            #? gestion cas particuliers pour récupérer le lien complet de l'image
            if self.nom == 'boulanger' or self.nom == 'grosbill' or self.nom == 'alternate':
                if url_image:
                    url_image = self.base_url + url_image
            #print("wait i a will start to write data ")
            if price != None and name != None and brand != None and description != None and url_product != None:
                #on stocke toutes les données d'un produit dans ce dictionnaire data, que l'on ajoute ensuite à la liste data_list
                data = {
                    'Nom': name,
                    'Marque': brand,
                    'Prix': price,
                    'Description': description,
                    'Url': url_product,
                    'Url_image': url_image
                }
                
                self.data_list.append(data)
                #print(f"hey i am writing data see:{data}")
            
            #self.data_list.append(data)
        return self.data_list

    # méthode pour extraire le texte d'une balise html
    def _extract_text(self, element, selector):
        try:
            selected_element = element.select_one(selector)
            return selected_element.get_text(strip=True) if selected_element else None
        except Exception as e:
            print(f"Erreur en tentant d'extraire le texte avec le sélecteur '{selector}': {e}")
            WindowError(f"Erreur en tentant d'extraire le texte avec le sélecteur '{selector}': {e}")
            return None

    # Méthode pour extraire un attribut d'une balise HTML
    def _extract_attribute(self, element, selector, attribute):
        try:
            selected_element = element.select_one(selector)
            return selected_element.get(attribute) if selected_element else None
        except Exception as e:
            print(f"Erreur en tentant d'extraire l'attribut '{attribute}' avec le sélecteur '{selector}': {e}")
            WindowError(f"Erreur en tentant d'extraire l'attribut '{attribute}' avec le sélecteur '{selector}': {e}")
            return None
    
    
    def _save_data_in_csv(self, product_name):
        # Enregistrer les données dans un fichier CSV
        csv_file = open(f'{self.nom}_{product_name}.csv', 'w', encoding='utf-8', newline='')
        writer = csv.writer(csv_file)

        with open(f'{self.nom}_{product_name}.csv', 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Écrire l'en-tête du fichier CSV
            writer.writerow(['Nom', 'Marque', 'Prix', 'Description', 'Url', 'Url_image'])

            # Écrire chaque ligne de données dans le fichier CSV
            for product in self.data_list:
                writer.writerow([product['Nom'], product['Marque'], product['Prix'], product['Description'], product['Url'], product['Url_image']])

            # Fermer le fichier CSV
            csv_file.close()
    
    #méthode pour créer un fichier csv avec les produits trouvés pour un site    
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
    # stockage des informations dans un json sites_information.json et lecture, stockage dans un dictionnaire
    
    with open('site_information.json', 'r') as infos_file:
        site_information = json.load(infos_file)
        # print(site_information)
        print(json.dumps(site_information, indent=4, sort_keys=True))
    
    
    # site_information = {
    #     'boulanger': {
    #         'base_url': 'https://boulanger.com',
    #         'search_url': 'https://www.boulanger.com/resultats?tr=',
    #         'selectors': {
    #             'products': '.product-list__item',
    #             'name': '.product-list__product-label',
    #             'brand': '.product-list__product-label > strong',
    #             'price': '.price__amount',
    #             'description': '.keypoints',
    #             'url_product': '.product-list__product-image-link',
    #             'url_image': 'img.product-list__product-image'
    #         }
    #     },
    #     'materiel': {
    #         'base_url' : 'https://materiel.net',
    #         'search_url' : 'https://www.materiel.net/recherche/',
    #         'selectors' : {
    #             'products': '.c-products-list__item',
    #             'name': '.c-product__title',
    #             'brand': '.c-product__title',  # traitement spécifique pour ce site
    #             'price': '.o-product__price',
    #             'description': '.c-product__description',
    #             'url_product': '.c-product__link',
    #             'url_image': '.c-product__thumb > a > img.img-fluid'
    #         }
    #     },
    #     'grosbill': {
    #         'base_url' : 'https://www.grosbill.com',
    #         'search_url' : 'https://www.grosbill.com/produit.aspx?q=',
    #         'selectors' : {
    #             'products': '.la_liste_des_produits.grb__liste-produit__liste__produit',
    #             'name': '.grb__liste-produit__liste__produit__information__libelle__libelle_produit',
    #             'brand': '.grb__liste-produit__liste__produit__information__constructeur',
    #             'price': '.grb__liste-produit__liste__produit__achat__prix > span',
    #             'description': '.grb__liste-produit__liste__produit__information__caracteristiques__liste',
    #             'url_product': '.prod_txt_left',
    #             'url_image': '.grb__liste-produit__liste__produit__image > a.prod_txt_left > img'
    #         }
    #     },
    #     'cybertech': {
    #         'base_url' : 'https://www.cybertek.fr/',
    #         'search_url' : 'https://www.cybertek.fr/boutique/produit.aspx?q=',
    #         'selectors' : {
    #             'products': '.la_liste_des_produits.grb__liste-produit__liste__produit',
    #             'name': '.grb__liste-produit__liste__produit__information__libelle__libelle_produit',
    #             'brand': '.grb__liste-produit__liste__produit__information__constructeur',
    #             'price': '.grb__liste-produit__liste__produit__achat__prix > span',
    #             'description': '.grb__liste-produit__liste__produit__information__caracteristiques__liste',
    #             'url_product': '.prod_txt_left',
    #             'url_image': '.grb__liste-produit__liste__produit__image > a.prod_txt_left > img'
    #         }
    #     },
    #     'alternate': {
    #         'base_url': 'https://www.alternate.fr',
    #         'search_url': 'https://www.alternate.fr/listing.xhtml?q=',
    #         'selectors': {
    #             'products': '.productBox.boxCounter',
    #             'name': '.product-name',
    #             'brand': '.product-name > span',
    #             'price': '.price',
    #             'description': '.product-info',
    #             'url_product': '.productBox.boxCounter',
    #             'url_image': 'img.productPicture'
    #         }
    #     }
    # }

    #creation des instances de classe Site
    materiel_net = Site('materiel', site_information['materiel']['base_url'], site_information['materiel']['search_url'], site_information['materiel']['selectors'])
    boulanger = Site('boulanger', site_information['boulanger']['base_url'], site_information['boulanger']['search_url'], site_information['boulanger']['selectors'])
    grosbill = Site('grosbill', site_information['grosbill']['base_url'], site_information['grosbill']['search_url'], site_information['grosbill']['selectors'])
    cybertech = Site('cybertech', site_information['cybertech']['base_url'], site_information['cybertech']['search_url'], site_information['cybertech']['selectors'])
    alternate = Site('alternate', site_information['alternate']['base_url'], site_information['alternate']['search_url'], site_information['alternate']['selectors'])
    

    # Get product information
    # product = "gopro"
    # materiel_net.write_data(product_name=product)
    # boulanger.write_data(product_name=product)
    # grosbill.write_data(product_name=product)
    # cybertech.write_data(product_name=product)
    # alternate.write_data(product_name=product)

    
    # Test du temps de scraping
    products = [
        "ordinateur portable",
        "imprimante",
        "disque dur externe",
        "clavier sans fil",
        "souris gamer",
        "écran LCD",
        "routeur Wi-Fi",
        "casque audio",
        "webcam HD",
        "tablette graphique"
    ]

    # Get product information for each product
    average_times_materiel = []
    average_times_boulanger = []
    average_times_grosbill = []
    average_times_cybertech = []
    average_times_alternate = []

    for product in products:
        start_time = time.time()
        materiel_net.get_infos(product_name=product)
        end_time = time.time()
        total_time = end_time - start_time
        average_times_materiel.append(total_time)

        start_time = time.time()
        boulanger.get_infos(product_name=product)
        end_time = time.time()
        total_time = end_time - start_time
        average_times_boulanger.append(total_time)

        start_time = time.time()
        grosbill.get_infos(product_name=product)
        end_time = time.time()
        total_time = end_time - start_time
        average_times_grosbill.append(total_time)

        start_time = time.time()
        cybertech.get_infos(product_name=product)
        end_time = time.time()
        total_time = end_time - start_time
        average_times_cybertech.append(total_time)

        start_time = time.time()
        alternate.get_infos(product_name=product)
        end_time = time.time()
        total_time = end_time - start_time
        average_times_alternate.append(total_time)

    mean_time_materiel = sum(average_times_materiel) / len(average_times_materiel)
    mean_time_boulanger = sum(average_times_boulanger) / len(average_times_boulanger)
    mean_time_grosbill = sum(average_times_grosbill) / len(average_times_grosbill)
    mean_time_cybertech = sum(average_times_cybertech) / len(average_times_cybertech)
    mean_time_alternate = sum(average_times_alternate) / len(average_times_alternate)

    print(f"Temps moyen de scraping par produit pour Materiel.net : {mean_time_materiel} secondes")
    print(f"Temps moyen de scraping par produit pour Boulanger : {mean_time_boulanger} secondes")
    print(f"Temps moyen de scraping par produit pour Grosbill : {mean_time_grosbill} secondes")
    print(f"Temps moyen de scraping par produit pour Cybertech : {mean_time_cybertech} secondes")
    print(f"Temps moyen de scraping par produit pour Alternate : {mean_time_alternate} secondes")