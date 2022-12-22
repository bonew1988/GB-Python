import model


def view_all_employee():
    with open(model.file_name, 'r+') as file:
        return file.readlines()
