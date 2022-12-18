def search_contact(base, contact):
    base = base.split('\n')
    flag = True
    result = []
    for i in base:
        if contact in i:
            flag = False
            result.append(i)
    if flag:
        result.append(f'Контакт {contact} не найден')
    return result
