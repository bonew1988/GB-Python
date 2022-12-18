import csv

def add_new(contact):
    try:
        with open('book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('book.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])
    except FileNotFoundError:
        with open('book.txt', 'w', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('book.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])

def get_base():
    with open('book.txt', 'r', encoding='utf-8') as book:
        return book.read()
