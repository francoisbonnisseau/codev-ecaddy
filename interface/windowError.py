import tkinter as tk
from tkinter import ttk

class WindowError:
    """Cette classe permet de créer une fenêtre d'erreur
    """
    def __init__(self, text):
        self.window = tk.Tk()
        self.window.title("Erreur")
        self.window.geometry("300x200")
        self.label = ttk.Label(self.window, text=text, wraplength=250, justify='center')
        self.label.pack(expand=True, padx=20, pady=20)
        self.button = ttk.Button(self.window, text="OK", command=self.window.destroy)
        self.button.pack(pady=10)
        self.window.mainloop()
        
        
if __name__ == "__main__":
    WindowError("Erreur")