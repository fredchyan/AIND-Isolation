from isolation import Board
from sample_players import GreedyPlayer
from game_agent import AlphaBetaPlayer

player1 = AlphaBetaPlayer()
player2 = AlphaBetaPlayer()
game = Board(player1, player2, 9, 9)
print(game.to_string())
game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 49]
print(game.to_string())
assert(player1 == game.active_player)
print(game.get_legal_moves())
# new_game = game.forecast_move((1, 1))
# assert(new_game.to_string() != game.to_string())
# print("\nOld state:\n{}".format(game.to_string()))
# print("\nNew state:\n{}".format(new_game.to_string()))
winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
# print("Move history:\n{!s}".format(history))
