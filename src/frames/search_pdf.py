from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import Canvas
from src.components.bton import Bton
from src.components.btons_properties import bton_searh_pdf_p
from tkinter import Scrollbar
from src.components.file_pdf import File_pdf
from controllers.file_controller import get_by_title_creation, get_all_files

class Search_pdf():

    def __init__(self, frame):       
        
        def click_bton():
            
            for widget in self.scrollable_frame_s.winfo_children():
                widget.destroy()

            file = get_by_title_creation(self.entry_title.get(), self.entry_creation.get())

            row = 0
            column= 0

            for i in range(len(file)):

                File_pdf( self.scrollable_frame_s, file[i], row , column)
                column += 1

                if column == 3:
                    
                    row += 1
                    column = 0

        files = get_all_files()

        self.search_pdf = Frame(frame, bg= "#F0E0B0", pady=150)    
        self.title = Label(frame, text="Ingresar título :", bg="#F0E0B0")
        self.title.pack()
        self.entry_title = Entry(frame, width=35)
        self.entry_title.pack()
        self.creation = Label(frame, text="Ingresar fecha de creación :", bg="#F0E0B0")
        self.creation.pack()
        self.entry_creation = Entry(frame, width=35)
        self.entry_creation.pack()
        
        self.bton_searh_pdf = Bton(frame, bton_searh_pdf_p, click_bton )

        self.canvas_s = Canvas(self.search_pdf, width=630, height=350, bg= "#EFEEE9")
        self.scrollbar_s= Scrollbar(self.search_pdf, orient="vertical", command=self.canvas_s.yview)
        self.scrollable_frame_s = Frame(self.canvas_s, bg="#EFEEE9")

        self.scrollable_frame_s.bind(
            "<Configure>",
            lambda e: self.canvas_s.configure(
            scrollregion= self.canvas_s.bbox("all"))
        )

        self.canvas_s.create_window((150, 0), window= self.scrollable_frame_s, anchor="nw")

        self.canvas_s.configure(yscrollcommand= self.scrollbar_s.set)

        row = 0
        column= 0

        for i in range(len(files)):
            File_pdf(self.scrollable_frame_s, files[i], row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0

        self.search_pdf.pack()
        self.canvas_s.pack(side="left", fill="both", expand=True)
        self.scrollbar_s.pack(side="right", fill="y")

    def get_search_pdf(self):

        return self.search_pdf