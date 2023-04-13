import curses
from curses import wrapper
import random
import time

def main(stdscr):
    playerHand = []
    PlayerCount = 0
    dealerHand = []
    usedCards = []
    GameOver = False
    suits = ['♥', '♦', '♣', '♠']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]

    #Deck Is Created And Placed in a variable Deck List 
    def CreateADeck():
        deck = []
        for s in suits:
            for v in values:
                deck.append((v+s))
        return deck

    deck = CreateADeck()


    #Random Number Generator For Deck (Should....Only select each card once... Doesn't Seem To)
    def RandNumGen():
        Num = random.randint(0,51)
        while Num in usedCards:
            Num = random.randint(0,51)
        usedCards.append(Num)
        return Num

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
        if GameOver == False:
            DrawnCard = deck.pop(i)
            playerHand.append(DrawnCard)
            return [DrawnCard]

    def dealerDrawCard(i):
        DrawnCard = deck.pop(i)
        dealerHand.append(DrawnCard)
        return [DrawnCard]

    stdscr.clear()
    stdscr.addstr( 5, 10, 'BLACKJACK')
    stdscr.addstr( 7, 2, 'press any key to continue')
    stdscr.refresh()
    stdscr.getkey()
    
    stdscr.clear()
    dealerDrawnCards = ((dealerDrawCard(RandNumGen())) + dealerDrawCard(RandNumGen()))
    playerDrawnCards = ((playerDrawCard(RandNumGen())) + playerDrawCard(RandNumGen()))
    dealerCount = updateCount(dealerHand)
    playerCount = updateCount(playerHand)
    while playerCount < 22:
        stdscr.addstr( 1, 10, f'Dealer Card: {dealerHand[0]}')
        stdscr.addstr( 2, 10, f'Dealer Count: {dealerCount}')
        stdscr.addstr( 7, 10, 'Press H to Hit')
        stdscr.addstr( 8, 9, 'Press S to Stand')
        stdscr.addstr( 14, 6, f'Player Cards:{playerHand}')
        stdscr.addstr( 15, 6, f'Player Count: {playerCount}')
        key = stdscr.getch()
        if key == ord('H') or key == ord('h'):
            playerDrawCard(RandNumGen())
            playerCount = updateCount(playerHand)
            stdscr.addstr(14, 6, f'Player Cards:{playerHand}')
            stdscr.addstr( 15, 6, f'Player Count: {playerCount}')
            stdscr.refresh()
        stdscr.addstr(14, 6, f'Player Cards:{playerHand}')
        stdscr.addstr( 15, 6, f'Player Count: {playerCount}')
        stdscr.refresh()

    #Pause To Let Player Know They Have Lost.
    time.sleep(1)
    GameOver = True
    stdscr.clear()
    stdscr.addstr(7, 12, 'BUST!')
    stdscr.addstr(8, 10, 'You Lose!')
    stdscr.refresh()
    stdscr.getkey()
wrapper(main)