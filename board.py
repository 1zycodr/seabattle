import random
from constants import *
from my_exception import Wrong_move, Hit_move, Destroy_move
class Board:
    four_deck = list()
    def __init__(self, id):
        self.board = [0] * 10
        self.id = id
        for i in range(10):
            self.board[i] = [FREE] * 10
        
    def set_ship(self, coordinates):
        """
        setting ship on the board, excluding its borders
        :param coordinates: list of coordinates (i, j) of ship points on border
        :return: None
        """

        for i, j in coordinates:
            self.board[i][j] = INTACT_DECK
        
        for i, j in coordinates:
            if j != 9:
                if self.board[i][j + 1] != INTACT_DECK:
                    self.board[i][j + 1] = ADJACENT
                if i != 0:
                    if self.board[i - 1][j + 1] != INTACT_DECK:
                        self.board[i - 1][j + 1] = ADJACENT
                if i != 9:
                    if self.board[i + 1][j + 1] != INTACT_DECK:
                        self.board[i + 1][j + 1] = ADJACENT
            
            if j != 0:
                if self.board[i][j - 1] != INTACT_DECK:
                    self.board[i][j - 1] = ADJACENT
                if i != 0:
                    if self.board[i - 1][j - 1] != INTACT_DECK:
                        self.board[i - 1][j - 1] = ADJACENT
                if i != 9:
                    if self.board[i + 1][j - 1] != INTACT_DECK:
                        self.board[i + 1][j - 1] = ADJACENT

            if i != 0:
                if self.board[i - 1][j] != INTACT_DECK:
                    self.board[i - 1][j] = ADJACENT

            if i != 9:
                if self.board[i + 1][j] != INTACT_DECK:
                    self.board[i + 1][j] = ADJACENT

            

    def get_possible_pos(self, ship_len):
        """
        returns possible positions for ship of size = size
        :param ship_len:    ship size
        :return:            list of possible coordinates
        """

        pos = list()

        for i in range(10):
            for j in range(ship_len, 11):
                #print(self.board[i][j - ship_len:j])   # получили значения клеток для корабля
                if ADJACENT not in self.board[i][j - ship_len:j] and INTACT_DECK not in self.board[i][j - ship_len:j]:
                    tmp_pos = list()
                    if ship_len != 1:
                        for k in range(ship_len):
                            tmp_pos.append((i, j - ship_len + k))
                    else:
                        tmp_pos = list()
                        tmp_pos.append((i, j - ship_len))
                    if tmp_pos not in pos:
                        pos.append(tmp_pos)

        for j in range(10):
            for i in range(10 - ship_len + 1):
                tmp = list()
                for k in range(ship_len):
                    tmp.append((i + k, j))

                is_free = True

                for m, n in tmp:
                    if self.board[m][n] == ADJACENT or self.board[m][n] == INTACT_DECK:
                        is_free = False
                
                if is_free and tmp not in pos:
                    pos.append(tmp)
        return pos
            
    def generate(self):
        """ 
        generating board
        2 - ship
        1 - engaged
        :return:    matrix 10x10
        """
        
        for ship_len in range(1, 5):
            for count in range(5 - ship_len):
                possible_pos = self.get_possible_pos(ship_len)
                new_ship = random.choice(possible_pos)
                if ship_len == 4:
                    for i in new_ship:
                        self.four_deck.append(i)
                self.set_ship(new_ship)
            
    def show_own_board(self):
        """
        printing own board
        X - destroyed deck
        O - intact deck
        :return: None
        """
        k = 1
        print("      A   B   C   D   E   F   G   H   I   J  ")
        print('    -----------------------------------------')
        for i in self.board:
            print(k, end='  ')
            if k != 10:
                print(end=' ')
            k += 1
            print('|', end=' ')
            for j in i:
                if j == INTACT_DECK:
                    print('O', '|', end = ' ')
                elif j == ATTACKED_FREE:
                    print('#', '|', end = ' ')
                elif j == ATTACKED_DECK or j == DEAD_SHIP:
                    print('X', '|', end = ' ')
                else:
                    print(' ', '|', end = ' ')
            print('\n    -----------------------------------------')
    
    def show_enemy_board(self):
        """
        printing enemy board
        X - destroyed deck
        O - intact deck
        :return: None
        """
        k = 1
        print("      A   B   C   D   E   F   G   H   I   J  ")
        print('    -----------------------------------------')
        for i in self.board:
            print(k, end='  ')
            if k != 10:
                print(end=' ')
            k += 1
            print('|', end=' ')
            for j in i:
                if j == ATTACKED_FREE:
                    print('#', '|', end = ' ')
                elif j == ATTACKED_DECK or j == DEAD_SHIP:
                    print('X', '|', end = ' ')
                else:
                    print(' ', '|', end = ' ')
            print('\n    -----------------------------------------')

    def show(self):
        """
        printing board with numbers
        :return: None
        """
        k = 1
        print("      A   B   C   D   E   F   G   H   I   J  ")
        print('    -----------------------------------------')
        for i in self.board:
            print(k, end='  ')
            if k != 10:
                print(end=' ')
            k += 1
            print('|', end=' ')
            for j in i:
                if j == 3:
                    print(j, '|', end = ' ')
                elif j == 4 or j == 5:
                    print(j, '|', end = ' ')
                else:
                    print(j, '|', end = ' ')
            print('\n    -----------------------------------------')

    def winning_arrangement (self):
        """
        checks whether winning position or not
        :return: True - win, False - not win
        """
        count = 0
    
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == DEAD_SHIP:
                    count += 1
    
        return True if count == 20 else False
    
    def ship_destroyed(self, i, j):
        """
        checks, the ship was destroyed or not
        :param i: y - coordinate of hitted deck
        :param j: x - coordinate of hitted deck
        :return True: If ship was destroyed
        :return False: If ship was not destroyed
        """
        for k in range(1, 4):
            if i - k >= 0:
                if self.board[i - k][j] == FREE or self.board[i - k][j] == ATTACKED_FREE or self.board[i - k][j] == ADJACENT:
                    break
                elif self.board[i - k][j] == INTACT_DECK:
                    return False
                                
        for k in range(1, 4):
            if i + k <= 9:
                if self.board[i + k][j] == FREE or self.board[i + k][j] == ATTACKED_FREE or self.board[i + k][j] == ADJACENT:
                    break
                elif self.board[i + k][j] == INTACT_DECK:
                    return False
                                
        for k in range(1, 4):
            if j - k >= 0:
                if self.board[i][j - k] == FREE or self.board[i][j - k] == ATTACKED_FREE or  self.board[i][j - k] == ADJACENT:
                    break
                elif self.board[i][j - k] == INTACT_DECK:
                    return False
                                
        for k in range(1, 4):
            if j + k <= 9:
                if self.board[i][j + k] == FREE or self.board[i][j + k] == ATTACKED_FREE or self.board[i][j + k] == ADJACENT:
                    break
                elif self.board[i][j + k] == INTACT_DECK:
                    return False
                                
        return True

    def fill_adjacent_near_destroyed_ship(self, i, j):
        """
        fills adjacent cell 
        :param i: y - coordinate of deck of destroyed ship
        :param j: x - coordinate of deck of destroyed ship
        """
        destroyed_ship = [(i, j)]

        for k in range(1, 4):            
            if i - k >= 0 and self.board[i - k][j] == ATTACKED_DECK:
                destroyed_ship.append((i - k, j))
            if j - k >= 0 and self.board[i][j - k] == ATTACKED_DECK:
                destroyed_ship.append((i, j - k))
        for k in range(1, 4):
            if i + k <= 9 and self.board[i + k][j] == ATTACKED_DECK:
                destroyed_ship.append((i + k, j))
            if j + k <= 9 and self.board[i][j + k] == ATTACKED_DECK:
                destroyed_ship.append((i, j + k))

        for n, m in destroyed_ship:
            if n != 0:
                self.board[n - 1][m] = ATTACKED_FREE
                if m != 0:
                    self.board[n - 1][m - 1] = ATTACKED_FREE
                if m != 9:
                    self.board[n - 1][m + 1] = ATTACKED_FREE
            if n != 9:
                self.board[n + 1][m] = ATTACKED_FREE
                if m != 0:
                    self.board[n + 1][m - 1] = ATTACKED_FREE   
                if m != 9:
                    self.board[n + 1][m + 1] = ATTACKED_FREE
            if m != 0:
                self.board[n][m - 1] = ATTACKED_FREE
            if m != 9:
                self.board[n][m + 1] = ATTACKED_FREE

        for n, m in destroyed_ship:
            self.board[n][m] = DEAD_SHIP

    def make_step(self, i, j):
        """
        performing move
        :param i: y - coordinate
        :param j: x - coordinate
        :raise Destroy_move: when ship was destroyed
        :raise Hit_move: when deck was hitted
        :raise Wrong_move: when this point has already attacked
        """
        if self.board[i][j] == FREE or self.board[i][j] == ADJACENT:
            self.board[i][j] = ATTACKED_FREE
        elif self.board[i][j] == INTACT_DECK:
            self.board[i][j] = ATTACKED_DECK
            if self.ship_destroyed(i, j):
                self.fill_adjacent_near_destroyed_ship(i, j)
                raise Destroy_move('You destroyed the ship!')
            raise Hit_move('You hit!')
        elif self.board[i][j] == ATTACKED_FREE or self.board[i][j] == ATTACKED_DECK or self.board[i][j] == DEAD_SHIP:
            raise Wrong_move('Error! This point has already attacked.')
        
if __name__ == '__main__':
    print('You turned on this module directly')