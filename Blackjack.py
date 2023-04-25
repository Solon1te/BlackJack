import curses
from Game import Game
from PokerHand import PokerHand 
from Deck import Deck
from curses import wrapper
import time

def main(stdscr):
    GameOver = False
    game = Game()
    game.deck.build()
    game.deck.Shuffle()
    game.Deal()

    player_count = game.playerHand.GetHandValue()
    player_hand = game.playerHand.ShowHand()

    dealer_count = game.dealerHand.GetHandValue()
    dealer_hand = game.dealerHand.ShowHand()

    player_win = curses.newwin(2, 60, 14, 10)
    dealer_win = curses.newwin(2, 60, 1, 10)

    stdscr.clear()
    stdscr.addstr( 5, 10, 'BLACKJACK')
    stdscr.addstr( 7, 2, 'Press Any Key To Continue')
    stdscr.refresh()
    stdscr.getkey()
    while GameOver == False:
        if game.playerStatus == 'P':
            stdscr.clear()
            dealer_win.clear()
            player_win.clear()

            dealer_win.addstr( f'Dealer Hand: {dealer_hand} \nDealer Count: {dealer_count} ')
            
            stdscr.addstr( 7, 10, 'Press H to Hit')
            stdscr.addstr( 8, 9, 'Press S to Stand')
            player_win.addstr( f'Player Cards:{player_hand} \nPlayer Count: {player_count}')
            
            stdscr.refresh()
            dealer_win.refresh()
            player_win.refresh()


            key = stdscr.getch()

        if key == ord('H') or key == ord('h'):
            player_win.clear()
            game.playerHand.AddCard(game.deck.Draw())
            player_hand = game.playerHand.ShowHand() 
            player_count = game.playerHand.GetHandValue()
            player_win.addstr( f'Player Cards:{player_hand} \nPlayer Count: {player_count}')
            player_win.refresh()
            if game.ExceedMaxValue(player_count):
                GameOver = True


        if key == ord('S') or key == ord('s'):
            dealer_win.clear()
            game.DealerTurn()
            dealer_count = game.dealerHand.GetHandValue()
            dealer_hand = game.dealerHand.ShowHand()
            dealer_win.addstr( f'Dealer Hand: {game.dealerHand.ShowHand()} \nDealer Count: {dealer_count}')
            dealer_win.refresh()
            time.sleep(1)
            while dealer_count < player_count:
                time.sleep(1)
                dealer_win.clear()
                game.DealerDrawCard(game.deck.Draw())
                dealer_count = game.dealerHand.GetHandValue()
                dealer_hand = game.dealerHand.ShowHand()
                dealer_win.addstr( f'Dealer Hand: {dealer_hand} \nDealer Count: {dealer_count}')
                dealer_win.refresh()
                time.sleep(1)
                if player_count > dealer_count:
                    time.sleep(1)
                    stdscr.clear()
                    stdscr.addstr(1, 2, f'Dealer Hand: {game.playerHand.ShowHand()}')
                    stdscr.addstr(2, 2, f'Dealer Count: {game.playerHand.GetHandValue()}')
                    stdscr.addstr( 6, 12, 'WINNER')
                    stdscr.addstr( 8, 11, 'You Win!')
                    stdscr.addstr(14, 2, f'Player Hand: {game.playerHand.ShowHand()}')
                    stdscr.addstr(15, 2, f'Player Count: {game.playerHand.GetHandValue()}')
                    stdscr.refresh()
                    stdscr.getkey()
        if game.playerStatus == 'T':
            time.sleep(1)
            stdscr.clear()
            stdscr.addstr( 6, 12, 'PUSH')
            stdscr.addstr( 7, 7, 'Game Was A Tie')
            stdscr.refresh()
            stdscr.getkey()
        if game.playerStatus == 'W':
            time.sleep(1)
            stdscr.clear()
            dealer_count = game.dealerHand.GetHandValue()
            dealer_hand = game.dealerHand.ShowHand()
            stdscr.addstr(1, 2, f'Dealer Hand: {dealer_hand}')
            stdscr.addstr(2, 2, f'Dealer Count: {dealer_count}')
            stdscr.addstr( 6, 12, 'DEALER BUSTED')
            stdscr.addstr( 8, 14, 'You Win!')
            stdscr.refresh()
            stdscr.getkey()
        if game.playerStatus == 'L':
            time.sleep(1)
            stdscr.clear()
            stdscr.addstr( 6, 12, 'DEALER WINS')
            stdscr.addstr( 8, 13, 'You LOSE!')
            stdscr.refresh()
            stdscr.getkey()
    
    #Pause To Let Player Realize They Have Lost.
    time.sleep(1)
    #Game Over
    if GameOver == True:
        stdscr.clear()
        stdscr.addstr(1, 2, f'Player Hand: {game.playerHand.ShowHand()}')
        stdscr.addstr(2, 2, f'Player Count: {game.playerHand.GetHandValue()}')
        stdscr.addstr(5, 12, 'BUST!')
        stdscr.addstr(6, 10, 'You Lost!')
        stdscr.addstr(9, 4, 'Press Ctrl + C to Exit')
        stdscr.refresh()
        stdscr.getkey()
wrapper(main)


