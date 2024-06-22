from tkinter import VERTICAL, Scrollbar, Tk, Canvas, Button, Frame
from tkinter.ttk import Treeview
from windowError import WindowError
from pathlib import Path
import sys
sys.path.append("..")
from analyses.product import Product



class ResultsInterface:
    """Cette classe permet de créer une interface graphique pour afficher les résultats de la recherche de produits
    """
    def __init__(self, products):
        self.products = products

        if len(self.products) < 1:
            WindowError("Il semble qu'aucun produit n'ait été trouvé. Vérifiez votre connexion internet, ou bien choisissez plus de sites à scraper")
            return None
        
        self.window = Tk()
        self.window.geometry("973x605")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Vos résultats !")

        self.canvas = Canvas(self.window)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            973.0,
            73.0,
            fill="#B0E0C6",
            outline=""
        )
        self.canvas.create_text(
            431.0,
            27.0,
            anchor="nw",
            text="Vos résultats !",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )

        self.create_product_widgets()

        self.resultats = Button(
            self.canvas,
            bg="#1EBA65",
            text="Voir tous les résultats",
            borderwidth=0,
            highlightthickness=0,
            command=self.open_results_window,
            relief="flat"
        )

        self.resultats.place(
            x=360.0,
            y=530.0,
            width=300,
            height=64.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()
        

    def create_product_widgets(self):
        if len(self.products) >= 1:
            self.canvas.create_rectangle(
                40.0,
                97.0,
                933.0,
                251.0,
                fill="#1EBA65",
                outline=""
            )
            self.canvas.create_text(
                69.0,
                138.0,
                anchor="nw",
                text="1",
                fill="#FFFFFF",
                font=("Inter Black", 60 * -1)
            )
            self.canvas.create_text(
                151.0,
                118.0,
                anchor="nw",
                text=self.products[0].get_name().split(' ')[0],
                fill="#000000",
                font=("Inter Black", 30 * -1)
            )
            self.canvas.create_text(
                151.0,
                150.0,
                anchor="nw",
                text=self.products[0].get_brand(),
                fill="#000000",
                font=("Inter SemiBold", 15 * -1)
            )
            self.canvas.create_text(
                775.0,
                107.0,
                anchor="nw",
                text=self.products[0].get_price(),
                fill="#000000",
                font=("Inter Bold", 30 * -1)
            )
            self.canvas.create_text(
                766.0,
                195.0,
                anchor="nw",
                text=self.products[0].get_store(),
                fill="#FFFFFF",
                font=("Inter Medium", 20 * -1)
            )

        if len(self.products) >= 2:
            self.canvas.create_rectangle(
                40.0,
                275.0,
                555.0,
                516.0,
                fill="#B0DFC6",
                outline=""
            )
            self.canvas.create_text(
                69.0,
                295.0,
                anchor="nw",
                text="2",
                fill="#000000",
                font=("Inter Black", 60 * -1)
            )
            self.canvas.create_text(
                151.0,
                310.0,
                anchor="nw",
                text=self.products[1].get_name().split(' ')[0],
                fill="#000000",
                font=("Inter Black", 30 * -1)
            )
            self.canvas.create_text(
                151.0,
                342.0,
                anchor="nw",
                text=self.products[1].get_brand(),
                fill="#000000",
                font=("Inter SemiBold", 15 * -1)
            )
            self.canvas.create_text(
                405.0,
                303.0,
                anchor="nw",
                text=self.products[1].get_price(),
                fill="#000000",
                font=("Inter Bold", 30 * -1)
            )
            self.canvas.create_text(
                151.0,
                451.0,
                anchor="nw",
                text=self.products[1].get_store(),
                fill="#1EBA65",
                font=("Inter Medium", 20 * -1)
            )

        if len(self.products) >= 3:
            self.canvas.create_rectangle(
                572.0,
                275.0,
                933.0,
                516.0,
                fill="#E1FCEE",
                outline=""
            )
            self.canvas.create_text(
                598.0,
                290.0,
                anchor="nw",
                text="3",
                fill="#1EBA65",
                font=("Inter Black", 60 * -1)
            )
            self.canvas.create_text(
                663.0,
                310.0,
                anchor="nw",
                text=self.products[2].get_name().split(' ')[0],
                fill="#000000",
                font=("Inter Black", 20 * -1)
            )
            self.canvas.create_text(
                663.0,
                334.0,
                anchor="nw",
                text=self.products[2].get_brand(),
                fill="#000000",
                font=("Inter SemiBold", 13 * -1)
            )
            self.canvas.create_text(
                828.0,
                307.0,
                anchor="nw",
                text=self.products[2].get_price(),
                fill="#000000",
                font=("Inter Bold", 15 * -1)
            )
            self.canvas.create_text(
                598.0,
                451.0,
                anchor="nw",
                text=self.products[2].get_store(),
                fill="#1EBA65",
                font=("Inter Medium", 20 * -1)
            )

    def open_results_window(self):
        if len(self.products) < 3:
            WindowError("Not enough products")
            return

        self.window_table = Tk()
        self.window_table.geometry("1400x400")
        self.window_table.configure(bg="#FFFFFF")
        self.window_table.title("Results Table")
        table_frame = Frame(self.window_table)
        table_frame.pack(side="bottom", fill="both", expand=True)

        scrollbar = Scrollbar(table_frame, orient=VERTICAL)
        scrollbar.pack(side="right", fill="y")

        self.table = Treeview(table_frame, yscrollcommand=scrollbar.set, selectmode="browse")
        self.table.pack(side="bottom", fill="both", expand=True)

        scrollbar.config(command=self.table.yview)

        self.table["columns"] = ("name", "site", "brand", "description", "price", "link")
        self.table.column("#0", width=0, stretch="no")
        self.table.heading("name", text="Name")
        self.table.heading("site", text="Site")
        self.table.heading("brand", text="Brand")
        self.table.heading("description", text="Description")
        self.table.heading("price", text="Price")
        self.table.heading("link", text="Link")

        for product in self.products:
            self.table.insert("", "end", values=(product.get_name(), product.get_store(), product.get_brand(), product.get_description(), product.get_price(), product.get_url()))

        self.table.pack(side="left", fill="both", expand=True)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_FOLDER = "assets/frame0"
        ASSETS_PATH = OUTPUT_PATH / ASSETS_FOLDER
        return ASSETS_PATH / Path(path)


if __name__ == "__main__":
    product1 = Product(name="Iphone 14 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet là", price=998.99, url="http://example.com/product1", image_url="http://example.com/image1.jpg")
    product2 = Product(name="Iphone 15 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet lorem ipsum dolor si amet texte long long texte long longtexte long long", price=1020.99, url="http://example.com/product2", image_url="http://example.com/image2.jpg")
    # product3 = Product(name="Iphone 16 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 16 pro lorem ipsum dolor sit amet ", price=1099.99, url="http://example.com/product3", image_url="http://example.com/image3.jpg")
    # product4 = Product(name="Iphone 14 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet ", price=1055.99, url="http://example.com/product4", image_url="http://example.com/image4.jpg")
    # products = [product1, product2]
    products = []
    interface = ResultsInterface(products)
