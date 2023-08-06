import os
import random

from Card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def load_cards_from_directory(self, directory_path):
        card_files = [file_name[:-3] for file_name in os.listdir(directory_path) if file_name.endswith('.py')]
        # change directory path to cards.deck.builder
        dotted_path = directory_path.replace('/', '.')

        for card_file in card_files:
            module_name = f"{dotted_path}{card_file}"
            try:
                module = __import__(module_name, fromlist=['*'])
                card_dict = module.card_dict
                card = Card(card_dict)
                self.add_card(card)
            except (ImportError, AttributeError):
                print(f"Error loading card from {card_file}")

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


