from Deck import Deck 


class PokerHand:

    def __init__(pokerhand):
        pokerhand.hand = []


    def AddCard(pokerhand, deck):
        pokerhand.hand.append(deck)

    def RevealFirstCard(pokerhand):
        if len(pokerhand.hand) > 0:
            pokerhand.hand[0].reveal()

    def ShowHand(pokerhand):
        handlist = []
        for i, card in enumerate(pokerhand.hand):
            if i == 0 and not card.faceUp:
                handlist.append('XX')
            else:
                handlist.append(card.show())
        return handlist

    def GetHandValue(pokerhand):
        count = 0
        numAces = 0
        
        for card in pokerhand.hand:
            if card.faceUp == False:
                count += 0
            elif card.value == 'A':
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
