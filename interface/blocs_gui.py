from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Checkbutton
from pathlib import Path

# Fonction utilitaire pour les chemins relatifs aux assets
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_FOLDER = "assets/frame0"
    ASSETS_PATH = OUTPUT_PATH / ASSETS_FOLDER
    return ASSETS_PATH / Path(path)


# Variable globale pour suivre la position verticale actuelle des blocs
current_y_position = 0

# Définir les variables d'image globales
button_image_1 = None
entry_image_1 = None
entry_image_2 = None
button_image_2 = None

# Fonction pour ajouter un bloc
def add_block():
    global current_y_position, button_image_1, entry_image_1, entry_image_2, button_image_2
    
    #importer les images
    if button_image_1 is None:
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    if entry_image_1 is None:
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    if entry_image_2 is None:
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    if button_image_2 is None:
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

    #supprimer le bouton add_item du bloc précédent si c'est au moins le deuxieme bloc
    if add_item_button:
        add_item_button.destroy()
    
    # Créer les éléments du bloc
    add_item_button = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=add_block,
        relief="flat"
    )
    add_item_button.place(
        x=309.0,
        y=current_y_position + 240.0,
        width=28.0,
        height=28.0
    )
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png")
    )
    entry_bg_1 = canvas.create_image(
        219.5,
        current_y_position + 186.0,
        image=entry_image_1
    )
    product_input = Entry(
        window,
        bd=0,
        bg="#D3D3D3",
        fg="#000716",
        highlightthickness=0
    )
    product_input.place(
        x=120.0,
        y=current_y_position + 172.0,
        width=199.0,
        height=26.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png")
    )
    entry_bg_2 = canvas.create_image(
        411.0,
        current_y_position + 186.0,
        image=entry_image_2
    )
    brand_input = Entry(
        window,
        bd=0,
        bg="#D3D3D3",
        fg="#000716",
        highlightthickness=0
    )
    brand_input.place(
        x=356.0,
        y=current_y_position + 172.0,
        width=110.0,
        height=26.0
    )

    canvas.create_text(
        114.0,
        current_y_position + 152.0,
        anchor="nw",
        text="Nom du produit *",
        fill="#000000",
        font=("Inter Medium", 14 * -1)
    )

    canvas.create_text(
        350.0,
        current_y_position + 152.0,
        anchor="nw",
        text="Marque",
        fill="#000000",
        font=("Inter Medium", 14 * -1)
    )
    
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png")
    )
    remove_item_button = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=remove_block,
        relief="flat"
    )
    remove_item_button.place(
        x=58.0,
        y=current_y_position + 172.0,
        width=28.0,
        height=28.0
    )

    
    current_y_position += 100

# Fonction pour supprimer un bloc
def remove_block(product_input, brand_input, quantity_input, remove_block_button):
    global current_y_position
    product_input.destroy()
    brand_input.destroy()
    quantity_input.destroy()
    remove_block_button.destroy()
    current_y_position -= 100

def compare():
    pass


# Créer la fenêtre principale
window = Tk()
window.geometry("973x605")
window.configure(bg="#FFFFFF")

# Créer un canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=605,
    width=973,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Ajouter le texte et les boutons
canvas.create_rectangle(
    0.0,
    0.0,
    973.0,
    73.0,
    fill="#1EBA65",
    outline=""
)

canvas.create_text(
    266.0,
    27.0,
    anchor="nw",
    text="Ecaddy - outil de shopping pour le matériel informatique",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    31.0,
    116.0,
    anchor="nw",
    text="CHOISIR DES PRODUITS",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    770.0,
    177.0,
    anchor="nw",
    text="Alternate",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    667.0,
    116.0,
    anchor="nw",
    text="CHOISIR DES MAGASINS",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    770.0,
    225.0,
    anchor="nw",
    text="Boulanger",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    770.0,
    273.0,
    anchor="nw",
    text="CyberTech",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    770.0,
    321.0,
    anchor="nw",
    text="GrosBill",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    770.0,
    369.0,
    anchor="nw",
    text="Materiel.net",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

checkbox_boulanger = Checkbutton(
    window,
    onvalue=True,
    offvalue=False,
    height=2,
    width=2,
    bg="#fff",
    activebackground="#fff",
    highlightthickness=0
)
checkbox_boulanger.place(x=715.0, y=220.0)

checkbox_cybertech = Checkbutton(
    window,
    onvalue=True,
    offvalue=False,
    height=2,
    width=2,
    bg="#fff",
    activebackground="#fff",
    highlightthickness=0
)
checkbox_cybertech.place(x=715.0, y=268.0)

checkbox_grosbill = Checkbutton(
    window,
    onvalue=True,
    offvalue=False,
    height=2,
    width=2,
    bg="#fff",
    activebackground="#fff",
    highlightthickness=0
)
checkbox_grosbill.place(x=715.0, y=316.0)

checkbox_materiel = Checkbutton(
    window,
    onvalue=True,
    offvalue=False,
    height=2,
    width=2,
    bg="#fff",
    activebackground="#fff",
    highlightthickness=0
)
checkbox_materiel.place(x=715.0, y=364.0)

checkbox_alternate = Checkbutton(
    window,
    onvalue=True,
    offvalue=False,
    height=2,
    width=2,
    bg="#fff",
    activebackground="#fff",
    highlightthickness=0
)
checkbox_alternate.place(x=715.0, y=172.0)

canvas.create_rectangle(
    641.0,
    66.0,
    647.0000000000001,
    650.0216064453125,
    fill="#1EBA65",
    outline=""
)

##créer le premier bloc
add_block()



canvas.create_rectangle(
    81.0,
    217.9999999999999,
    556.0,
    219.0,
    fill="#1EBA65",
    outline=""
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png")
)
comparer = Button(
    window,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=compare,
    relief="flat"
)
comparer.place(
    x=670.0,
    y=509.0,
    width=174.0,
    height=64.0
)

window.resizable(False, False)
window.mainloop()
