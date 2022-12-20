import random
candys = 117

def input_candy():
    global candys
    while True:
        move = int(input('Введите конфеты: '))
        if move > 0 and move < 29 and move <= candys:
            candys -= move
            break
        else:
            print('Столько взять нельзя!')

def bot_take():
    global candys
    while True:
        move = random.randint(1, 28)
        if move > 0 and move < 29 and move <= candys:
            print(f'Бот взял {move} конфет')
            candys -= move
            break

print(f'На столе лежит {candys} конфет')
players = ['Пользователь', 'Компьютер']
move = random.choice(players)
print(f'Первым ходит - {move}')
while True:
    if move == 'Пользователь':
        input_candy()
        print(f'Осталось {candys}')
        move = 'Компьютер'
        if candys < 29:
            print(f'Победил {move}')
            break
    else:
        bot_take()
        print(f'Осталось {candys} конфет')
        move = 'Пользователь'
        if candys < 29:
            print(f'Победил {move}')
            break
