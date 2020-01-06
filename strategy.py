"""
A module for strategies.
"""
from typing import Any, Union
from game import Game
from random import *
from game_state import GameState


def interactive_strategy(game: Game) -> Union[str, int]:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Game) -> Union[str, int]:
    """
    Return a random, valid move for game.
    """
    possible_moves = game.state.get_possible_moves()
    random_index = random.randint(0, possible_moves.length - 1)

    return possible_moves[random_index]


def recursive_minimax_strategy(game: Game) -> Any:
    """
    Return a move that produces the "highest guaranteed score" for the current
    player in game.

    Recursive implementation of the MINIMAX decision rule.
    """
    current_state = game.state
    possible_moves = game.state.get_possible_moves()
    moves = {}

    for move in possible_moves:
        next_state = game.state.make_move(move)
        current_player = game.state.get_current_player_name()
        opponent_player = "p1" if current_player == "p2" else "p2"

        if game.is_over(next_state):
            if game.is_winner(current_player):  # Move results in curr. win
                moves[move] = 1
            elif game.is_winner(opponent_player):  # Move results in opp. win
                moves[move] = -1
            else:  # Move results in a draw
                moves[move] = 0

        else:  # Game hasn't ended, continue looking for final outcome
            game.state = next_state
            # Multiply by -1, since opponent's outcome is opposite from curr's
            moves[move] = -1 * recursive_helper(game)

    # Return a move that results in the best possible outcome
    game.state = current_state
    draw_move = None
    for move in moves:
        if moves[move] == 1:  # Win move that results in possible win
            return move
        elif moves[move] == 0:
            draw_move = move

    # If no possibility to win or draw, return the first possible move
    return possible_moves[0] if draw_move is None else draw_move


def recursive_helper(game: Game) -> int:
    """
    Returns an integer representing the score for the state of this game
    for the current player of this game.

    Returns 1 if the state results in the current player's win, -1 if the
    state results in the opposing player's win, and 0 in the case of a draw.
    """
    current_state = game.state
    current_player = game.state.get_current_player_name()
    opponent_player = "p1" if current_player == "p2" else "p2"

    scores = []
    if game.is_over(current_state):
        if game.is_winner(current_player):  # Move results in curr. win
            return 1
        elif game.is_winner(opponent_player):  # Move results in opp. win
            return -1
        else:  # Move results in a draw
            return 0
    else:
        for move in game.state.get_possible_moves():
            game.state = game.state.make_move(move)
            scores.append(-1 * recursive_helper(game))

    game.state = current_state
    return max(scores)
