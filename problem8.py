import random
from Utils.chessboard import ChessBoard


# first of the 8*8 chessboard
board = ChessBoard(8, 8)
board.generateGamesProblem8(100, False)
# then of the 7 * 7 chessboard
board = ChessBoard(7, 7)
board.generateGamesProblem8(100, False)
# and finally for the 7 * 8 
chessboardboard = ChessBoard(7, 8)
board.generateGamesProblem8(100, True)