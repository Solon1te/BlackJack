import curses
from curses import wrapper
import random

suits = ['♥', '♦', '♣', '♠']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',' K' ]

def CreateADeck():
    deck = []
    for s in suits:
        for v in values:
            deck.append((v+s))
    return deck

deck = CreateADeck()


def main(stdscr):
    stdscr.clear()
    stdscr.addstr( 5, 10, 'BLACKJACK')
    stdscr.addstr( 7, 2, 'press any key to continue')
    stdscr.refresh()
    stdscr.getkey()
    stdscr.addstr(f'deck:{deck}')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)