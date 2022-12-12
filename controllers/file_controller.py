from models.file_model import File_pdf

def insert_file(name, path, size, creation):
    file_pdf = File_pdf()
    file_pdf.name = name
    file_pdf.path = path
    file_pdf.size = size
    file_pdf.creation = creation
    file_pdf.save()

def get_all_files():

    files = []

    for i in File_pdf.select():

        file = {
            "id": i.id,
            "name": i.name,
            "path": i.path,
            "size": i.size,
            "creation": i.creation
        }

        files.append(file)

    return files

def get_by_title_creation(title, creation):

    #función con SQL utilizando LIKE

    """db_proyect = sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    query = f"SELECT * FROM files WHERE name LIKE '%{title}%' AND creation LIKE '%{creation}%';"
    cursor_db_proyect.execute(query)
    return cursor_db_proyect.fetchall()"""

    files = []

    if title == "" and creation == "":

        files = get_all_files()

        return files

    if title != "" and creation != "":

        for i in File_pdf.select().where(File_pdf.name % f'*{title}*' and File_pdf.creation % f'*{creation}*'):

            file = {
                "id": i.id,
                "name": i.name,
                "path": i.path,
                "size": i.size,
                "creation": i.creation
            }

            files.append(file)

        return files

    if title != "" and creation == "":

        for i in File_pdf.select().where(File_pdf.name % f'*{title}*'):

            file = {
                "id": i.id,
                "name": i.name,
                "path": i.path,
                "size": i.size,
                "creation": i.creation
            }

            files.append(file)

        return files

    if title == "" and creation != "":

        for i in File_pdf.select().where(File_pdf.creation % f'*{creation}*'):

            file = {
                "id": i.id,
                "name": i.name,
                "path": i.path,
                "size": i.size,
                "creation": i.creation
            }

            files.append(file)

        return files

def get_file_by_id(id):

    files = []

    for i in File_pdf.select().where(File_pdf.id == id):

        file = {
            "id": i.id,
            "name": i.name,
            "path": i.path,
            "size": i.size,
            "creation": i.creation
        }

        files.append(file)

    return files

def delete_by_id(id):
    
    delete = File_pdf.get(File_pdf.id == id)
    delete.delete_instance()

def edit_file(id,new_title, new_path, new_creation):

    File_pdf.update(
            name = new_title, 
            path = new_path, 
            creation = new_creation
            ).where(
                File_pdf.id == id
                ).execute()