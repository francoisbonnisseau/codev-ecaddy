from tkinter import Tk, Frame, Canvas, Scrollbar

class ResultsInterface:
    def __init__(self, products):
        self.products = products

        self.window = Tk()
        self.window.geometry("973x605")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Product Results")

        # Main Frame
        self.main_frame = Frame(self.window, bg="#FFFFFF")
        self.main_frame.pack(fill="both", expand=True)

        # Header Frame
        self.header_frame = Frame(self.main_frame, bg="#B0E0C6", height=73)
        self.header_frame.pack(fill="x", side="top")
        self.header_frame.pack_propagate(False)

        # Header Canvas for Texts and Shapes
        self.header_canvas = Canvas(self.header_frame, bg="#B0E0C6", height=73, width=973, bd=0, highlightthickness=0, relief="ridge")
        self.header_canvas.pack(fill="both", expand=True)
        self.header_canvas.create_text(431.0, 27.0, anchor="nw", text="Vos résultats !", fill="#000000", font=("Inter Bold", 16 * -1))

        # Product Display Frame with Scrollbar
        self.product_display_frame = Frame(self.main_frame, bg="#FFFFFF")
        self.product_display_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.canvas = Canvas(self.product_display_frame, bg="#FFFFFF")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.product_display_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollable_frame = Frame(self.canvas, bg="#FFFFFF")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Creating individual frames for each product display area
        for i, product in enumerate(self.products):
            frame = Frame(self.scrollable_frame, bg=["#1EBA65", "#B0DFC6", "#E1FCEE"][i % 3], height=241)
            frame.pack(fill="x", padx=40, pady=(0, 20) if i < len(self.products) - 1 else 0)
            frame.pack_propagate(False)
            canvas = Canvas(frame, bg=["#1EBA65", "#B0DFC6", "#E1FCEE"][i % 3], bd=0, highlightthickness=0, relief="ridge")
            canvas.pack(fill="both", expand=True)
            canvas.create_text(111.0, 30.0, anchor="nw", text=f"{i+1}. {product['name']}", fill="#000000", font=("Inter Black", 30 * -1))
            canvas.create_text(111.0, 80.0, anchor="nw", text=product['description'], fill="#000000", font=("Inter SemiBold", 15 * -1))
            canvas.create_text(111.0, 110.0, anchor="nw", text=product['brand'], fill="#000000", font=("Inter SemiBold", 15 * -1))
            canvas.create_text(735.0, 30.0, anchor="nw", text=product['price'], fill="#000000", font=("Inter Bold", 30 * -1))
            canvas.create_text(111.0, 140.0, anchor="nw", text=product['site'], fill="#1EBA65", font=("Inter Medium", 20 * -1))

        self.window.resizable(False, False)
        self.window.mainloop()
if __name__ == "__main__":
    products = [
        {
            "name": "Product 1",
            "description": "Description 1",
            "brand": "Brand 1",
            "price": "$100",
            "site": "Site 1"
        },
        {
            "name": "Product 2",
            "description": "Description 2",
            "brand": "Brand 2",
            "price": "$200",
            "site": "Site 2"
        },
        {
            "name": "Product 3",
            "description": "Description 3",
            "brand": "Brand 3",
            "price": "$300",
            "site": "Site 3"
        }
    ]
    ResultsInterface(products)