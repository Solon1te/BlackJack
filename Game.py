from PokerHand import PokerHand 
from Deck import Deck

class Game:

    def __init__(self):
        self.playerHand = PokerHand()
        self.dealerHand = PokerHand()
        self.deck = Deck()
        self.maxVal = 21
        self.playerStatus = 'P'
    
    def Deal(game):
        for x in range(2):
            game.PlayerDrawCard()
            game.DealerDrawCard()
        game.dealerHand.hand[0].hide()
        # print(game.dealerHand.hand[0].show())
        # print(game.dealerHand.hand[1].show())

    
    def PlayerTurn(game):
        playerInput = ''
        while playerInput.lower() != 's':
            if playerInput.lower() == ord('h'):
                game.PlayerDrawCard()

    def PlayerDrawCard(game):
        playerCard = game.deck.Draw()
        game.playerHand.AddCard(playerCard)
        
        playerCount = game.playerHand.GetHandValue()
        if game.ExceedMaxValue(playerCount):
            game.playerStatus = 'L'   

    def DealerDrawCard(game, faceUp=True):
        dealerCard = game.deck.Draw()
        game.dealerHand.AddCard(dealerCard)

        dealerCount = game.dealerHand.GetHandValue()
        if game.ExceedMaxValue(dealerCount):
            game.playerStatus = 'W'

        # Show the dealer's card
        if len(game.dealerHand.hand) == 1:
            game.dealerHand.hand[0].show(faceUp = False)

        else:
            for card in game.dealerHand.hand:
                card.show(faceUp=True) 


    def ExceedMaxValue(game, count):
        if count > game.maxVal:
            return True
        else: 
            return False

game = Game()
game.deck.Shuffle()
game.Deal()
# game.dealerHand.ShowHand()
# print(game.dealerHand.GetHandValue())