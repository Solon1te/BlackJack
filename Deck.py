from Card import Card
import random


class Deck:
    SUITS = ['♥', '♦', '♣', '♠']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]

    def __init__(deck):
        deck.cards = []
        for s in SUITS:
            for v in VALUES:
                card = Card(suit,value)
                deck.cards.append(card)

    def DrawCard(deck):
        i = random.randint(0, len(deck.cards))
        drawnCard = deck.pop(i)
        return [drawnCard]
    