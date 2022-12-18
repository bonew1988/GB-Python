def contact_to_s():
    return input('Введите информацию для поиска: ')

def choose_mode():
    return input('Выберите режим работы (1 - добавление, 2 - поиск): ')

def new_contact():
    name = input('Введите имя: ')
    phone_num = input('Введите норме телефона: ')
    return f'{name} || {phone_num}'

def show_found(result):
    print('Результат поиска: ')
    for i in result:
        print(i)
