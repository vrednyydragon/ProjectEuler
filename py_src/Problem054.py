import logging
from collections import Counter

# logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.basicConfig(level=logging.INFO) # DEBUG INFO WARNING ERROR CRITICAL

all_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
all_suits = ['D', 'H', 'S', 'C']
all_combinations_arr = ["High Card", "One Pair", "Two Pairs", "Three of a Kind",
		"Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
class Problem054():
	
	def All_Combinations(self, cards, suits):
		logger = logging.getLogger("Combinations")
		# logger.debug()
		royal_flush = all_cards[8:]
		flag = True
		count = 0
		index_arr = [] # список индексов соответствующих номеров карт из all_values 
		sorted_index_arr = [] # отсортированый массив по возрастанию
		card_combination = ''
		if len(cards) == 5 and len(suits) == 1: 
			# check is royal_flush
			for key in cards:
				if key in all_cards[8:]: 
					count += 1
			if count == 5:
				card_combination = 'Royal Flush'
			else:
				# в этом условии проверяю раскладку карт на наявность stright flush
				# сортирую индексы по возрастанию и проверяю последовательность с шагом 1
				# и если разница между индексами в сумме даст 4 то это stright flush
				count = 0
				for key in cards:
					index_arr.append(all_cards.index(key))
				# print(sorted(index_arr))
				sorted_index_arr = sorted(index_arr)
				for i in range(4, 0, -1):
					if sorted_index_arr[i] - sorted_index_arr[i-1] == 1:
						count += 1
				if count == 4:
					card_combination = 'Stright Flush'
				else:
					card_combination = 'Flush'
		if len(suits) > 1: 			
			if len(cards) == 2: 
				for key in cards:
					if cards[key] == 4:
						card_combination = 'Four of a Kind'
					elif cards[key] == 3:
						card_combination = 'Full House'
			if len(cards) == 5:
				count = 0
				index_arr = []
				sorted_index_arr = []
				for key in cards:
					index_arr.append(all_cards.index(key))
				# print(sorted(index_arr))
				sorted_index_arr = sorted(index_arr)
				for i in range(4, 0, -1):
					if sorted_index_arr[i] - sorted_index_arr[i-1] == 1:
						count += 1
				if count == 4:
					card_combination = 'Stright'
			if len(cards) == 3:
				for key in cards:
					if cards[key] == 3:
						card_combination = 'Three of a Kind'
					elif cards[key] == 2:
						card_combination = 'Two Pairs'
						break
			if len(cards) == 4:
				card_combination = 'One Pair'
			if len(cards) == 5:
				card_combination = 'High Card'
		# print(card_combination)
		return card_combination
	
	# в этой функции я отделяю значения карты от масти
	def PlayersCombination(self, card):
		card_value = card[0]
		card_suit = card[1]
		return card_value, card_suit
	
	# в этой функции узнаем сколько похожих значений карт есть у игрока
	def Counter_arr(self, arr):
		c = Counter(arr)
		return c # возвращает словарь такого типа {'A': 3, '6': 1, 'K': 1}

	# функция определения уровня ранга комбинации 
	def RankOfCombination(self, combination):
		index = 0
		for comb in all_combinations_arr:
			index = all_combinations_arr.index(combination)		
		return index

	# функция определения большей карты в раскладке 
	def HighestСard1(self, cards):
		min_ = 0
		max_ = 0
		high_card = ''
		for c in cards:
			min_ = all_cards.index(c)
			if min_ > max_:
				max_ = min_
		high_card = all_cards[max_]
		return high_card, max_

	def PlayersCards(self, player):
		logger = logging.getLogger("PlayersCards")
		# logger.debug(random_hands)
		card = [] #номер карты игрока
		suit = [] # масть карты игрока
		count_card = {} #считаем количество одинаковых номеров карты игрока
		count_suit = {} #считаем количество одинаковых мастей карты игрока
		card_combination = ''
		for cards in player:
			a,b = self.PlayersCombination(cards)
			card.append(a)
			suit.append(b)
		# logger.info('у игрока значение карт : {}, масти : {}'.format(card, suit))
		count_card = self.Counter_arr(card)
		count_suit = self.Counter_arr(suit)
		# logger.info('Игрок:')
		# logger.info('сумма одинаковых последовательностей карт {}.'.format(count_card))
		# logger.info('Сумма одинаковых мастей {}'.format(count_suit))
		card_combination = self.All_Combinations(count_card, count_suit)
		# logger.info('Комбинация карт {}'.format(card_combination))
		return count_card, count_suit, card_combination

	def PokerHands(self, file):
		logger = logging.getLogger("PokerHands")
		logger.info('start')
		count = 0
		count2 = 0
		player1 = []
		player2 = []
		cards1 = []
		suits1 = []
		combination1 = '' # имя комбинации
		index1 = 0 # порядковый номер комбинации из списка all_combinations_arr
		highest_card1 = ''
		ind_hight_card1 = 0 # порядковый номер карты из списка all_cards
		cards2 = []
		suits2 = []
		combination2 = ''
		index2 = 0
		highest_card2 = ''
		ind_hight_card1 = 0
		file_txt = open(file, 'r')
		random_hands = []
		poker_txt = file_txt.read().split("\n") 
		new1 = []
		new2 = []
		for i in poker_txt:
			logger.info("-"*50)
			random_hands = i.split(" ")
			player1 = random_hands[:5]
			player2 = random_hands[5:]
			cards1, suits1, combination1 = self.PlayersCards(player1)
			index1 = self.RankOfCombination(combination1)
			logger.info('Player 1:')
			logger.info('{}, cards : {}.'.format(combination1, player1))
			# logger.debug('index1 = {}'.format(index1))
			cards2, suits2, combination2 = self.PlayersCards(player2)
			index2 = self.RankOfCombination(combination2)
			logger.info('Player 2:')
			logger.info('{}, cards : {}.'.format(combination2, player2))
			# logger.debug('index2 = {}'.format(index2))
			if combination1 == 'Royal Flush' and combination2 == 'Royal Flush':
				logger.info('Dead heat')
			elif index1 > index2:
				logger.info('{} is winner'.format("Player 1"))
				count += 1
			elif index1 < index2:
				logger.info('{} is winner'.format("Player 2"))
				count2 += 1
			elif index1 == index2:
				logger.info('combinations are equal')
				# logger.debug('combination : {}, cards : {}, suit {}.'.format(combination1, cards1,suits1))
				arr1 = ["High Card", "Straight Flush", "Straight", "Flush"] 
				arr2 = ["Four of a Kind", "Full House"]
				arr3 = ["One Pair", "Three of a Kind"]
				if combination1 in arr1:
					highest_card1, ind_hight_card1 = self.HighestСard1(cards1)
					highest_card2, ind_hight_card2 = self.HighestСard1(cards2)
					if ind_hight_card1 > ind_hight_card2:
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 1"))
						count += 1
					else:
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 2"))
						count2 += 1
				new1 = [*cards1] # отделяю ключи(карты) отдельно от количества из словаря
				new2 = [*cards2]
				if combination1 in arr2:
					if all_cards.index(new1[0]) > all_cards.index(new2[0]):
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 1"))
						count += 1
					elif all_cards.index(new1[0]) < all_cards.index(new2[0]):
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 2"))
						count2 += 1
				if combination1 in arr3:
					if all_cards.index(new1[0]) > all_cards.index(new2[0]):
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 1"))
						count += 1
					elif all_cards.index(new1[0]) < all_cards.index(new2[0]):
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 2"))
						count2 += 1
					else:
						highest_card1, ind_hight_card1 = self.HighestСard1(new1[1:])
						highest_card2, ind_hight_card2 = self.HighestСard1(new2[1:])
						if ind_hight_card1 > ind_hight_card2:
							logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
							logger.info('{} is winner'.format("Player 1"))
							count += 1
						else:
							logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
							logger.info('{} is winner'.format("Player 2"))
							count2 += 1
				if combination1 == "Two Pairs":
					logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
					highest_card2, ind_hight_card2 = self.HighestСard1(new2[:2])
					if ind_hight_card1 > ind_hight_card2:
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 1"))
						count += 1
					elif ind_hight_card1 < ind_hight_card2:
						logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
						logger.info('{} is winner'.format("Player 2"))
						count2 += 1
					else:
						highest_card1, ind_hight_card1 = self.HighestСard1(new1[2:])
						highest_card2, ind_hight_card2 = self.HighestСard1(new2[2:])
						if ind_hight_card1 > ind_hight_card2:
							logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
							logger.info('{} is winner'.format("Player 1"))
							count += 1
						else:
							logger.info('{} highest card - {}, {} highest card - {}'.format("Player 1", highest_card1, "Player 2", highest_card2))
							logger.info('{} is winner'.format("Player 2"))
							count2 += 1
		logger.debug(count)
		logger.debug(count2)
		file_txt.close()
		return count
if __name__ == "__main__":
	n = Problem054()
	print(n.PokerHands('p054_poker.txt'))