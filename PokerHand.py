class PokerHand:

    def __init__(pokerHand):
        pokerHand.cards = []


    def AddCard(pokerHand, card):
        playerHand.append(card)

    def GetHandValue(pokerHand):
        count = 0
        numAces = 0
        for card in pokerHand.cards:
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
        
    
