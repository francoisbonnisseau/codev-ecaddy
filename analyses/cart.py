# cart.py
from product import Product
from demand import Demand
class Cart:
    all_products = []

    """classmethod"""
    def initialize_all_products(cls, all_products):
        """Initialize the list of all products."""
        cls.all_products = all_products

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a product to the cart."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the cart."""
        self.products.remove(product)

    def search_product_by_attributes(self, name=None, price_min=None, price_max=None, brand=None, description=None, store=None, url=None, image_url=None, nature=None):
        """Searches for products in the cart based on specified attributes."""
        matching_products = []
        for product in self.all_products:
            # Check if the product matches the criteria for each specified attribute
            if (name is None or name.lower() in product.name.lower()) and \
               (price_min is None or product.price >= price_min) and \
               (price_max is None or product.price <= price_max) and \
               (brand is None or brand == product.brand) and \
               (description is None or description.lower() in product.description.lower()) and \
               (store is None or store.lower() in product.store.lower()) and \
               (url is None or url== product.url) and \
               (image_url is None or image_url == product.image_url) and \
               ( nature is None or nature.lower() in product.nature.lower()):
                matching_products.append(product)
        return matching_products
    def search_by_query(self, query):
        """Searches for products in the cart based on a general query string."""
        matching_products = []
        for product in self.all_products:
            if query.lower() in product.name.lower() or \
               query.lower() in product.brand.lower() or \
               query.lower() in product.description.lower() or \
               query.lower() in product.store.lower() or \
               query.lower() in product.nature.lower():
                matching_products.append(product)
        return matching_products
    def get_products_by_store(self, store_name):
        """Returns products from the given store."""
        return search_product_by_attributes(store=store_name)
    def fill_the_demand(self, demands):
        """Calculates the total price of the products for the given demands."""
        self.products=[]
        total_price=0
        for demand in demands:
            products_founded = self.search_product_by_attributes(self, name=demand.get_name(),price_min=None, price_max=demand.price_per_unit(), brand=demand.get_brand(), description=None, store=demand.get_store(), url=None, image_url=None, nature=demand.get_nature())
            cheapest_product = self.all_products[0]  # Initialize with the first product
            for product in products_founded[1:]:
                if product.price < cheapest_product.price:
                    cheapest_product = product
            self.products.append((cheapest_product,demand.get_quantity()))
            total_price += demand.get_quantity()* cheapest_product.get_price()
        return total_price