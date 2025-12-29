from card import Card, Palo
import random

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Palo.__members__ for rank in [1,2,3,4,5,6,7,10,11,12]]
        
    def shuffle(self):
        random.shuffle(self.cards)