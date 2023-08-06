class Card:

    def __init__(self, card_dict: dict):
        self.name = card_dict.get('name')
        self.id = card_dict.get('id')
        self.cost = card_dict.get('cost')
        self.description = card_dict.get('description')
        self.dict = card_dict
        #TODO - add __description__ in dict format







