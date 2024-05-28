from tkinter import Tk, Canvas, Frame, VERTICAL
from tkinter.ttk import Scrollbar
from PIL import Image, ImageTk

import sys
# sys.path.append("..")
# from analyses.product import Product

class MultipleProductsInterface:
    def __init__(self, products, num_articles=3):
        self.products = products[:num_articles]

        self.window = Tk()
        self.window.geometry("973x605")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Vos résultats !")

        self.canvas = Canvas(self.window)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.frame = Frame(self.canvas, bg="#FFFFFF")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.display_products()

        # Calculate total sum
        total_sum = sum(product.get_price() for product in self.products)

        # Display total sum
        self.canvas.create_text(
            431.0,
            20,
            anchor="nw",
            text=f"Total: {total_sum}€",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def display_products(self):
        y_offset = 50
        for i, product in enumerate(self.products, start=1):
            # Change rectangle background color to green
            self.canvas.create_rectangle(
                0.0,
                y_offset - 20,
                973.0,
                y_offset + 193,
                fill="#B0E0C6",
                outline=""
            )

            self.canvas.create_text(
                431.0,
                y_offset,
                anchor="nw",
                text=f"Product {i}",
                fill="#000000",
                font=("Inter Bold", 16 * -1)
            )

            self.canvas.create_text(
                151.0,
                y_offset + 50,
                anchor="nw",
                text=product.get_name().split(' ')[0],
                fill="#000000",
                font=("Inter Black", 30 * -1)
            )

            self.canvas.create_text(
                151.0,
                y_offset + 90,
                anchor="nw",
                text=product.get_brand(),
                fill="#000000",
                font=("Inter SemiBold", 15 * -1)
            )

            self.canvas.create_text(
                775.0,
                y_offset + 40,
                anchor="nw",
                text=product.get_price(),
                fill="#000000",
                font=("Inter Bold", 30 * -1)
            )

            self.canvas.create_text(
                766.0,
                y_offset + 80,
                anchor="nw",
                text=product.get_store(),
                fill="#FFFFFF",
                font=("Inter Medium", 20 * -1)
            )

            self.canvas.create_text(
                151.0,
                y_offset + 160,
                anchor="nw",
                text=product.get_description()[:130],
                fill="#000000",
                font=("Inter SemiBold", 15 * -1)
            )

            y_offset += 240

if __name__ == "__main__":
    product1 = Product(name="Iphone 14 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet là", price=998.99, url="http://example.com/product1", image_url="http://example.com/image1.jpg")
    product2 = Product(name="Iphone 15 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet lorem ipsum dolor si amet texte long long texte long longtexte long long", price=1020.99, url="http://example.com/product2", image_url="http://example.com/image2.jpg")
    product3 = Product(name="Iphone 16 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 16 pro lorem ipsum dolor sit amet ", price=1099.99, url="http://example.com/product3", image_url="http://example.com/image3.jpg")
    product4 = Product(name="Iphone 14 Pro", store="Cyber", brand="Apple", description="Description de l’iphone 14 pro lorem ipsum dolor sit amet ", price=1055.99, url="http://example.com/product4", image_url="http://example.com/image4.jpg")
    products = [product1, product2, product3, product4]

    interface = MultipleProductsInterface(products, num_articles=4)
