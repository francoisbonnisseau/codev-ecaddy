import os
import csv
import sys
import numpy as np 
from product import Product
from demand import Demand
from cart import Cart 
from datetime import date

sys.path.append("..")

from scraping.Site import Site


def creat_demands():
    writen_demands= [{"name": 'name1', "brand": 'brand1'}, {"name": 'name2',"brand":'brand2'}]
    """we have to import  writen_demands from the interface """
    demands=[]
    for writen_demand in writen_demands:
        demand=demand(name= writen_demand["name"], brand=writen_demand["brand"] , budget_limit=np.inf, store='', quantity=1)
        demands.append(demand)
    return demands
Web_sites_name=['materiel', 'boulanger','grosbill','cybertech','alternate']
def send_requests(Name,Brand, Web_sites):
    #creation des instances de classe Site
    Web_sites_objects=[]
    for web_site_name in Web_sites_name:
        New_site= Site(web_site_name, site_information[web_site_name]['base_url'], site_information[web_site_name]['search_url'], site_information[web_site_name]['selectors'])
        Web_sites_objects.append(New_site)
    # Get product information
    key_word_research = Name+' '+Brand
    #search informtions in web sites and write the in a csv file 
    for site in Web_sites: 
        site.write_data(product_name=key_word_research)
    # precise the csv files names 
    csv_files=[]
    for web_site_name in Web_sites_name:
        today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")
        csv_file= folder_path = f"../{today_date}/{web_site_name}_{key_word_research}.csv"
        csv_files.append(csv_file)
    return csv_files
def fill_delivery(demands, web_sites):
    delivery=[] #list of products
    for demand in demands:
        cart=Cart(demand)
        csv_files=send_requests(demand.get_name(), demand.get_brand(), web_sites )
        cart.set_products(csv_files)
        sorted_products=cart.fill_the_demand()
        delivery.append(sorted_products[0])
    return delivery


"""how  to execute:
* pressing the compare botton
* we need a function that reads the writen demands from the client window and returns writen_demands as a list [ {name: 'name1';brand: 'brand1'}, {name: 'name2';brand:'brand2'}, ... ]
* creat demands 
* fill delevery 
* we have to creat a function that presents the results 
"""