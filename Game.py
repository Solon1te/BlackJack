from PokerHand import PokerHand 
from Deck import Deck
import time

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
        game.dealerHand.hand[0].hide()
        print(game.dealerHand.hand[0].show())
        print(game.dealerHand.hand[1].show())

    
    def PlayerTurn(game):
        playerInput = ''
        while playerInput.lower() != 's':
            if playerInput.lower() == ord('h'):
                game.PlayerDrawCard()

    def DealerTurn(game):
        game.dealerHand.RevealFirstCard()
        dealerCount = game.dealerHand.GetHandValue()
        while dealerCount < 17:
            game.DealerDrawCard()
            time.sleep(1)
            dealerCount = game.dealerHand.GetHandValue()
        if game.ExceedMaxValue(dealerCount):
            game.playerStatus = 'W'
        else:
            playerCount = game.playerHand.GetHandValue()
            if dealerCount > playerCount:
                game.playerStatus = 'L'
            elif dealerCount == playerCount:
                game.playerStatus = 'T'
            else:
                game.playerStatus = 'W'

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



    def ExceedMaxValue(game, count):
        if count > game.maxVal:
            return True
        else: 
            return False
