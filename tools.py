from time import sleep
import sys

def typewriter(string):
    """
    smoothly printing string 
    :param line: line which we have to print 
    :return:     None
    """
    for letter in string:
        print(letter, end='')
        sys.stdout.flush()
        sleep(0.01)

def player_winning(player):
    """
    checks whether winning position or not
    :param player: Player class object
    :return: True - win, False - not win
    """

    count = 0
    
    for i in range(10):
        for j in range(10):
            if player.e_board.board[i][j] == 2:
                count += 1
    
    return True if count == 20 else False
    
    pass