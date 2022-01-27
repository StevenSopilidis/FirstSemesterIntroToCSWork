import random


class ChessBoard:
    __chessboard = []
    __width= 0
    __height= 0
    """
    @param width: width of the chessboard
    @param height: height of the chessboard
    """
    def __init__(self, width, height) -> None:
        self.__height = height
        self.__width = width

    # func for generating the board
    def __generateBoard(self) -> None:
        # empty the chessboard
        self.__chessboard = []
        # fill the chessboard
        for i in range(self.__height):
            self.__chessboard.append(["" for i in range(self.__width)])

    # private func to print the board in generateGames if user wants
    def __printBoard(self) -> None:
        print("*************************")
        for row in self.__chessboard:
            print(row)
        print("*************************")

    """ private func for checking who won
        returns 1 if White tower won
        or 0 of black officer won
        or -1 if none won
        @param tower_row: the row that the towes is in
        @param tower_col: the col that the tower is in
        @param officer_row: the row that the officer is in
        @param officer_col: the col that the officer is in
    """
    def __checkWhoWon(self, tower_row, tower_col, officer_row, officer_col) -> int:
        # check if the tower won
        if tower_col == officer_col or tower_row == officer_row:
            return 1
        #check if the officer won
        i = 1
        while(self.__height - i > 0 and self.__width - i > 0):
            if(officer_row - i == tower_row and officer_col - i == tower_col):
                return 0
            if(officer_row - i == tower_row and officer_col + i == tower_col):
                return 0
            if(officer_row + i == tower_row and officer_col - i == tower_col):
                return 0
            if(officer_row + i == tower_row and officer_col + i == tower_col):
                return 0
            i += 1
        # else is a draw
        return -1

    """
    func for generating the random games and 
    printing the results
    @param times: times that random game will be generated
    @param printBoard: wether user wants to see the boards that
    get generated (WT represents white tower and 
    BO represents black officer)
    """
    def generateGames(self, times, printBoard) -> None:
        times_tower_won = 0
        times_officer_won = 0
        for i in range(times):
            self.__generateBoard()
            # get random pos for both white tower and black officer
            tower_row = random.randint(0, self.__height - 1)
            tower_col = random.randint(0, self.__width - 1)
            officer_row = random.randint(0, self.__height - 1)
            officer_col = random.randint(0, self.__width - 1)
            self.__chessboard[tower_row][tower_col] = "WT"
            self.__chessboard[officer_row][officer_col] = "BO"
            if printBoard:
                self.__printBoard()
            result = self.__checkWhoWon(tower_row, tower_col, officer_row, officer_col)
            if result == 1:
                times_tower_won += 1
            if result == 0:
                times_officer_won += 1
            print(result)
        print(f"Black won: {times_officer_won} times")
        print(f"White won: {times_tower_won} times")


# first of the 8*8 chessboard
board = ChessBoard(8, 8)
board.generateGames(100, False)
# then of the 7 * 7 chessboard
board = ChessBoard(7, 7)
board.generateGames(100, False)
# and finally for the 7 * 8 
chessboardboard = ChessBoard(7, 8)
board.generateGames(100, False)