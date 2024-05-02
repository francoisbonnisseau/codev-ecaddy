from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Checkbutton, Scrollbar, Frame
from pathlib import Path

# Fonction utilitaire pour les chemins relatifs aux assets
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_FOLDER = "assets/frame0"
    ASSETS_PATH = OUTPUT_PATH / ASSETS_FOLDER
    return ASSETS_PATH / Path(path)

# Variable globale pour suivre la position verticale actuelle des blocs
current_y_position = 0

# Variable pour stocker la référence du bouton "add_item" du bloc précédent
previous_add_button = None

# Variable pour compter le nombre de blocs - permet de cibler les blocs à supprimer
block_count = 0

# Définir les variables d'image globales
button_image_1 = None
entry_image_1 = None
entry_image_2 = None
button_image_2 = None

# Fonction pour ajouter un bloc
def add_block():
    global current_y_position, button_image_1, entry_image_1, entry_image_2, button_image_2, previous_add_button, block_count
    
    #importer les images
    if button_image_1 is None:
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    if entry_image_1 is None:
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    if entry_image_2 is None:
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    if button_image_2 is None:
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    
    
    # Créer un frame pour contenir le bloc
    block_frame = Frame(blocks_frame, bg="#FFFFFF")
    block_frame.pack(fill="x", padx=10, pady=5)

    # Créer les éléments du bloc
    canvas.create_rectangle(
        81.0,
        current_y_position + 217.9999999999999,
        556.0,
        current_y_position + 219.0,
        fill="#1EBA65",
        outline=""
    )

    add_item_button = Button(
        block_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=add_block,
        relief="flat"
    )
    add_item_button.grid(row=0, column=0)
    previous_add_button = add_item_button
    
    product_input = Entry(
        block_frame,
        bd=0,
        bg="#D3D3D3",
        fg="#000716",
        highlightthickness=0
    )
    product_input.grid(row=1, column=0)
    
    brand_input = Entry(
        block_frame,
        bd=0,
        bg="#D3D3D3",
        fg="#000716",
        highlightthickness=0
    )
    brand_input.grid(row=1, column=1)

    current_y_position += 100
    block_count += 1

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

# Créer un frame pour contenir les blocs
blocks_frame = Frame(canvas, bg="#FFFFFF")
blocks_frame.place(x=0, y=0, relwidth=1, relheight=1)

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
