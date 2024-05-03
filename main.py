import numpy as np 
from analyses.product import Product
from analyses.demand import Demand
from analyses.cart import Cart
from datetime import date
from scraping.Site import Site
from interface.interface import ShoppingApp

app = ShoppingApp()

user_information = app.comparison_information
print(f"informations : {user_information}")