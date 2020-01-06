"""
Superclass Game
"""
from typing import Any
from game_state import GameState


class Game:
    """
    Represents a generic two-player, sequential-move, zero-sum game.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize a new Game self, using p1_starts to find who the first
        player is.
        """
        raise NotImplementedError

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game self.
        """
        raise NotImplementedError

    def is_over(self, state: GameState) -> bool:
        """
        Return True if this game is over at its current game state state,
        otherwise return False.
        """
        raise NotImplementedError

    def is_winner(self, player: str) -> bool:
        """
        Return True if player is the winner of this game, otherwise return
        False.

        Precondition: player is 'p1' or 'p2'
        """
        raise NotImplementedError

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        then return some invalid move.
        """
        raise NotImplementedError
