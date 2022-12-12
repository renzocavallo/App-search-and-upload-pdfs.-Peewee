from tkinter import Menu
from src.frames.save_pdf import Save_pdf
from src.frames.search_pdf import Search_pdf

class Menu_app():

    def __init__(self, frame):
            
        def click_search_pdf():

            for widget in frame.winfo_children():
                widget.destroy()
            
            search_pdf = Search_pdf(frame)
            search_pdf.get_search_pdf()

        def click_search_disk():

            for widget in frame.winfo_children():
                widget.destroy()
                
            save_pdf = Save_pdf(frame)
            save_pdf.get_save_pdf()

        self.menu = Menu()

        self.item_0 = Menu(self.menu, tearoff=False)
         
        self.item_0.add_command(label="Guardar", command= click_search_disk)
        self.item_0.add_command(label="Buscar", command= click_search_pdf)
        self.item_0.add_separator()
        self.item_0.add_command(label="Salir", command= quit)

        self.item_1 = Menu(self.menu, tearoff=False)

        self.menu.add_cascade(menu=self.item_0, label="Archivos")

    def get_menu(self):

        return self.menu
