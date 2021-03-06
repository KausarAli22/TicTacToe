from player import ComputerPlayer, HumanPlayer
import math as m
import time as t
import sys


class TicTacToe(object):
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner=None

    def empty_square(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')         

    def moves_available(self):
        return[i for i, x in enumerate(self.board)if x == ' ']    

    def show_current_board_state(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')        

    def move(self,square,player_letter):
        if self.board[square] == ' ':
            self.board[square]=player_letter

            if self.is_winner(square,player_letter):
                self.current_winner=player_letter
            return True
            

        return False

    def is_winner(self,square,player_letter):
        row_idx=m.floor(square/3)
        row=self.board[row_idx*3 : (row_idx + 1)*3]
        if all([s == player_letter for s in row]):
            return True
        col_idx=square%3
        col=[self.board[col_idx + i*3] for i in range(3)] 
        if all([s == player_letter for s in col]):  
            return True

        if square % 2 == 0:
            left_diagonal=[self.board[i] for i in [0,4,8]]
            if all([s==player_letter for s in left_diagonal]):
                return True

            right_diagonal=[self.board[i] for i in [2,4,6]]  
            if all([s==player_letter for s in left_diagonal]):
                return True

        return False                       

def play(game_instance,x_player,o_player,start_from='X', speed=0.8):
    game_instance.show_current_board_state()
    player_letter=start_from

    while game_instance.empty_square():
        if player_letter == 'O':
            square = o_player.move()
        else:
            square = x_player.move()    

        if game_instance.move(square,player_letter):
            print(f'{player_letter} made a move to {square + 1}')
            game_instance.show_current_board_state()

            if game_instance.current_winner:
                print(f'{player_letter} has won the game, Hurray!')
                sys.exit(0)

        player_letter='O' if player_letter == 'X' else 'X'
        t.sleep(speed)       
    print("It's draw")
    sys.exit(0)

if __name__ == '__main__':
    g=TicTacToe()    
    x_player=HumanPlayer('X',g)
    o_player=ComputerPlayer('O',g)
    play(g,x_player,o_player)
