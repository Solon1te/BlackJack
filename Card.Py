
class Card():
    def __init__(card, suit, value):
        card.suit = suit
        card.value = value
        card.faceUp = True

    def show(card, faceUp = True):
        if faceUp:
            return('{}{}'.format(card.value, card.suit))
        else:
            return('XX')
            
    def reveal(card):
        card.faceUp = True
        
    def hide(card):
        card.faceUp = False

    def Draw(card, faceUp=True):
        if faceUp:
            return card
        else: 
            return ' '