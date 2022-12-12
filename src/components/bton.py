from tkinter import Button

class Bton():
    
    def __init__(self, root, bton_propertys, function):
        self.bton = Button(
        root, 
        text = bton_propertys["text"],
        bg = bton_propertys["bg"], 
        fg = bton_propertys["fg"], 
        activebackground = bton_propertys["active_bg"], 
        activeforeground = bton_propertys["active_fg"],
        cursor= bton_propertys["cursor"],
        command = function
        )

        self.bton.place(x = bton_propertys["place_x"], y = bton_propertys["place_y"])