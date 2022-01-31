# class for basic functionality about boards
class Board:
    """
    method for generating a board
    @param width: width of board
    @param height: height of the board
    """ 
    def generateBoard(self, width, height) -> list: 
        # empty the chessboard
        board = []
        # fill the chessboard
        for i in range(height):
            board.append(["" for i in range(width)])
        return board

    """
    method for printing a board
    @param board: the board we want to print
    """
    def printBoard(self, board):
        print("*************************")
        for row in board:
            print(row)
        print("*************************")