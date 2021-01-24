from board import Board 
from player import Player
from tools import typewriter, player_winning
import copy

def get_amount_of_players():
    typewriter('Enter amount of players: ')
    amount = input()
    
    while not amount.isdigit():
        typewriter('Error!\nEnter amount of players: ')
        amount = input()

    return int(amount)

def main():
    amount_of_players = get_amount_of_players()
    players = []

    for i in range(amount_of_players):
        player = Player(i + 1)
        player.s_board.generate()
        players.append(player)

    for i in range(amount_of_players - 1):
        players[i].e_board.board = players[i + 1].s_board.board

    players[amount_of_players - 1].e_board.board = players[0].s_board.board
    winner = 0
    while True:
        if amount_of_players == 1:
            print('Player ' + players[0].name + ' won!')
            exit(0)

        for i in range(winner, amount_of_players):
            players[i].make_step()
            if players[i].e_board.winning_arrangement():
                if i != amount_of_players - 1:
                    print('Player ' + players[i + 1].name + ' lost!')
                    del players[i + 1]
                    amount_of_players -= 1
                    if i + 1 == amount_of_players:
                        players[i].e_board.board = players[0].s_board.board
                    else:
                        players[i].e_board.board = players[i + 1].s_board.board
                    winner = i
                else:
                    print('Player ' + players[0].name + ' lost!')
                    del players[0]
                    amount_of_players -= 1
                    players[amount_of_players - 1].e_board.board = players[0].s_board.board
                    winner = amount_of_players - 1
                break
            else:
                print('not win!')
                winner = 0
    
if __name__ == '__main__':
    main()