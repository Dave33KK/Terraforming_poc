class Player:

    def __init__(self, ip: str, name: str):
        self.ip = ip
        self.name = name

        '''PRODUCTION, INCOME AND RESOURCES'''
        self.terra_score = 20
        self.gold_prod = 0
        self.income_gold = self.terra_score + self.gold_prod
        self.gold = 0

        self.steel_prod = 0
        self.steel = 0

        self.titanium_prod = 0
        self.titanium = 0

        self.lumber_prod = 0
        self.lumber = 0

        self.energy_prod = 0
        self.energy = 0

        self.heat_prod = 0
        self.heat = 0

        '''MARKERS'''
        self.markers = {
            'builder': 0,
            'titanium': 0,
            'science': 0,
            'plant': 0,
            'bacteria': 0,
            'animal': 0,
            'energy': 0,
            'saturn': 0,
            'earth': 0,
            'event': 0,
            'city': 0  # TO DO: add city marker to game state
        }

        '''CARDS'''
        self.card_in_hand = []

    '''using update instead of set, because we always work with current values'''
    '''GETTER AND SETTER FOR PRODUCTION, INCOME AND RESOURCES'''

    def __repr__(self):
        return f"Player {self.name} with IP {self.ip}"

    def update_terra_score(self, number: int):
        self.terra_score = self.terra_score + number

    def get_terra_score(self):
        return self.terra_score

    def update_gold_prod(self, number: int):
        self.gold_prod = self.gold_prod + number

    def get_gold_prod(self):
        return self.gold_prod

    def update_gold(self, number: int):
        self.gold = self.gold + number

    def get_gold(self):
        return self.gold

    def update_steel_prod(self, number: int):
        self.steel_prod = self.steel_prod + number

    def get_steel_prod(self):
        return self.steel_prod

    def update_steel(self, number: int):
        self.steel = self.steel + number

    def get_steel(self):
        return self.steel

    def update_titanium_prod(self, number: int):
        self.titanium_prod = self.titanium_prod + number

    def get_titanium_prod(self):
        return self.titanium_prod

    def update_titanium(self, number: int):
        self.titanium = self.titanium + number

    def get_titanium(self):
        return self.titanium

    def update_lumber_prod(self, number: int):
        self.lumber_prod = self.lumber_prod + number

    def get_lumber_prod(self):
        return self.lumber_prod

    def update_lumber(self, number: int):
        self.lumber = self.lumber + number

    def get_lumber(self):
        return self.lumber

    def update_energy_prod(self, number: int):
        self.energy_prod = self.energy_prod + number

    def get_energy_prod(self):
        return self.energy_prod

    def update_energy(self, number: int):
        self.energy = self.energy + number

    def get_energy(self):
        return self.energy

    def update_heat_prod(self, number: int):
        self.heat_prod = self.heat_prod + number

    def get_heat_prod(self):
        return self.heat_prod

    def update_heat(self, number: int):
        self.heat = self.heat + number

    def get_heat(self):
        return self.heat

    '''since income_gold gets defined by terra_score and gold_prod, function update_income_gold would be misleading'''

    def get_income_gold(self):
        return self.income_gold

    '''TO DO: return all income / game state'''

    def get_total_income(self):
        return [self.get_income_gold(), self.get_steel_prod()]

    def initiate_total_income(self):
        self.gold = self.gold + self.get_income_gold()
        self.steel = self.steel + self.get_steel_prod()
        self.titanium = self.titanium + self.get_titanium_prod()
        self.lumber = self.lumber + self.get_lumber_prod()
        '''energy gets transformed into heat at the end of every round'''
        self.heat = self.heat + self.energy + self.get_heat_prod()
        self.energy = self.get_energy_prod()

    '''SETTER AND GETTER FOR MARKERS'''

    def update_marker(self, marker_type: str, number: int):
        if marker_type in self.markers:
            self.markers[marker_type] = self.markers[marker_type] + number
        else:
            raise ValueError(f"Invalid key: {marker_type}")

    def get_marker(self, marker_type: str):
        if marker_type in self.markers:
            return self.markers[marker_type]
        else:
            raise ValueError(f"Invalid key: {marker_type}")

    '''CARDS'''

    def get_card_in_hand(self):
        return self.card_in_hand

    def add_card_to_hand(self, card):
        self.card_in_hand.append(card)
