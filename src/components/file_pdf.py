from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import END
from tkinter.messagebox import showerror
from src.components.card import Card
from src.components.bton import Bton
from src.components.btons_properties import bton_save_edit_p, bton_quit_p, bton_comfirm_date_p
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo
import os
from os import system, rename
from shutil import move
from controllers.file_controller import delete_by_id, get_all_files, edit_file, get_file_by_id
from validators.title_creation import title_patron, creation_patron
from src.components.date_picker import Date_picker

class File_pdf():

    def __init__(self, root, file, i, j):   
        
        def click_bton(file_pdf):

            system(file_pdf["path"])
        
        def click_delete():

            if askyesno("Eliminar Archivo", file["name"]):
                showinfo("Si", "Archivo Eliminado") 

                for widget in root.winfo_children():
                    widget.destroy()
            
                move(file["path"], './remove')
                delete_by_id(file["id"])
                files = get_all_files()

                row = 0
                column= 0

                for i in range(len(files)):

                    File_pdf( root, files[i] , row , column)
                    column += 1

                    if column == 3:
                        row += 1
                        column = 0

        def click_edit():

            window = Tk()
            window.title("Editar PDF")
            window.geometry("600x400")
            window.config(bg="#E3E1EB")
            title_label = Label(window, text="Título :", bg="#E3E1EB", fg="#FA534A")
            title_label.pack()
            title_entry = Entry(window, width=30)
            title_entry.insert(0, file["name"])
            title_entry.pack()
            creation_label = Label(window, text="Fecha de creación :", bg="#E3E1EB", fg="#FA534A")
            creation_label.pack()
            creation_entry = Entry(window)
            creation_entry.insert(0, file["creation"])
            creation_entry.pack()

            def click_confirm_date(date, calendar):

                date.delete(0, END)
                date.insert(0, calendar.date_calendar())

            date_picker = Date_picker(window, 175, 100)

            Bton(window, bton_comfirm_date_p, lambda : click_confirm_date(creation_entry, date_picker))

            Bton(window, bton_save_edit_p, lambda : click_save_edit(title_entry, creation_entry, window))
  
            Bton(window, bton_quit_p, window.destroy) 

            window.mainloop()

        def click_save_edit(title, creation, window):   

            if title_patron(title.get()) != None and creation_patron(creation.get()) != None:  

                if askyesno("Confirmar Edición", 
                    "Desea confirmar la edición ? " + 
                    "\n" + title.get() + 
                    "\n" + creation.get()):

                    showinfo("Si", "Archivo Editado") 

                    rename('./files/'+file["name"], './files/'+ title.get())
                    new_path = f"{os.path.abspath(os.getcwd())}"+"\\files\\" +  title.get().split("/").pop()
                    edit_file(file["id"], title.get(), new_path, creation.get())

                    for widget in root.winfo_children():
                        widget.destroy()
                
                    file_edit = get_file_by_id(file["id"])
                    Card(root, i , j, file_edit[0], lambda: click_bton(file_edit[0]), click_delete, click_edit)
                    window.destroy()

            else:

                showerror("Error", "Datos INVALIDOS")

                window.destroy()

        self.card = Card(root, i, j, file, lambda: click_bton(file) , click_delete, click_edit)
        self.card.get_card()