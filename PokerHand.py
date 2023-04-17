from Deck import Deck 


class PokerHand:

    def __init__(self):
        self.hand = []


    def AddCard(self, deck):
        self.hand.append(deck.Draw())

    def ShowHand(self):
        for card in self.hand:
            card.show()

    def GetHandValue(self):
        count = 0
        numAces = 0
        for card in self.hand:
            if card.value == 'A':
                numAces += 1
            elif card.value == 'J' or card.value == 'Q' or card.value == 'K' or card.value == '10':
                count += 10
            else:
                count += int(card.value) 
        for x in range(numAces):
            if count >= 11:
                count += 1
            else: 
                count += 11
        return count

