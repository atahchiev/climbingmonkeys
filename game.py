from constants import *
import probabilities

DEFAULT_BOARD = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
            7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

my_ropes = DEFAULT_BOARD
its_ropes = DEFAULT_BOARD

finished_ropes = {}


class Board:

    def __init__(self, board=DEFAULT_BOARD  ):
        self.board = board

    def sum_evaluation(player_ropes):
        S = 0
        for i in player_ropes:
            S += player_ropes[i] * coef(i)
        return S

    def evaluate(rope, n):
        return player_ropes[n] * coef(i)

    def best_n_ropes(player_ropes, n):
        sorted_x = sorted(
            player_ropes.items(), key=operator.itemgetter(1), reverse=True)
        return dict(sorted_x[:n])

    def ropes_behind(my_ropes, opponent_ropes):
        S = 0
        for i in my_ropes:
            if my_ropes[i] < opponent_ropes[i]:
                S += 1
            elif my_ropes[i] < opponent_ropes[i]:
                S -= 1
        return S

    def get_ropes_behind(my_ropes, opponent_ropes):
        ropes = []

        for i in my_ropes:
            if my_ropes[i] < opponent_ropes[i]:
                ropes.append(i)
            elif my_ropes[i] < opponent_ropes[i]:
                S -= 1
        return ropes

    def is_n_rope_climbed(board, n):
        return board[n]*coef(n)/2 == n*(14/(7 - abs(n - 7)))

    def is_game_done(player_ropes):

        first_3 = best_n_ropes(board, 3)


class Player(Board):

    def __init__(self, board=DEFAULT_BOARD, turn=None):
        super().__init__(board)
        self.turn = turn

    def __not__(self):
        self.turn = not self.turn
        print(self.turn)
        return self

player1 = Player(DEFAULT_BOARD, True)
player2 = Player(DEFAULT_BOARD, False)
player1 = not player1
# print(player1.turn)
b = Board()
# print(b.board)
