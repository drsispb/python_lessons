'''Задача 6. Крестики-нолики
Что нужно сделать
Создайте программу, которая реализует игру «Крестики-нолики».

Для этого напишите:

1. Класс, который будет описывать поле игры.
class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки.
    #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    #  Помимо этого, класс должен содержать методы:
    #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние.
    Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
    #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
    True — если один из игроков победил, False — если победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
    #  Клетка, у которой есть значения:
    #  занята она или нет;
    #  номер клетки;
    #  символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
    #  У игрока может быть:
    #  имя,
    #  количество побед.
    #  Класс должен содержать метод:
    #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
    Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:
    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
    проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков
    или ничьей. Если игра завершена, метод возвращает True, иначе False.
    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать
    играть. После каждой игры выводится текущий счёт игроков.'''


class Board:

    def __init__(self, board):
        self.board = board

    def change_cell_state(self, num_cell, symbol):
        if self.board[num_cell] == None:
            self.board[num_cell] = symbol
            return True
        else:
            return False

    def check_status_game(self):
        if self.board[1] == '+' and  self.board[2] == '+' and self.board[2] == '+':
            return True
        elif self.board[2]== '0' and self.board[1] == '0' and self.board[3] == '0':
            return True
        elif self.board[4] == '+' and self.board[5] == '+' and self.board[6] == '+':
            return True
        elif self.board[4] == '0' and self.board[5] == '0' and self.board[6] == '0':
            return True
        elif self.board[7] == '+' and self.board[8]== '+' and  self.board[9] == '+':
            return True
        elif self.board[7] == '0' and self.board[8] == '0' and self.board[9] == '0':
            return True
        elif self.board[1] == '+' and self.board[4] == '+' and self.board[7] == '+':
            return True
        elif self.board[1] == '0' and self.board[4] == '0' and self.board[7] == '0':
            return True
        elif self.board[2] == '+' and self.board[5] == '+' and self.board[8] == '+':
            return True
        elif self.board[2] == '0' and self.board[5] == '0' and self.board[8] == '0':
            return True
        elif self.board[3] == '+' and self.board[6] == '+' and self.board[9] == '+':
            return True
        elif self.board[3] == '+' and  self.board[6] == '+' and  self.board[9] == '0':
            return True
        elif self.board[1] == '+' and self.board[5] == '+' and self.board[9] == '+':
            return True
        elif self.board[1] == '+' and  self.board[5] == '+' and  self.board[9] == '0':
            return True
        elif self.board[3] == '+' and self.board[5] == '+' and self.board[7] == '+':
            return True
        elif self.board[3] == '+' and  self.board[5] == '+' and  self.board[7] == '0':
            return True
        else:
            return False

class Cell:

    def __init__(self, busy=None):
        self.busy = busy
        self.number_cell = 1, 2, 3, 4, 5, 6, 7, 8, 9
        self.symbol = '+', '0', None

class Player:

    def __init__(self, name, win, sym):
        self.name = name
        self.win = win
        self.sym = sym

    # @staticmethod
    def do_move(self):
        x = True
        while x == True:
            try:
                num_cell = int(input('Введите номер клетки (от 1 до 9): '))
                if type(num_cell) == int and len(str(num_cell)) == 1 and num_cell != 0:
                    x = False
                    return num_cell
                else:
                    print('Введен номер выходящий за границы поля')
            except:
                print('Неверный формат ввода')



class Game:
    status = True
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board

    '''Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
    проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.'''

    def start_one_step(self, player):
        x = player.do_move()
        if x:
            if self.board.change_cell_state(x, player.sym):
                if self.board.check_status_game():
                    return True
                else:
                    return False
        else:
            print('start_one_step not work')

    '''Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков
    или ничьей. Если игра завершена, метод возвращает True, иначе False.'''

    def start_one_game(self):

        for i in range(9):
            if i % 2 == 0:
                if self.start_one_step(player_1):
                    player_1.win += 1
                    break
            elif i % 2 == 1:
                if self.start_one_step(player_2):
                    player_2.win += 1
                    break

        return True


    '''Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать
    играть. После каждой игры выводится текущий счёт игроков.'''

    def start_game(self):
        ask = 'да'
        while ask == 'да':
            print('Текущий счет: {} {} - {} {}'.format(
                player_1.name,
                player_1.win,
                player_2.name,
                player_2.win
            ))
            print('Желаете ли начать игру ? ')
            ask = input('да или нет ').lower()
            if ask == 'да':
                self.start_one_game()
            elif ask != 'да' and ask != 'нет':
                print('Некорректный ответ')
                ask = input('Повторите, да или нет: ').lower()
                if ask != 'да' or ask != 'нет':
                    print('Какой же ты тупой, лучше не продолжай играть дальше')
            elif ask == 'нет':
                ask = 'нет'
        return False





while True:
    player_1 = Player(input('Введите имя '), 0, '+')
    player_2 = Player(input('Введите имя '), 0, '0')
    cell = Cell()
    board = Board({i: cell.busy for i in range(1, 10)})

    crBoard = Game(player_1, player_2, board)
    if crBoard.start_game():
        break
            # if crBoard.start_one_game() != True:
            #     for i in range(9):
            #         if i % 2 == 0:
            #             crBoard.start_one_step(player_1.sym)
            #             if self.start_one_step == True:
            #                 break
            #         elif i % 2 == 1:
            #             crBoard.start_one_step(player_2.sym)
            #             if self.start_one_step == True:
            #                 break





