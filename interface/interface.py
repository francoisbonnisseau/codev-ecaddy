import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Checkbutton, BooleanVar, Scrollbar
from pathlib import Path
import json
import sys
import numpy as np 
from datetime import date
from windowError import WindowError
from results_interface_errors import ResultsInterface
from best_path_interface import MultipleProductsInterface
import pulp
import threading
#import queue
sys.path.append("..")
from scraping.Site import Site
from scraping import *
sys.path.append("..")
from analyses.product import Product
from analyses.demand import Demand
from analyses.cart import Cart



class Block:
     def __init__(self, canvas, window, current_y_position, add_block, images):
        """
        Initialize a Block object.

        Parameters:
        - canvas: Canvas object where elements will be drawn.
        - window: Tkinter window.
        - current_y_position: Current vertical position on the canvas.
        - add_block: Function to add another block.
        - images: Dictionary containing image paths.
        """
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
        """
        Add a new block to the canvas.
        """
        # Remove the previous "Add" button if it exists
        if self.previous_add_button:
            self.previous_add_button.destroy()
        
        # Draw rectangle to visually separate each block
        self.canvas.create_rectangle(
            81.0,
            self.current_y_position + 217.9999999999999,
            556.0,
            self.current_y_position + 219.0,
            fill="#1EBA65",
            outline=""
        )

        # Create an "Add" button for adding more blocks
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
        
        # Create input field for product name
        
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
        
        # Create input field for brand
        
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
        
        # Create input field for price
        
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
        
        # Add labels for input fields
        
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
        # Update the current_y_position for the next block
        self.current_y_position += 100

     def get_product_brand_inputs(self):
        """Function to retrieve product, brand, and minimum price inputs from the block"""
        product_inputs = [entry.get() for entry in self.product_inputs]
        brand_contents = [entry.get() for entry in self.brand_inputs]
        min_price_content = [entry.get() for entry in self.price_inputs]
        product_brand_inputs = [[product_inputs[i],brand_contents[i],min_price_content[i]] for i in range(len(product_inputs))]
        return product_brand_inputs

