# cart.py
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import csv
import numpy as np 
from product import Product
from demand import Demand
from datetime import date
class Cart:
    """
    This class represents a shopping cart for one demand.

    Attributes:
        products (list): A list containing products found after scraping. Each element of the list is a sublist
                         containing products from a specific store.
        demand (Demand): A demand object representing the requirements for the shopping cart.
    """
    def __init__(self,demand):
        self.products = []
        self.demand=demand
    def get_products(self):
        """Get the products in the cart."""
        return self.products

    def get_demand(self):
        """Get the demand associated with the cart."""
        return self.demand

    def set_demand(self, demand):
        """Set the demand associated with the cart."""
        self.demand = demand
    
    def add_product(self, product, store):
        """Add a product to the cart."""
        for store_products in self.products:
            if store_products and store_products[0].get_store() == store:
                store_products.append(product)
                return
        # If no inner list exists for the given store, create a new one
        self.products.append([product])


    def remove_product(self, product):
        """Remove a product from the cart."""
        for store_products in self.products:
            if product in store_products:
                store_products.remove(product)
            if len(store_products)==0:
                self.products.remove(store_products)

    def filter_products(self, name=None, price_min=None, price_max=None, brand=None, description=None, store=None, url=None, image_url=None):
        """
        Retrieves all products in the cart that match the specified criteria.
        
        Args:
            name (str, optional): The name of the product to filter by.
            price_min (float, optional): The minimum price of the product to filter by.
            price_max (float, optional): The maximum price of the product to filter by.
            brand (str, optional): The brand of the product to filter by.
            description (str, optional): The description of the product to filter by.
            store (str, optional): The store where the product is available to filter by.
            url (str, optional): The URL of the product to filter by.
            image_url (str, optional): The image URL of the product to filter by.
        """
        matching_products = []
        for store_products in self.products:
            for product in store_products:
                # Check if the product matches the criteria for each specified attribute
                if (name is None or name.lower() in product.get_name().lower()) and \
                   (price_min is None or product.get_price() >= price_min) and \
                   (price_max is None or product.get_price() <= price_max) and \
                   (brand is None or brand.lower() in product.get_brand().lower()) and \
                   (description is None or description.lower() in product.get_description().lower()) and \
                   (store is None or store.lower() in product.get_store().lower()) and \
                   (url is None or url == product.get_url()) and \
                   (image_url is None or image_url == product.get_image_url()):
                    matching_products.append(product)
        return matching_products
    

    def search_product_by_attributes(self, name=None, price_min=None, price_max=None, brand=None, description=None, store=None, url=None, image_url=None):
        """Searches for products in the cart based on specified attributes. and returns the best product from each list
        """
        #a list of filtred products i have the same structure of the attribute products  
        useful_products=[]
        # a list of best prodcut of each store  
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
            if best_store_price != np.inf : 
                useful_products.append(matching_products)
                best_products.append(best_store_product)
            else: 
                best_products.append(None)
        #self.products=useful_products
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
    
    def correspondPrice (self, SPrice, store):  
        if store in ["cybertech","grosbill"]:
            return float(SPrice.replace(' ', '').replace('€', '.').strip())
        if store == "boulanger":
            return float(SPrice.replace(',','.').replace(' ', '').replace('€', '').strip())
        if store == "alternate":
            return float(SPrice.replace('.','').replace(' ', '').replace('€', '').replace(',', '.').strip())
        if store == "materiel":
            #print(float(SPrice.replace(' ', '').replace('€', '.').replace('\xa0', '').replace('â‚¬', '').strip()))
            return float(SPrice.replace(' ', '').replace('€', '.').replace('\xa0', '').replace('â‚¬', '').strip())
    
    def set_products(self,csv_files):
        """this function reads the csv files and set the attribute products  """
        """Charge les produits à partir des fichiers CSV et les ajoute à self.products."""
        self.products=[]
        for csv_file in csv_files:
            store_products=[]
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                #next(reader)  # Skip header row if present
                for row in reader:
                    product = Product(
                        name=row['Nom'],
                        brand=row['Marque'],
                        price=self.correspondPrice (row['Prix'], os.path.basename(csv_file).split("_")[0]) ,
                        description=row['Description'],
                        store= os.path.basename(csv_file).split("_")[0],
                        url=row['Url'],
                        image_url=row['Url_image']
                    )
                    store_products.append(product)
            # Ajouter les produits à self.products       
            self.products.append(store_products)
    
    def fill_the_demand(self):
        """Calculates the total price of the products for the given demands.
        best_products is a list that contains all the products that match the filtres 
        this function retruns sorted list of products that matches the critireas 
        """
        demand=self.demand
        best_products=self.filter_products( name=demand.get_name(),price_min=demand.get_price_min(), price_max=demand.get_budget_limit(), brand=demand.get_brand(), description=None, store=demand.get_store(), url=None, image_url=None)
        sorted_products=[]
        # Sort the list of products based on their price attribute
        if None not in best_products:
            sorted_products = sorted(best_products, key=lambda x: x.get_price())
        return sorted_products
    


    def fill_the_demand_1(self):
        """Calculates the total price of the products for the given demands.
        best_products is a list that contains all the products that match the filtres 
        this function retruns sorted list of products(one from each web_site) that matches the critireas 
        """
        demand=self.demand
        best_products=self.search_product_by_attributes( name=demand.get_name(),price_min=demand.get_price_min(), price_max=demand.get_budget_limit(), brand=demand.get_brand(), description=None, store=demand.get_store(), url=None, image_url=None)
        
        return best_products


if __name__ == "__main__": 
    # Créer une instance de Demand
    demand = Demand(name="Lap", brand="asus",budget_limit=900,store="")
    # Créer une instance de Cart avec la demande
    cart = Cart(demand)
    # Chemin relatif des fichiers CSV dans le même répertoire que le script principal
    today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")
    csv_files = [ os.path.join(os.path.dirname(__file__), "materiel_asus_for_test.csv")]
    print(csv_files)
    # Charger les produits à partir des fichiers CSV
    cart.set_products(csv_files)
    # Récupérer les produits triés selon la demande
    sorted_products = cart.fill_the_demand()
    # Afficher les produits du panier
    print("Products in the cart:")
    for store_products in cart.get_products():
        for product in store_products: 
            print(product.get_id(), product.get_name(), product.get_brand(), product.get_price(), product.get_description())
    # Afficher les produits triés
    print("All Products sorted:")
    for product in sorted_products:
        print(product.get_name(), product.get_brand(), product.get_price())
    # Vérifier que les produits sont triés par prix croissant
    prices = [product.get_price() for product in sorted_products]
    assert prices == sorted(prices), "Products are not sorted by price"
    print("Test passed: Select matching products and sort them ")

    # Récupérer les produits triés selon la demande
    sorted_products = cart.fill_the_demand_1()
    # Afficher les produits triés
    print("Best Products sorted:")
    for product in sorted_products:
        print(product.get_name(), product.get_brand(), product.get_price())
    assert len(sorted_products)==1, "Products are not sorted by price"
    print("Test passed: Select best product from each web site ")
