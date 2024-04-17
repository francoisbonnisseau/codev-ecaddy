# cart.py
import os
import csv
import numpy as np 
from product import Product
from demand import Demand
class Cart:
    """classmethod"""
    def __init__(self,demand):
        self.products = []
        self.demand=demand
    def get_products(self):
        return self.products
    def get_demand(self):
        return self.demand
    def set_demand(self,demand):
        self.demand=demand
    
    def add_product(self, product):
        """Add a product to the cart."""
        self.products.append([product])

    def remove_product(self, product):
        """Remove a product from the cart."""
        for store_products in self.products:
            if product in store_products:
                store_products.remove(product)
            if len(store_products)==0:
                self.products.remove(store_products)

    def search_product_by_attributes(self, name=None, price_min=None, price_max=None, brand=None, description=None, store=None, url=None, image_url=None):
        """Searches for products in the cart based on specified attributes."""
        useful_products=[]
        best_products=[]
        for store_product in self.products:
            best_store_price=np.inf
            best_store_product=None
            matching_products = []
            for product in store_product:
                # Check if the product matches the criteria for each specified attribute
                if (name is None or name.lower() in product.name.lower()) and \
                (price_min is None or product.get_price() >= price_min) and \
                (price_max is None or product.get_price() <= price_max) and \
                (brand is None or brand.lower() in product.brand.lower()) and \
                (description is None or description.lower() in product.description.lower()) and \
                (store is None or store.lower() in product.store.lower()) and \
                (url is None or url== product.url) and \
                (image_url is None or image_url == product.image_url) :
                    matching_products.append(product)
                    if product.get_price()<=best_store_price:
                        best_store_price=product.get_price()
                        best_store_product=product
            useful_products.append(matching_products)
            best_products.append(best_store_product)
        self.products=useful_products
        return best_products
    def search_by_query(self, query):
        """Searches for products in the cart based on a general query string."""
        matching_products = []
        for product in self.all_products:
            if query.lower() in product.name.lower() or \
               query.lower() in product.brand.lower() or \
               query.lower() in product.description.lower() or \
               query.lower() in product.store.lower() :
                matching_products.append(product)
        return matching_products
    def set_products(self,csv_files):
        """this function re ds the csv files and set products  """
        """Charge les produits à partir des fichiers CSV et les ajoute à self.products."""
        for csv_file in csv_files:
            store_products=[]
            with open(csv_file, 'r', newline='', encoding='latin1') as file:
                """reader = csv.reader(file)
                next(reader)  # Skip header row if present"""
                reader = csv.DictReader(csv_file)
                for row in reader:
                    print("Nom : " + row['Nom'], "Marque : " + row['Marque'], "Prix : " + row['Prix'], "Description : " + row['Description'], "url : " + row['Url'], "Url image : " + row['Url_image'])
                """for row in reader:
                   # Créer une instance de Product à partir des données du fichier CSV
                   print(row)
                   print(len(row[0].split(',')))
                   print(len(row))
                   product = Product(
                        name=row[0],
                        brand=row[1],
                        price=float(row[2].replace('€', '').replace(',', '').strip()),
                        description=row[3],
                        store='',
                        url=row[4],
                        image_url=row[5]
                    )
                   store_products.append(product)
            # Ajouter les produits à self.products       
            self.products.append(store_products)"""
    def fill_the_demand(self):
        """Calculates the total price of the products for the given demands."""
        demand=self.demand
        best_products=self.search_product_by_attributes( name=demand.get_name(),price_min=0, price_max=demand.get_budget_limit(), brand=demand.get_brand(), description=None, store=demand.get_store(), url=None, image_url=None)
        sorted_products=[]
        # Sort the list of products based on their price attribute
        print(best_products)
        sorted_products = sorted(best_products, key=lambda x: x.get_price())
        return sorted_products


""" cette liste est déjà triée """
if __name__ == "__main__": 
   
    # Créer une instance de Demand
    demand = Demand(
    name="laptop",
    brand="asus",
    budget_limit=99,
    store=""
)
    # Créer une instance de Cart avec la demande
    cart = Cart(demand)
    # Chemin relatif des fichiers CSV dans le même répertoire que le script principal
    csv_files = [
        os.path.join(os.path.dirname(__file__), 'alternate_asus.csv')

    ]
    # Charger les produits à partir des fichiers CSV
    cart.set_products(csv_files)
    sorted_products=cart.fill_the_demand()

    # Afficher les produits du panier
    print("Products in the cart:")
    for store_products in cart.get_products():
        for product in store_products: 
            print(product.get_id(),product.get_name(), product.get_brand(), product.get_price(),product.get_description())
    print("Products sorted")
    for product in sorted_products:
        print(product.get_name(), product.get_brand(), product.get_price())