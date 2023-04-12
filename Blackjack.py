import curses
from curses import wrapper
import random

def main(stdscr):
    playerHand = []
    dealerHand = []
    suits = ['♥', '♦', '♣', '♠']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]

    def CreateADeck():
        deck = []
        for s in suits:
            for v in values:
                deck.append((v+s))
        return deck

    deck = CreateADeck()

        #Create a for loop the goes through hand and updates player count
    def updateCount(hand, count = 0):
        for card in hand:
            if card[0] == 'A' and count >= 11:
                count += 1
            elif card[0] == 'A' and count <= 10:
                count += 11
            elif card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0:2] == '10':
                count += 10
            else:
                count += int(card[0])
        return count

    def playerDrawCard(i):
        DrawnCard = deck.pop(i)
        playerHand.append(DrawnCard)
        return [DrawnCard]

    stdscr.clear()
    stdscr.addstr( 5, 10, 'BLACKJACK')
    stdscr.addstr( 7, 2, 'press any key to continue')
    stdscr.refresh()
    stdscr.getkey()

    stdscr.clear()
    playerDrawnCards = (playerDrawCard(random.randint(0,51)) + playerDrawCard(random.randint(0,51)))
    playerCount = updateCount(playerHand)
    stdscr.addstr( 14, 10, f'Player Cards:{playerDrawnCards}')
    stdscr.addstr( 15, 10, f'Player Count: {playerCount}')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)