import random

suits = ('Spades', 'Clubs', "Diamonds", 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		
	def __str__(self):
		return('{} of {}'.format(self.rank, self.suit))

class Deck:
	def __init__(self):
		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(rank, suit))

	def __str__(self):
		ret = []

		for card in self.deck:
			ret.append('{} of {}'.format(card.rank, card.suit))

		return str(ret)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		card = self.deck.pop()
		print(card)


class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.acves -= 1

class Chips:

	def __init__(self, total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True
		try:
			chips.bet = int(input('How much do you bet? '))
		except:
			print("The bet needs to be an integer")
		else:
			if chips.bet > chips total:
				print("You can only bet up to {} chips!".format(chips.bet))
			else:
				break







