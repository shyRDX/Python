#coursera: Principles of Computing
#https://class.coursera.org/principlescomputing-001/wiki/view?page=mancala

class SolitaireMancala(object):
    def __init__(self):
        self.board = [0]

    def set_board(self, configuration):
        self.board = list(configuration)
    
    def __str__(self):
        copy_board = list(self.board)
        copy_board.reverse()
        return str(copy_board)
    
    def get_num_seeds(self, house_nun):
        return self.board[house_num]

    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        else:
            if get_num_seeds(self, house_num) == house_num:
                return True
            else:
                return False

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for i in range(0, house_num):
                self.board[house_num] -= 1
                slef.board[i] += 1

    def choose_move(self):
        for i in range(1, len(self)):
            if is_legal_move(self, i):
                return i
                break
        else:
            return 0

    def is_game_won(self):
        for i in range(1, len(self)):
            if self.board[i] != 0:
                return False
                break
        else:
            return True

    def plan_moves(self):
        current = self.board
        moves = []
        while is_game_won(current) != "True":
            if choose_move(current):
                move += choose_move(current)
                current = apply_move(current, move)
                moves.append(move)
            else:
                return False
                break
        else:
            return moves

import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())
