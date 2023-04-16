from PokerHand import PokerHand 
from Deck import Deck

class Game:

    def __init__(game):
        game.playerHand = PokerHand()
        game.dealerHand = PokerHand()
        game.deck = Deck()
        game.maxVal = 21
        game.playerStatus = 'P'
    
    def Deal(game):
        for x in range(2):
            game.PlayerDrawCard()
            game.DealerDrawCard()
    
    def PlayerTurn(game):
        playerInput = ''
        while playerInput.lower() != 's':
            stdscr.addstr( 7, 10, 'Press H to Hit')
            stdscr.addstr( 8, 9, 'Press S to Stand')
            playerInput = stdscr.getch()
            if playerInput.lower() == ord('h'):
                game.PlayerDrawCard()

    def PlayerDrawCard(game):
        playerCard = game.deck.DrawCard()
        game.playerHand.AddCard(playerCard)
        
        playerCount = game.playerHand.GetHandValue()
        if game.ExceedMaxValue(playerCount):
            game.playerStatus = 'L'   

    def DealerDrawCard(game):
        dealerCard = game.deck.DrawCard()
        game.dealerHand.AddCard(dealerCard)

        dealerCount = game.dealerHand.GetHandValue()
        if game.ExceedMaxValue(dealerCount):
            game.playerStatus = 'W'   


    def ExceedMaxValue(game, count):
        if count > game.maxVal:
            return True
        else: 
            return False


Game.deck.show()