from tkinter import Frame
from src.components.bton import Bton
from src.components.btons_properties import bton_search_file_p, bton_delete_path_p, bton_save_file_p
from tkinter import Label
from tkinter import Entry
from tkinter import filedialog
from tkinter import END
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo
import os
from datetime import datetime
from shutil import move
from controllers.file_controller import insert_file

class Save_pdf():

    def __init__(self, root):

        def select_file(entry):

            file_path = filedialog.askopenfilename(title = "Seleccione Archivo", filetypes=[("PDF", "*.pdf")])
            entry.insert(0, file_path)

        def save_file(entry):

            if entry.get() != "":

                if askyesno("Guardar Archivo", entry.get().split("/").pop()):
                    showinfo("Si", "Archivo Guardado") 

                    new_pdf = [
                        "id",
                        entry.get().split("/").pop(),
                        f"{os.path.abspath(os.getcwd())}"+"\\files\\" +  entry.get().split("/").pop(),
                        float(os.path.getsize(entry.get())/1000), 
                        datetime.fromtimestamp(os.path.getctime(entry.get())).strftime('%Y-%m-%d %H:%M:%S')
                    ]
        
                    insert_file(
                        new_pdf[1],
                        new_pdf[2], 
                        new_pdf[3], 
                        new_pdf[4]
                    )
                    move(entry.get(), "./files")
                    entry.delete(0, END)

        def delete_path(entry):
            entry.delete(0, END)

        self.save_pdf = Frame(root)
        self.save_pdf.config(width=600, height=300, bg="#F0E0B0")

        self.label = Label(self.save_pdf, text = "Ruta del archivo :", bg="#F0E0B0")
        self.label.place(x=115, y=3)

        self.entry_file = Entry(self.save_pdf, width = 65)
        self.entry_file.place(x=118, y=23)

        self.bton_search_file = Bton(self.save_pdf, bton_search_file_p, lambda: select_file(self.entry_file))
        
        self.bton_delete_path = Bton(self.save_pdf, bton_delete_path_p, lambda : delete_path(self.entry_file))

        self.bton_save_file = Bton(self.save_pdf, bton_save_file_p, lambda : save_file(self.entry_file))
        
        self.save_pdf.pack()

    def get_save_pdf(self):

        return self.save_pdf