#création de la classe Shopping app qui va contenir l'interface graphique
class ShoppingApp:
    def __init__(self):
        """ 
    This class represents the main shopping application.

    Attributes:
        sites_repertory (list): A list of available websites for comparison.
        window (Tk): The main Tkinter window.
        canvas (Canvas): The canvas widget for displaying elements.
        checkbox_boulanger_state (BooleanVar): State variable for Boulanger checkbox.
        checkbox_cybertech_state (BooleanVar): State variable for CyberTech checkbox.
        checkbox_grosbill_state (BooleanVar): State variable for GrosBill checkbox.
        checkbox_materiel_state (BooleanVar): State variable for Materiel checkbox.
        checkbox_alternate_state (BooleanVar): State variable for Alternate checkbox.
        current_y_position (int): Current y-coordinate position.
        images (dict): A dictionary containing images used in the application.
        block (Block): An instance of the Block class for managing product blocks.
        comparer (Button): Button for initiating product comparison.
    """

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

        # creat green rectongle and its text 
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
        #right column
       
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
            177.0,
            anchor="nw",
            text="Alternate",
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

        
        #checkboxes for the roght column 
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
        # main session
        self.canvas.create_text(
            31.0,
            116.0,
            anchor="nw",
            text="CHOISIR DES PRODUITS",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )

        # Set initial y-coordinate position to 0
        self.current_y_position = 0

        # Load images for buttons and entry fields
        self.images = {
            'button_image_1': PhotoImage(file=relative_to_assets("button_1.png")),
            'entry_image_1': PhotoImage(file=relative_to_assets("entry_1.png")),
            'entry_image_2': PhotoImage(file=relative_to_assets("entry_2.png")),
            'button_image_2': PhotoImage(file=relative_to_assets("button_2.png"))
        }
        # Create a Block instance to manage product blocks
        self.block = Block(self.canvas, self.window, self.current_y_position, self.add_block, self.images)
         # Add an initial block
        self.add_block()
        # Create and place a button for initiating product comparison
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
        # Disable window resizing
        self.window.resizable(False, False)
        # Start the Tkinter event loop
        self.window.mainloop()

    def on_close(self):
        """
        Called when the Tkinter window is closed.
        Destroys the Tkinter window.
        """
        self.window.destroy()
    
    def add_block(self):
        """
        Adds a new block to the interface.
        """
        self.block.add()
    def to_int_or_zero(self,value):
        """
        Converts a value to an integer or returns 0 if conversion fails.

        Args:
            value: The value to convert.

        Returns:
            int: The integer value if conversion succeeds, otherwise 0.
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0
    
    def create_demands(self):
        """
        Creates demand objects based on user input.

        Returns:
            list: A list of Demand objects.
        """
        writen_demands=[ {'name': writen_demand[0], 'brand': writen_demand[1],'price_min': self.to_int_or_zero(writen_demand[2])}  for writen_demand in self.comparison_information['products'] ]
        """we have to import  writen_demands from the interface """
        demands=[]
        for writen_demand in writen_demands:
            the_demand=Demand(name= writen_demand['name'], brand=writen_demand['brand'] , budget_limit=np.inf, store='', quantity=1, price_min=writen_demand['price_min'])
            demands.append(the_demand)
        return demands
    
    def fill_delivery(self, demand, csv_files):
        """
        Fills the delivery with sorted products based on the demand.

        Args:
            demand: The demand object.
            csv_files: The paths to the CSV files containing product information.

        Returns:
            list: A list of sorted products.
        """
        cart=Cart(demand)
        cart.set_products(csv_files)
        sorted_products=cart.fill_the_demand()
        return sorted_products

    def load_site_information(self):
        """
        Loads site properties from a JSON file.
        """
        with open('site_information.json', 'r') as infos_file:
            self.site_information = json.load(infos_file)
            #print(site_information)
            # print(json.dumps(site_information, indent=4, sort_keys=True))
    
    def get_comparison_information(self):
        """
        Retrieves comparison information including demanded products and selected sites.
        """
        
        self.comparison_information = {'products':[] , 'sites':[]}
        #on ajoute le produit à la liste si le nom du produit n'est pas vide. On autorise une marque vide
        self.comparison_information['products'] = [product for product in self.block.get_product_brand_inputs()
                                            if product[0] != '']
        
        for site in self.sites_repertory: 
            checkbox = getattr(self, 'checkbox_' + site + '_state')
            if checkbox.get():
                self.comparison_information['sites'].append(site)
        
        
        
        # print(self.comparison_information)
    
    def get_status(self):
        """
        Retrieves the status to know if the scraping can start and throws an error if no product or no site is selected.

        Returns:
            bool: The status of the application.
        """
        if not self.comparison_information['products']:
            WindowError("Veuillez ajouter au moins un produit à comparer.")
            return False
        
        if not self.comparison_information['sites']:
            WindowError("Veuillez sélectionner au moins un site pour la recherche.")
            return False
        
        return True
            
    def scrape_product(self, product, site, sites_might_be_scrapped):
        """
        Scrapes product information from a given site.

        Args:
            product: The product name.
            site: The site to scrape.
            sites_might_be_scrapped: List of Site objects.

        Raises:
            Exception: If scraping encounters an error.
        """
        for object_site in sites_might_be_scrapped: 
            if site==object_site.nom:
                object_site.write_data(product)
        

    def perform_scraping(self,sites_might_be_scrapped):
        """
        Performs scraping of products from selected sites.

        Args:
            sites_might_be_scrapped: List of Site objects.
        """
        for product in self.comparison_information['products']:
            for site in self.comparison_information['sites']:
                try:
                    self.scrape_product(product[0] + "_" + product[1], site, sites_might_be_scrapped)
                    print(f'{site} scraped for product {product[0]}')
                except Exception as e:
                    print(f'error while scraping {site} for product {product[0]}: {e}')
                    WindowError(f'error while scraping {site} for product {product[0]}: {e}')
                    
    def get_csv_paths(self,demand):
        """
        Generates paths to CSV files based on demand.

        Args:
            demand: The demand object.

        Returns:
            list: A list of CSV file paths.
        """
        today_date = date.today().strftime("%d/%m/%Y").replace("/", "_")
        csv_files = []
        key_word_research = demand.get_name() + "_" + demand.get_brand()
        for web_site_name in self.comparison_information['sites']:
            OUTPUT_PATH = Path(__file__).parent
            if os.name == 'posix':
                csv_file = f"{OUTPUT_PATH}/{today_date}/{web_site_name}_{key_word_research}.csv"
            else:
                csv_file = f"{OUTPUT_PATH}\\{today_date}\\{web_site_name}_{key_word_research}.csv"
            csv_files.append(csv_file)
        return csv_files
    def get_deliveries(self, demands):
        """
        Generates deliveries for each demand.

        Args:
            demands: List of demand objects.

        Returns:
            list: A list of deliveries.
        """
        deliveries = []
        for demand in demands:
            csv_files = self.get_csv_paths(demand)
            deliveries.append(self.fill_delivery(demand, csv_files))
        return deliveries
    def get_best_product_from_each_web( self, demand, csv_files):
        """
        Retrieves the best products from each web for a given demand.

        Args:
            demand: The demand object.
            csv_files: List of CSV file paths.

        Returns:
            list: A list of best products.
        """
        self.cart=Cart(demand)
        self.cart.set_products(csv_files)
        best_products=self.cart.fill_the_demand_1()
        return best_products
    def get_best_delivery_from_each(self , demands):
        """
        Generates the best delivery from each demand.

        Args:
            demands: List of demand objects.

        Returns:
            list: A matrix of best deliveries.
        """
        deliveries_matrix = []
        for demand in demands:
            csv_files = self.get_csv_paths(demand)
            best_product_from_each_web=self.get_best_product_from_each_web(demand,csv_files)
            deliveries_matrix.append(best_product_from_each_web)
        deliveries_matrix = list(map(list, zip(*deliveries_matrix)))
        return deliveries_matrix
    
    def optimise_path(self, deliveries_matrix, web_site_costs):
        """
        Optimizes the delivery path to minimize costs.

        Args:
            deliveries_matrix: Matrix of best deliveries.
            web_site_costs: List of costs associated with each web site.

        Returns:
            tuple: A tuple containing the optimized result matrix and y_results.
        """
        num_demands = len(deliveries_matrix[0])
        num_web_sites = len(deliveries_matrix)
        # Create the LP problem
        prob = pulp.LpProblem("Minimize_Delivery_Costs", pulp.LpMinimize)
        # Define decision variables
        x = pulp.LpVariable.dicts("x",  ((i, j) for i in range(num_web_sites) for j in range(num_demands)), cat="Binary")    
        y = pulp.LpVariable.dicts("y", (i for i in range(num_web_sites)), cat="Binary")
        large_value=1e6
        # Define the objective function
        prob += pulp.lpSum([(deliveries_matrix[i][j].get_price() if deliveries_matrix[i][j] is not None else large_value) * x[i, j] for i in range(num_web_sites) for j in range(num_demands)] + [web_site_costs[i] * y[i] for i in range(num_web_sites)])
        # Add constraints
        # Each demand must be satisfied exactly once
        for j in range(num_demands):
            prob += pulp.lpSum([x[i, j] for i in range(num_web_sites)]) == 1, f"Demand_{j}_Constraint"
        # Link x and y variables
        for i in range(num_web_sites):
            for j in range(num_demands):
                prob += x[i, j] <= y[i], f"Link_x_y_{i}_{j}"
        # Solve the problem
        prob.solve()
        # Extract the results
        result_matrix = [[0] * num_demands for _ in range(num_web_sites)]
        for i in range(num_web_sites):
            for j in range(num_demands):
                result_matrix[i][j] = pulp.value(x[i, j])
        # Extract the y variable results
        y_results = [pulp.value(y[i]) for i in range(num_web_sites)]
        return result_matrix, y_results
    def get_best_sum(self, deliveries_matrix, web_site_costs):
        """
        Calculates the best sum of products to buy.

        Args:
            deliveries_matrix: Matrix of best deliveries.
            web_site_costs: List of costs associated with each web site.

        Returns:
            list: A list of best products to buy.
        """
        result_matrix, y_results = self.optimise_path(deliveries_matrix, web_site_costs)
        products_to_buy = []
        num_web_sites = len(deliveries_matrix)
        num_demands = len(deliveries_matrix[0])
        products_to_buy= [deliveries_matrix[i][j] for j in range(num_demands) for i in range(num_web_sites) if result_matrix[i][j] == 1]
        return products_to_buy
    
    def compare(self):
        """
        Compares products across selected websites and performs optimization.
        """
        self.load_site_information()

        #Setup web sites 
        materiel_net = Site.Site('materiel', self.site_information['materiel']['base_url'], self.site_information['materiel']['search_url'], self.site_information['materiel']['selectors'])
        boulanger = Site.Site('boulanger', self.site_information['boulanger']['base_url'], self.site_information['boulanger']['search_url'], self.site_information['boulanger']['selectors'])
        grosbill = Site.Site('grosbill', self.site_information['grosbill']['base_url'], self.site_information['grosbill']['search_url'], self.site_information['grosbill']['selectors'])
        cybertech = Site.Site('cybertech', self.site_information['cybertech']['base_url'], self.site_information['cybertech']['search_url'], self.site_information['cybertech']['selectors'])
        alternate = Site.Site('alternate', self.site_information['alternate']['base_url'], self.site_information['alternate']['search_url'], self.site_information['alternate']['selectors'])
        
        sites_might_be_scrapped=[materiel_net, boulanger,grosbill, cybertech, alternate]
        
        if self.window.winfo_exists():
            self.get_comparison_information()
            _status = self.get_status()
            if _status == True:
                # if it exists informations about available products and wanted web site let's perform the scrapping the the analyse  
                if(self.comparison_information and self.comparison_information['sites']):
                    #the scrapping
                    self.perform_scraping(sites_might_be_scrapped)
                    
                # creat demands 
                demands=self.create_demands()
                # match deliveries to products to deliveries 
                deliveries=self.get_deliveries(demands)

                for delivery in deliveries:
                    thread = threading.Thread(target=ResultsInterface, args=(delivery,))
                    thread.start()
                

                deliveries_matrix=self.get_best_delivery_from_each(demands)
                #print("this the matrix=" ,deliveries_matrix)
                
                if len(demands)>1: 
                    try: 
                        best_sum = self.get_best_sum(deliveries_matrix,[0]* len(self.comparison_information["sites"]))
                        thread=threading.Thread(target= MultipleProductsInterface, args=(best_sum,len(demands)))
                        thread.start()
                    except: 
                        return


def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_FOLDER = "assets/frame0"
    ASSETS_PATH = OUTPUT_PATH / ASSETS_FOLDER
    return ASSETS_PATH / Path(path)

if __name__ == "__main__":
    app = ShoppingApp()