"""
Subtract Squares Game - Subclass of Game.
"""
from game import Game
from subtract_square_state import SubtractSquaresState


class SubtractSquaresGame(Game):
    """
    Represents a generic two-player, sequential-move, zero-sum game of
    Subtract Squares.

    Subclass of Game class.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize a new Game self, using p1_starts to find who the first
        player is.

        Overrides superclass __init__.
        """
        starting_num = int(input("Enter the starting number: "))
        self.state = SubtractSquaresState(p1_starts, starting_num)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game self.


        """
        instructions = "Starting with a non-negative whole number, each " \
                       "player takes turns choosing some square of a " \
                       "positive whole number to subtract from the value, " \
                       "provided the chosen square is not larger than the " \
                       "current value.\nThe first player to get the value " \
                       "to be 0 is the winner."

        return instructions

    def is_over(self, state: SubtractSquaresState) -> bool:
        """
        Return True if this game is over at its current game state state,
        otherwise return False.
        """
        return state.value == 0

    def is_winner(self, player: str) -> bool:
        """
        Return True if player is the winner of this game, otherwise return
        False.

        Precondition: player is 'p1' or 'p2'
        """
        if self.state.get_current_player_name() == player:
            return False

        return self.is_over(self.state)

    def str_to_move(self, string: str) -> int:
        """
        Return the move that string represents. If string is not a move,
        then return some invalid move.
        """
        if not (string.strip().isdigit()):
            return -1
        else:
            return int(string.strip())
