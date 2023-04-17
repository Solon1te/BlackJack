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
    
    def Show(self):
        for c in self.cards:
            c.show()

    def Shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

        
    def Draw(self):
        return self.cards.pop()
