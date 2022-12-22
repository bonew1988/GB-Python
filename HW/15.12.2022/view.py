def start():
    print("Список работников\n" +
          "-------------------------------\n" +
          "1 - показ работников\n" +
          "2 - добавление новых работников\n" +
          "3 - поиск работников\n" +
          "4 - удаление работников\n" +
          "5 - выход")
    choice = input("Введите номер: ")
    return choice

def print_message(data):
    print(data)

def insert_data(message):
    return input(message)
