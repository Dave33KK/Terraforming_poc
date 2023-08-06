from Player import Player
from Deck import Deck

from pprint import pprint


# Create a deck and load cards from the specified directory, shuffle deck
card_directory = 'cards/deck/builder/'
deck = Deck()
deck.load_cards_from_directory(card_directory)
deck.shuffle()


player = Player('my_ip_8123.123', 'David')

print(player)

print(player.card_in_hand)

player.add_card_to_hand(deck.pop_card())

pprint(player.card_in_hand[0].dict)







