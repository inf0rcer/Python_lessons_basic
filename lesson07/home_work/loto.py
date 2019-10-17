#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
from random import randint


class Card:
	def __init__(self, name):
		barrel_bag = [x for x in range(1, 91)]
		self.card = [
		    __class__.gen_string(barrel_bag),
		    __class__.gen_string(barrel_bag),
		    __class__.gen_string(barrel_bag)
		]
		self.name = name
		self.count_barrel = 15

	@staticmethod
	def gen_string(barrel_bag):
		string = ['' for _ in range(9)]
		for x in range(8, 3, -1):
			digit = randint(0, x)
			while string[digit] != '':
				digit += 1
			string[digit] = barrel_bag.pop(randint(0, len(barrel_bag) - 1))
		return string

	def __str__(self):
		rez = '{:-^26}\n'.format(self.name)
		for x in range(3):
			rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
		return rez + '--------------------------'


user = Card(' Пользователь ')
computer = Card(' Компьютер ')

barrel_bag = [x for x in range(1, 91)]
while True:
	if len(barrel_bag) < 1:
		print('Сумка с боченками пуста.\n'
		      'у пользователя осталось {} чисел,\n'
		      'у компьютера осталось {} чисел.'.format(
		          user.count_barrel, computer.count_barrel))
		break
	barrel = barrel_bag.pop(randint(0, len(barrel_bag) - 1))
	print('\nНовый боченок: {} (осталось {})'.format(barrel, len(barrel_bag)))
	print(computer)
	print(user)
	action = input('Зачеркнуть цифру? (y/n)')
	action = action.lower()
	while len(action) == 0 or action not in 'yn':
		print('\n\nНезивестный ввод\n')
		print('Новый боченок: {} (осталось {})'.format(barrel, len(bag)))
		print(computer)
		print(user)
		action = input('Зачеркнуть цифру? (y/n)')
		action = action.lower()


	if action == 'y':
		test = False
		for x in range(3):
			if barrel in user.card[x]:
				test = True
				user.card[x][user.card[x].index(barrel)] = '-'
				user.count_barrel -= 1
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			if user.count_barrel < 1:
				print('Пользователь победил!')
				break
			elif computer.count_barrel < 1:
				print('Компьютер победил!')
				break
		else:
			print('Пользователь проиграл! Такого числа нет на карточке')
			break
	elif action == 'n':
		test = False
		for x in range(3):
			if barrel in user.card[x]:
				print('Пользователь проиграл! Такое число есть на карточке')
				test = True
				break
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			break
		if user.count_barrel < 1:
			print('Пользователь выиграл!')
			break
		elif computer.count_barrel < 1:
			print('Компьютер выиграл!')
			break
