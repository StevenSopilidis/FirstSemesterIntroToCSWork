import random

from Utils.Board import Board

# class for problem1 game
class Game(Board):
    __board = []
    """
    method for generating the games and returning the
    avarage steps it took for the game to finish
    @param times: How many games to generate
    @param printBoard: If user wants the boards to be printed 
    """