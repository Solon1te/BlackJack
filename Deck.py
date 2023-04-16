from Card import Card
import random

class Deck:

    def __init__(self):
        self.cards = []
        self.build()
        
        
    def build(self):
        for s in ['♥', '♦', '♣', '♠']:
            for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]:
                self.cards.append(Card(s,v))


    def DrawCard(self):
        i = random.randint(0, len(self.cards)-1)
        drawnCard = self.cards.pop(i)
        return drawnCard
    
    def show(self):
        for c in self.cards:
            c.show()
 