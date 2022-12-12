from tkinter import Frame
from src.frames.search_pdf import Search_pdf

class Conteiner():

    def __init__(self, root):

        self.conteiner = Frame(root)
        self.conteiner.config(width=800, height=800, bg="#F0E0B0")

        self.search_pdf = Search_pdf(self.conteiner)
        self.search_pdf.get_search_pdf()
        
        self.conteiner.pack()

    def get_conteiner(self):
        
        return self.conteiner