import random

suits = ('Spades', 'Clubs', "Diamonds", 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
again = False

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
		return card


class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

class Chips:

	def __init__(self, total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input('How much do you bet? '))
		except ValueError:
			print("The bet needs to be an integer")
		if(chips.bet <= 0):
			chips.bet = input('Bet needs to be above zero. Press enter to continue ')
		else:
			if chips.bet > chips.total:
				print("You can only bet up to {} chips!".format(chips.total))
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck, hand):
	global playing

	while True:
		choice = input("\nWould you like to hit or stand? Enter 'h' or 's' ")

		if choice[0].lower() == 'h':
			hit(deck,hand)

		elif choice[0].lower() == 's':
			print("Player stands. Dealer's turn.")
			playing = False

		else:
			print("You must enter 'h' or 's' ")
			continue
		break


def show_some(player,dealer):
	print("\nDealer's Hand:")
	print(" <hidden card>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)
	print("\n")
    
def show_all(player,dealer):
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)
	print("\n")

def player_busts(chips):
    print("You bust")
    chips.lose_bet()

def player_wins(chips):
    print("You win!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("You tie with the dealer! It's a push.")




while True:
	print("\nWelcome to Blackjack!")

	deck = Deck()
	deck.shuffle()
	p_hand = Hand()
	d_hand = Hand()
	p_hand.add_card(deck.deal())
	d_hand.add_card(deck.deal())
	p_hand.add_card(deck.deal())
	d_hand.add_card(deck.deal())

	
	if not again:
	
		p_chips = Chips()

	
	take_bet(p_chips)

	show_some(p_hand, d_hand)

	while playing:

		hit_or_stand(deck, p_hand)
		show_some(p_hand, d_hand)

		if p_hand.value > 21:
			player_busts(p_chips)
			break

	if p_hand.value <= 21:
		while d_hand.value < 17:
			hit(deck, d_hand)

		show_all(p_hand, d_hand)

		if d_hand.value > 21:
			dealer_busts(p_chips)

		elif d_hand.value > p_hand.value:
			dealer_wins(p_chips)

		elif d_hand.value < p_hand.value:
			player_wins(p_chips)

		else:
			push()

	print("\n Your chip count is now {}".format(p_chips.total))

	if p_chips.total > 0:
		new_game = input("Up for another hand? Enter 'y' to continue: ")

		if new_game[0].lower() == 'y':
			playing = True
			again = True
			continue
		else:
			print("Your final chip count was {}".format(p_chips.total))
			break
	else:
		print("You're out of chips! Tough luck!")
		break
	













