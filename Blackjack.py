import curses
from Game import Game
from PokerHand import PokerHand 
from Deck import Deck
from curses import wrapper
import random
import time

def main(stdscr):
    game = Game()
    game.deck.build()
    game.deck.Shuffle()
    game.Deal()
    stdscr.clear()
    stdscr.addstr( 5, 10, 'BLACKJACK')
    stdscr.addstr( 7, 2, 'Press Any Key To Continue')
    stdscr.refresh()
    stdscr.getkey()

    if game.playerStatus == 'P':
        stdscr.clear()
        stdscr.addstr( 1, 10, f'Dealer Hand: {game.dealerHand.ShowHand()}')
        stdscr.addstr( 2, 10, f'Dealer Count: {game.dealerHand.GetHandValue()}')
        stdscr.addstr( 7, 10, 'Press H to Hit')
        stdscr.addstr( 8, 9, 'Press S to Stand')
        stdscr.addstr( 14, 10, f'Player Cards:{game.playerHand.ShowHand()}')
        stdscr.addstr( 15, 10, f'Player Count: {game.playerHand.GetHandValue()}')
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
    if key == ord('S') or key == ord('s'):
        dealerDrawCard(RandNumGen())
        dealerCount = updateCount(dealerHand)
        stdscr.addstr( 1, 10, f'Dealer Card: {dealerHand}')
        stdscr.addstr( 2, 10, f'Dealer Count: {dealerCount}')
        stdscr.refresh()
        while dealerCount < playerCount:
            time.sleep(1)
            dealerDrawCard(RandNumGen())
            dealerCount = updateCount(dealerHand)
            stdscr.addstr( 1, 10, f'Dealer Card: {dealerHand}')
            stdscr.addstr( 2, 10, f'Dealer Count: {dealerCount}')
            stdscr.refresh()
            if playerCount > dealerCount:
                time.sleep(1)
                stdscr.clear()
                stdscr.addstr( 6, 12, 'WINNER')
                stdscr.addstr( 8, 11, 'You Win!')
                stdscr.refresh()
                stdscr.getkey()
    if game.playerStatus == 'T':
        time.sleep(1)
        stdscr.clear()
        stdscr.addstr( 6, 12, 'PUSH')
        stdscr.addstr( 7, 6, 'Game Was A Tie')
        stdscr.refresh()
        stdscr.getkey()
    if game.playerStatus == 'W':
        time.sleep(1)
        stdscr.clear()
        stdscr.addstr( 6, 12, 'DEALER BUSTED')
        stdscr.addstr( 8, 14, 'You Win!')
        stdscr.refresh()
        stdscr.getkey()
    if game.playerStatus == 'L':
        time.sleep(1)
        stdscr.clear()
        stdscr.addstr( 6, 12, 'DEALER WINS')
        stdscr.addstr( 8, 10, 'You LOSE!')
        stdscr.refresh()
        stdscr.getkey()
    
    #Pause To Let Player Realize They Have Lost.
    time.sleep(1)
    #Game Over
    GameOver = True
    stdscr.clear()
    stdscr.addstr(6, 12, 'BUST!')
    stdscr.addstr(7, 10, 'You Lost!')
    stdscr.addstr(9, 4, 'Press Ctrl + C to Exit')
    stdscr.refresh()
    stdscr.getkey()
wrapper(main)