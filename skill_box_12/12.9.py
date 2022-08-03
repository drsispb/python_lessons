import random
'''
Вы пришли на работу в контору по разработке игр, целевая аудитория — дети и их родители. У прошлого
программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не успел сделать эту задачу и оставил только
небольшой шаблон проекта. Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или
проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
'''

def rock_paper_scissors():
    answer = input('Введите ваш ход (камень, ножницы, бумага): ')
    game = ['камень', 'ножницы', 'бумага']
    game = random.choice(game)
    if game == answer:
        print('Ничья')
    elif game == 'камень' and answer == 'ножницы':
        print('Вы проиграли')
    elif game == 'камень' and answer == 'бумага':
        print('Вы выиграли')
    elif game == 'ножницы' and answer == 'бумага':
        print('Вы выиграли')
    elif game == 'ножницы' and answer == 'камень':
        print('Вы проиграли')
    elif game == 'бумага' and answer == 'ножницы':
        print('Вы выиграли')
    elif game == 'бумага' and answer == 'камень':
        print('Вы проиграли')
    else:
        print('Неверный ввод')

def guess_the_number():
    number = int(input('Загадай число: '))
    N = 50
    low_limit = 0
    high_limit = 100
    answer = 0
    answer_count = 1
    while True:
        print('n = ', int(N))
        answer = int(input('Твое число равно, больше или меньше, чем число n? '))
        if answer == 2:
            low_limit = N
            N *= 1.5
            if high_limit < N:
                N = (low_limit + high_limit) // 2
        elif answer == 3:
            high_limit = N
            N *= 0.5
            if low_limit > N:
                N = (low_limit + high_limit) // 2
        else:
            print('Ты угадал')
            break
        answer_count += 1
    print('Попыток ', answer_count)

def mainMenu():
    while True:
        choice = int(input('В какую игры вы хоите сыграть ? 1 - К Н Б, 2 - Угадай число: '))
        if choice == 1:
            rock_paper_scissors()
        elif choice == 2:
            guess_the_number()
        else:
            print('Неверный ввод')
    # Здесь главное меню игры


mainMenu()

