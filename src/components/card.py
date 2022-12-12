from tkinter import Frame
from tkinter import Label
from src.components.bton import Bton
from src.components.btons_properties import bton_open_p, bton_delete_p, bton_edit_p

class Card():

    def __init__(self, root, i, j, file, function_open, function_delete, function_edit):

        self.card = Frame(root)
        self.card.config(width="200", height="135", bd=2, relief="ridge", bg="#E3E1EB")
        self.card.grid(row=i,  column=j, padx= 5, pady=5)
        self.marc = Label(self.card, text="PDF", bg="#FA534A", fg="white")
        self.marc.place(x=0, y=0)
        self.title = Label(self.card, text=file["name"], bg="#E3E1EB", fg="#FA534A")
        self.title.place(x=0, y=25)

        self.bton_open = Bton(self.card, bton_open_p, function_open)

        self.bton_delete = Bton(self.card, bton_delete_p, function_delete)

        self.bton_edit = Bton(self.card, bton_edit_p, function_edit)

        self.size = Label(self.card, text=file["size"]+" bytes", bg="#E3E1EB", fg="#FA534A")
        self.size.place(x=0, y=90)
        self.creation = Label(self.card, text=file["creation"], bg="#E3E1EB", fg="#FA534A")
        self.creation.place(x=0, y=108)

    def get_card(self):
        
        return self.card