
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.faceUp = True
        
    def show(self, faceUp = True):
        if faceUp:
            print('{}{}'.format(self.value, self.suit))
        else:
            print('XX')
            
    def reveal(self):
        self.faceUp = True
        
    def hide(self):
        self.faceUp = False

    def Draw(self, faceUp=True):
        if faceUp:
            return self
        else: 
            return ' '