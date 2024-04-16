import os
import csv
import numpy as np 
from product import Product
from demand import Demand
from cart import Cart 
 
def fill_delivery(demands):
    delivery=[] #list of products
    for demand in demands: 
        cart=Cart(demand)
        csv_files=fill_csv(demand)
        cart.set_products(csv_files)
        sorted_products=cart.fill_the_demand()
        delivery.append(sorted_products[0])
    return delivery