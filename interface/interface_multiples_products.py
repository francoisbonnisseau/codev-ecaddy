from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Checkbutton, BooleanVar, Scrollbar
from pathlib import Path
import threading
import json
import sys
import numpy as np 
from datetime import date
from results_interface import ResultsInterface
from windowError import WindowError
sys.path.append("..")
from scraping.Site import Site
from scraping import *
sys.path.append("..")
from analyses.product import Product
from analyses.demand import Demand
from analyses.cart import Cart



class Block:
    def __init__(self, canvas, window, current_y_position, add_block, images):
        self.canvas = canvas
        self.window = window
        self.current_y_position = current_y_position
        self.add_block = add_block
        self.previous_add_button = None
        self.block_images = []
        self.images = images
        self.product_inputs = []
        self.brand_inputs = []
        self.price_inputs = []

    def add(self):
        #supprimer le bouton add_item du bloc précédent si c'est au moins le deuxieme bloc
        if self.previous_add_button:
            self.previous_add_button.destroy()
        
        # créer les éléments d'un bloc
        self.canvas.create_rectangle(
            81.0,
            self.current_y_position + 217.9999999999999,
            556.0,
            self.current_y_position + 219.0,
            fill="#1EBA65",
            outline=""
        )
        
        add_item_button = Button(
            self.window,
            image=self.images['button_image_1'],
            borderwidth=0,
            highlightthickness=0,
            command=self.add_block,
            relief="flat"
        )
        add_item_button.place(
            x=309.0,
            y=self.current_y_position + 240.0,
            width=28.0,
            height=28.0
        )
        self.previous_add_button = add_item_button
        
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png")
        )
        entry_bg_1 = self.canvas.create_image(
            219.5,
            self.current_y_position + 186.0,
            image=entry_image_1
        )
        product_input = Entry(
            self.window,
            bd=0,
            bg="#D3D3D3",
            fg="#000716",
            highlightthickness=0
        )
        self.product_inputs.append(product_input)
        product_input.place(
            x=120.0,
            y=self.current_y_position + 172.0,
            width=199.0,
            height=26.0
        )
        self.block_images.append((entry_image_1,))
        
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png")
        )
        entry_bg_2 = self.canvas.create_image(
            411.0,
            self.current_y_position + 186.0,
            image=entry_image_2
        )
        brand_input = Entry(
            self.window,
            bd=0,
            bg="#D3D3D3",
            fg="#000716",
            highlightthickness=0
        )
        self.brand_inputs.append(brand_input)
        brand_input.place(
            x=356.0,
            y=self.current_y_position + 172.0,
            width=110.0,
            height=26.0
        )
        
        self.block_images.append((entry_image_2,))
        
        entry_bg_3 = self.canvas.create_image(
            550.0,
            self.current_y_position + 186.0,
            image=entry_image_2
        )
        price_input = Entry(
            self.window,
            bd=0,
            bg="#D3D3D3",
            fg="#000716",
            highlightthickness=0
        )
        self.price_inputs.append(price_input)
        price_input.place(
            x=500.0,
            y=self.current_y_position + 172.0,
            width=110.0,
            height=26.0
        )
        
        self.block_images.append((entry_image_2,))
        
        
        self.canvas.create_text(
            114.0,
            self.current_y_position + 152.0,
            anchor="nw",
            text="Nom du produit *",
            fill="#000000",
            font=("Inter Medium", 14 * -1)
        )
        
        self.canvas.create_text(
            350.0,
            self.current_y_position + 152.0,
            anchor="nw",
            text="Marque",
            fill="#000000",
            font=("Inter Medium", 14 * -1)
        )
        
        self.canvas.create_text(
            500.0,
            self.current_y_position + 152.0,
            anchor="nw",
            text="Prix minimum",
            fill="#000000",
            font=("Inter Medium", 14 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png")
        )
        
        self.block_images.append((button_image_2,))
        
        self.current_y_position += 100

    def get_product_brand_inputs(self):
        product_inputs = [entry.get() for entry in self.product_inputs]
        brand_contents = [entry.get() for entry in self.brand_inputs]
        min_price_content = [entry.get() for entry in self.price_inputs]
        product_brand_inputs = [[product_inputs[i],brand_contents[i],min_price_content[i]] for i in range(len(product_inputs))]
        return product_brand_inputs

#création de la classe Shopping app qui va contenir l'interface graphique
class ShoppingApp:
    def __init__(self):
        self.sites_repertory = ['boulanger', 'cybertech', 'grosbill', 'materiel', 'alternate']
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.geometry("973x605")
        self.window.configure(bg="#FFFFFF")      

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=605,
            width=973,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Add text and buttons
        self.canvas.create_rectangle(
            0.0,
            0.0,
            973.0,
            73.0,
            fill="#1EBA65",
            outline=""
        )
        self.canvas.create_text(
            266.0,
            27.0,
            anchor="nw",
            text="Ecaddy - outil de shopping pour le matériel informatique",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            31.0,
            116.0,
            anchor="nw",
            text="CHOISIR DES PRODUITS",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            770.0,
            177.0,
            anchor="nw",
            text="Alternate",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            667.0,
            116.0,
            anchor="nw",
            text="CHOISIR DES MAGASINS",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            770.0,
            225.0,
            anchor="nw",
            text="Boulanger",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            770.0,
            273.0,
            anchor="nw",
            text="CyberTech",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            770.0,
            321.0,
            anchor="nw",
            text="GrosBill",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
            770.0,
            369.0,
            anchor="nw",
            text="Materiel.net",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )

        self.checkbox_boulanger_state = BooleanVar()  
        self.checkbox_boulanger = Checkbutton(
            self.window,
            variable=self.checkbox_boulanger_state,
            onvalue=True,
            offvalue=False,
            height=2,
            width=2,
            bg="#fff",
            activebackground="#fff",
            highlightthickness=0
        )
        self.checkbox_boulanger.place(x=715.0, y=220.0)

        self.checkbox_cybertech_state = BooleanVar()  
        self.checkbox_cybertech = Checkbutton(
            self.window,
            variable=self.checkbox_cybertech_state,            
            onvalue=True,
            offvalue=False,
            height=2,
            width=2,
            bg="#fff",
            activebackground="#fff",
            highlightthickness=0
        )
        self.checkbox_cybertech.place(x=715.0, y=268.0)

        self.checkbox_grosbill_state = BooleanVar()  
        self.checkbox_grosbill = Checkbutton(
            self.window,
            variable=self.checkbox_grosbill_state,
            onvalue=True,
            offvalue=False,
            height=2,
            width=2,
            bg="#fff",
            activebackground="#fff",
            highlightthickness=0
        )
        self.checkbox_grosbill.place(x=715.0, y=316.0)

        self.checkbox_materiel_state = BooleanVar()  
        self.checkbox_materiel = Checkbutton(
            self.window,
            variable=self.checkbox_materiel_state,
            onvalue=True,
            offvalue=False,
            height=2,
            width=2,
            bg="#fff",
            activebackground="#fff",
            highlightthickness=0
        )
        self.checkbox_materiel.place(x=715.0, y=364.0)

        self.checkbox_alternate_state = BooleanVar()  
        self.checkbox_alternate = Checkbutton(
            self.window,
            variable=self.checkbox_alternate_state,
            onvalue=True,
            offvalue=False,
            height=2,
            width=2,
            bg="#fff",
            activebackground="#fff"
        )
        self.checkbox_alternate.place(x=715.0, y=172.0)

        self.canvas.create_rectangle(
            641.0,
            66.0,
            647.0000000000001,
            650.0216064453125,
            fill="#1EBA65",
            outline=""
        )

        self.current_y_position = 0
        self.images = {
            'button_image_1': PhotoImage(file=relative_to_assets("button_1.png")),
            'entry_image_1': PhotoImage(file=relative_to_assets("entry_1.png")),
            'entry_image_2': PhotoImage(file=relative_to_assets("entry_2.png")),
            'button_image_2': PhotoImage(file=relative_to_assets("button_2.png"))
        }
        self.block = Block(self.canvas, self.window, self.current_y_position, self.add_block, self.images)
        
        self.add_block()

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png")
        )
        self.comparer = Button(
            self.window,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.compare,
            relief="flat"
        )
        self.comparer.place(
            x=670.0,
            y=509.0,
            width=174.0,
            height=64.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def on_close(self):
        # Appelé lors de la fermeture de la fenêtre Tkinter
        self.window.destroy()
    
    def add_block(self):
        self.block.add()

    def create_demands(self):
        # Convert comparison information into demand objects
        writen_demands = [{'name': writen_demand[0], 'brand': writen_demand[1], 'price_min': writen_demand[2]} 
                        for writen_demand in self.comparison_information['products']]
        demands = []
        for writen_demand in writen_demands:
            price_min_demand = 0 if not isinstance(writen_demand['price_min'], int) else writen_demand['price_min']
            the_demand = Demand(
                name=writen_demand['name'], 
                brand=writen_demand['brand'], 
                budget_limit=np.inf,  # Set to infinity, adjust if needed
                store='', 
                quantity=1, 
                price_min=price_min_demand
            )
            demands.append(the_demand)
        return demands

    def fill_delivery(self, demand, csv_files):
        cart = Cart(demand)
        cart.set_products(csv_files)
        sorted_products = cart.fill_the_demand()
        return sorted_products

    def compare(self):
        with open('site_information.json', 'r') as infos_file:
            self.site_information = json.load(infos_file)

        materiel_net = Site.Site('materiel', self.site_information['materiel']['base_url'], self.site_information['materiel']['search_url'], self.site_information['materiel']['selectors'])
        boulanger = Site.Site('boulanger', self.site_information['boulanger']['base_url'], self.site_information['boulanger']['search_url'], self.site_information['boulanger']['selectors'])
        grosbill = Site.Site('grosbill', self.site_information['grosbill']['base_url'], self.site_information['grosbill']['search_url'], self.site_information['grosbill']['selectors'])
        cybertech = Site.Site('cybertech', self.site_information['cybertech']['base_url'], self.site_information['cybertech']['search_url'], self.site_information['cybertech']['selectors'])
        alternate = Site.Site('alternate', self.site_information['alternate']['base_url'], self.site_information['alternate']['search_url'], self.site_information['alternate']['selectors'])

        if self.window.winfo_exists():
            self.comparison_information = {'products': [], 'sites': []}
            self.comparison_information['products'] = [product for product in self.block.get_product_brand_inputs() if product[0] != '']
            
            for site in self.sites_repertory: 
                checkbox = getattr(self, 'checkbox_' + site + '_state')
                if checkbox.get():
                    self.comparison_information['sites'].append(site)
            
            print(self.comparison_information)

            if self.comparison_information and self.comparison_information['sites']:
                for product in self.comparison_information['products']:
                    for site in self.comparison_information['sites']:
                        if site == 'materiel':
                            materiel_net.write_data(product[0] + "_" + product[1])
                            print(f'materiel scraped for product {product[0]}')
                        elif site == 'boulanger':
                            boulanger.write_data(product[0] + "_" + product[1])
                            print(f'boulanger scraped for product {product[0]}')
                        elif site == 'grosbill':
                            grosbill.write_data(product[0] + "_" + product[1])
                            print(f'grosbill scraped for product {product[0]}')
                        elif site == 'cybertech':
                            cybertech.write_data(product[0] + "_" + product[1])
                            print(f'cybertech scraped for product {product[0]}')
                        elif site == 'alternate':
                            alternate.write_data(product[0] + "_" + product[1])
                            print(f'alternate scraped for product {product[0]}')

                demands = self.create_demands()
                today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")

                for demand in demands:
                    csv_files = []
                    key_word_research = demand.get_name() + "_" + demand.get_brand()
                    for web_site_name in self.comparison_information['sites']:
                        OUTPUT_PATH = Path(__file__).parent
                        csv_file = f"{OUTPUT_PATH}\\{today_date}\\{web_site_name}_{key_word_research}.csv"
                        csv_files.append(csv_file)

                    deliveries = self.fill_delivery(demand, csv_files)
                    
                    final_products = []
                    for product in deliveries:
                        final_products.append({
                            'name': product.get_name(),
                            'brand': product.get_brand(),
                            'price': product.get_price(),
                            'description': product.get_description(),
                            'url': product.get_url(),
                            'image_url': product.get_image_url(),
                            'store': product.get_store()
                        })

                    print(final_products)

                    # Open a ResultsInterface for each product
                    # ResultsInterface(final_products)
                    threading.Thread(target=ResultsInterface, args=(final_products,)).start()


def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_FOLDER = "assets/frame0"
    ASSETS_PATH = OUTPUT_PATH / ASSETS_FOLDER
    return ASSETS_PATH / Path(path)

if __name__ == "__main__":
    app = ShoppingApp()