import random


class LotoCard:
    def __init__(self, player_name):
        self.name = player_name
        numbers = [i + 1 for i in range(90)]
        random.shuffle(numbers)
        self.card = [sorted([numbers.pop() for i in range(5)]) for j in range(3)]
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                self.card[i][j] = str(self.card[i][j])
        for i in range(len(self.card)):
            whitespace = [t for t in range(5)]
            random.shuffle(whitespace)
            for j in range(9-len(self.card[i])):
                self.card[i].insert(whitespace[j], '_')
        self.score = 15

    def delete(self, number):
        in_card = False
        for j in range(len(self.card)):
            if number in self.card[j]:
                self.card[j][self.card[j].index(number)] = '/'
                in_card = True
                self.score -= 1
                if self.score == 0:
                    print(self.name, ' вычеркнул все числа! Победа!')
                    exit()
        return in_card

    def check(self, number):
        in_card = False
        for j in range(3):
            if number in self.card[j]:
                in_card = True
        return in_card

    def print_card(self):
        print('Игрок:', self.name, '\n', '------------------')
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                print(self.card[i][j].rjust(2, ' '), end=' ')
            print('\n')
        print('------------------')



class LotoGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def start(self):
        bag = [str(i + 1) for i in range(90)]
        random.shuffle(bag)
        for current_num in bag:
            self.player_1.print_card()
            self.player_2.print_card()
            print('Новый боченок: ', current_num)
            decide = input('Удаляем? y/n ')
            while True:
                if decide == 'y':
                    if not self.player_1.delete(current_num):
                        print('Game over! ', self.player_1.name, ' lose.')
                        exit()
                    break
                elif decide == 'n':
                    if self.player_1.check(current_num):
                        print('Game over! ', self.player_1.name, ' lose.')
                        exit()
                    break
                elif decide != 'y' and decide != 'n':
                    print('Введен некорректный ответ, попробуйте еще раз.', '\n')
                    decide = input('Удаляем? y/n ')
            self.player_2.delete(current_num)


first_card = LotoCard('Дмитрий')
second_card = LotoCard('Компьютер')
game = LotoGame(first_card, second_card)
game.start()
