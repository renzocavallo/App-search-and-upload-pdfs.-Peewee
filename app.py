import os
import errno
from tkinter import Tk
from src.menu.menu import Menu_app
from src.frames.conteiner import Conteiner

def create_files():
    try:
       os.mkdir('files')
    except OSError as e:
        if e.errno != errno.EEXIST:
           raise

def create_remove():
   try:
      os.mkdir('remove')
   except OSError as e:
      if e.errno != errno.EEXIST:
         raise

app = Tk()
app.title("UPLOAD PDF")
app.geometry("800x800")

create_remove()
create_files()

conteiner = Conteiner(app)
conteiner.get_conteiner()

menu = Menu_app(conteiner.get_conteiner())

app.config(menu=menu.get_menu(), bg="#F0E0B0")

app.mainloop()