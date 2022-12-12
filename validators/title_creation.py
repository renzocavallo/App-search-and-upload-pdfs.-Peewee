import re

def title_patron(title):
    
    patron = re.compile("^[A-Za-z-_.0-9]*$")

    return patron.match(title)

def creation_patron(creation): 
    
    patron = re.compile("^[ /-:0-9]*$")

    return patron.match(creation)