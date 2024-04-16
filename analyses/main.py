import os
import csv
import numpy as np 
from product import Product
from demand import Demand
from cart import Cart 


def send_requests(demand):
     
    return csv_files 

def fill_delivery(demands):
    delivery=[] #list of products
    for demand in demands: 
        cart=Cart(demand)
        csv_files=send_requests(demand)
        cart.set_products(csv_files)
        sorted_products=cart.fill_the_demand()
        delivery.append(sorted_products[0])
    return delivery