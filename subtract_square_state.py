"""
Subtract Squares Game State - Subclass of GameState
"""
from typing import Any
from game_state import GameState


class SubtractSquaresState(GameState):
    """
    The state of a two-player, sequential-move, zero-sum game of Subtract
    Squares at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, starting_num: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        Extends superclass __init__
        """
        super().__init__(is_p1_turn)
        self.value = starting_num

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return "Current Total: {0}".format(self.value)

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        possible_moves = []

        for i in range(1, self.value + 1):
            if i ** 2 <= self.value:
                possible_moves.append(i ** 2)

        return possible_moves

    def make_move(self, move: Any) -> 'SubtractSquaresState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        return SubtractSquaresState(not self.is_p1_turn, self.value - int(move))

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - Total: {}".format(self.is_p1_turn,
                                                  self.value)

