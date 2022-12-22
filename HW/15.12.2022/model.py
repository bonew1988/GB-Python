import logger

file_name = "employee.csv"
file1 = open(file_name, "a+")
file1.close()


def search_employee_record(search_name):
    search_name = search_name.title()
    file_contents = logger.view_all_employee()

    found = False
    for line in file_contents:
        if search_name in line:
            print("Результат: :", end=" ")
            print(line)
            return line
    if not found:
        return 'Не найдено!'


def delete_employee(search_name):
    search_name = search_name.title()
    file_contents = logger.view_all_employee()

    found_delete = False
    for line in file_contents:
        if search_name in line:
            print("Результат: :", end=" ")
            print(line)
            found_delete = True
            file = open('employee.csv', "r")
            f = file.read().replace(line, '')
            file2 = open('employee.csv', 'w')
            file2.write(f)
            file2.close()
            print('Работник удалён!')
            break
    if not found_delete:
        return 'Не найдено!'


def enter_employee_record():
    id_employee = input('Введите id: ')
    first = input('Введите Имя: ')
    first = first.title()
    last = input('Введите Фамилию: ')
    last = last.title()
    job_title = input('Введите должность: ')
    phone = input('Введите телефонный номер: ')
    email = input('Введите E-mail: ')
    employee = ("[" + id_employee + ", " + first + " " + last + ", " + phone + ", " + email + ", " + job_title + "]\n")
    file1 = open(file_name, "a+")
    file1.write(employee)
    file1.close()

    print("Работник\n " + employee + "успешно добавлен!")
