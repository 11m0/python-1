import random


def my_sort(line):
    temp_line = []
    for i in range(len(line)):
        if line[i] != ' ':
            temp_line.append(line[i])
            line[i] = '&'
    temp_line.sort(reverse=True)
    for i in range(len(line)):
        if line[i] == '&':
            line[i] = temp_line.pop()
    return line


class LottoCard:
    def __init__(self, name_card):
        common_line = random.sample(range(1, 91), 15)
        self.name_card = name_card
        self.line_1 = common_line[:5] + [' ' for _ in range(1, 5)]
        self.line_2 = common_line[5:10] + [' ' for _ in range(1, 5)]
        self.line_3 = common_line[10:15] + [' ' for _ in range(1, 5)]
        random.shuffle(self.line_1)
        random.shuffle(self.line_2)
        random.shuffle(self.line_3)
        self.result = [my_sort(self.line_1), my_sort(self.line_2), my_sort(self.line_3)]

    def __str__(self):
        return '{}{}{}'.format('\t'.join(map(str, my_sort(self.line_1))) + '\n',
                               '\t'.join(map(str, my_sort(self.line_2))) + '\n',
                               '\t'.join(map(str, my_sort(self.line_3))) + '\n')


class LottoGame:
    def __init__(self, card_1, card_2):
        self.card_1 = card_1
        self.card_2 = card_2
        self.rand_line = random.sample(range(1, 91), len(range(1, 91)))

    def start(self):
        while True:
            print('---------Карточка игрока----------')
            for i in range(len(self.card_1)):
                print('{}'.format('\t'.join(map(str, self.card_1[i]))))
            print('-------Карточка компьютера--------')
            for i in range(len(self.card_2)):
                print('{}'.format('\t'.join(map(str, self.card_2[i]))))

            rand_number = self.rand_line.pop()
            print(f'Выпал бочонок: {rand_number}, в мешке осталось {len(self.rand_line)}')
            answer = input('Хотите зачеркнуть ? (y/n): ')

            self.card_2 = [['-' if el == rand_number else el for el in self.card_2[i]]
                           for i in range(len(self.card_2))]
            if not any(isinstance(i, int) for i in [i for line in self.card_1 for i in line]):
                print('Игра окончена, игрок победил!')
                break
            elif not any(isinstance(i, int) for i in [i for line in self.card_2 for i in line]):
                print('Игра окончена, компьютер победил!')
                break
            elif answer == 'y' and any(rand_number in i for i in (self.card_1[j] for j in range(len(self.card_1)))):
                self.card_1 = [['-' if el == rand_number else el for el in self.card_1[i]]
                               for i in range(len(self.card_1))]
            elif answer == 'n' and not any(rand_number in i for i in (self.card_1[j] for j in range(len(self.card_1)))):
                continue
            else:
                print('Игрок ввел неверный вариант и проиграл')
                break


human_player = LottoCard('Player')
computer_player = LottoCard('Computer')

game = LottoGame(human_player.result, computer_player.result)
game.start()
