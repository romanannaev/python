#black-jack
#от 1 до 7 against dealer
import cards, games
class BJ_Card(cards.Card):
	""" Card for game in black-jack """
	ACE_VALUE = 1
	@property
	def value(self):
		if self.is_face_up:
			v = BJ_Card.RANKS.index(self.rank) + 1
			if v > 10:
				v = 10
		else:
			v = None
		return v

class BJ_Deck(cards.Deck):
	""" Deck for game Black-jack"""
	def populate(self):
		for suit in BJ_Card.SUITS:
			for rank in BJ_Card.RANKS:
				self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
	""" 'Hand:' set card "black-jack" one player """
	def __init__(self,name):
		super(BJ_Hand, self).__init__()
		self.name = name

	def __str__(self):
		rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
		if self.total:
			rep += "(" + str(self.total) + ")"
		return rep

	@property
	def total(self):
		#если у одной карты value равно None, то и все свойство равно None
		for card in self.cards:
			if not card.value:
				return None
		#суммируем очки, считая каждый туз за 1 очко
		t = 0
		for card in self.cards:
			t += card.value
		#определяем, есть ли туз на руках у игрока
		contains_ace = False
		for card in self.cards:
			if card.value == BJ_Card.ACE_VALUE:
				contains_ace = True
		#если на руках есть туз и сумма очков не превышает 11,будем считать туз за 11 очков
		if contains_ace and t <= 11:
			#прибавить лишь 10, потому что еденица уже вошла в общую сумму
			t += 10
		return t
	
	def is_busted(self):
		return self.total > 21

class BJ_Player(BJ_Hand):
	""" Player in "Black-jack". """
	def is_hitting(self):
		response = games.ask_yes_no("\n" + self.name + ", будете брать еще карты? (Y/N): ")
		return response == "y"
	
	def bust(self):
		print(self.name, "перебрал.")
		self.lose()

	def lose(self):
		print(self.name, "проиграл.")
	
	def win(self):
		print(self.name, "выиграл.")
	
	def push(self):
		print(self.name, "сыграл с компьютером вничью.")

class BJ_Dealer(BJ_Hand):
	""" Dealer in game "Black-jack"."""
	def is_hitting(self):
		return self.total < 17
	
	def bust(self):
		print(self.name, "перебрал")
	
	def flip_first_card(self):
		first_card = self.cards[0]
		first_card.flip()

class BJ_Game(object):
	""" Game to 'Black-jack' """
	def __init__(self,names):
		self.players = []
		for name in names:
			player = BJ_Player(name)
			self.players.append(player)
		self.dealer = BJ_Dealer("DEALER")
		self.deck = BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()
	
	@property
	def still_playing(self):
		sp = []
		for player in self.players:
			if not player.is_busted():
				sp.append(player)
		return sp
	
	def __additional_cards(self, player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print(player)
			if player.is_busted():
				player.bust()
	
	def play(self):
		#сдача всем по 2 карты
		self.deck.deal(self.players + [self.dealer], per_hand=2)
		self.dealer.flip_first_card() #первая из карт,сданных дилеру,переворачивается
		#рубашкой вверх
		
		for player in self.players:
			print(player)
		print(self.dealer)
		#сдача дополнительных карт игрокам
		
		for player in self.players:
			self.__additional_cards(player)
		self.dealer.flip_first_card() #первая карта дилера раскрывается
		
		if not self.still_playing:
			#все игроки перебрали,покажем только  "руку " дилера
			print(self.dealer)
		else:
			#сдача дополнительных карт дилеру
			print(self.dealer) 
			self.__additional_cards(self.dealer)
			if self.dealer.is_busted():
				#выигрывают все,кто еще остался в игре
				for player in self.still_playing:
					player.win()
			else:
				#сравниваем суммы очков у дилера и у игроков,оставшихся в игре
				for player in self.still_playing:
					if player.total > self.dealer.total:
						player.win()
					elif player.total < self.dealer.total:
						player.lose()
					else:
						player.push()
		
		#удаление всех карт
		for player in self.players:
			player.clear()
		self.dealer.clear()

def main():
	print('\t\tДобро пожаловать за игровой стол Black-jack!\n')
	names = []
	number = games.ask_number('Сколько всего игроков?(1-7): ', low = 1, high = 8)
	for i in range (number):
		name = input ("Ведите имя игрока: ")
		names.append(name)
		print()
	game = BJ_Game(names)
	again = None
	while again != "n":
		game.play()
		again = games.ask_yes_no('\nDo you want to play one more time?(y/n):')
		main()
	input("\nPress enter for exit.")

main()