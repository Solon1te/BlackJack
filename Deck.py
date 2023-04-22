from Card import Card
import random

class Deck:

    def __init__(deck):
        deck.cards = []
        deck.build()
        
        
    def build(deck):
        for s in ['♥', '♦', '♣', '♠']:
            for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]:
                deck.cards.append(Card(s,v))
    
    def Show(deck):
        for c in deck.cards:
            c.show()

    def Shuffle(deck):
        for i in range(len(deck.cards)-1, 0, -1):
            r = random.randint(0, i)
            deck.cards[i], deck.cards[r] = deck.cards[r], deck.cards[i]

        
    def Draw(deck):
        return deck.cards.pop()
