from asyncio.windows_events import NULL
from posixpath import split
import random
from unittest import result

from Utils.Board import Board

# chessboard class for problem 8 and 6
class ChessBoard(Board):
    __width= 0
    __height= 0
    __chessboard = []
    """
    @param width: width of the chessboard
    @param height: height of the chessboard
    """
    def __init__(self, width, height) -> None:
        self.__height = height
        self.__width = width

    """ private method for checking who won
        in problem 8
        returns 1 if White tower won
        or 0 of black officer won
        or -1 if none won
        @param tower_row: the row that the towes is in
        @param tower_col: the col that the tower is in
        @param officer_row: the row that the officer is in
        @param officer_col: the col that the officer is in
    """
    def __checkWhoWonProblem8(self, tower_row, tower_col, officer_row, officer_col) -> int:
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
    method for generating the random games for problem8 
    and printing the results
    @param times: times that random game will be generated
    @param printBoard: wether user wants to see the boards that
    get generated (WT represents white tower and 
    BO represents black officer)
    """
    def generateGamesProblem8(self, times, printBoard) -> None:
        times_tower_won = 0
        times_officer_won = 0
        for i in range(times):
            self.__chessboard = self.generateBoard(self.__width, self.__height)
            # get random pos for both white tower and black officer
            tower_row = random.randint(0, self.__height - 1)
            tower_col = random.randint(0, self.__width - 1)
            officer_row = random.randint(0, self.__height - 1)
            officer_col = random.randint(0, self.__width - 1)
            self.__chessboard[tower_row][tower_col] = "WT"
            self.__chessboard[officer_row][officer_col] = "BO"
            if printBoard:
                self.printBoard(self.__chessboard)
            result = self.__checkWhoWonProblem8(tower_row, tower_col, officer_row, officer_col)
            if result == 1:
                times_tower_won += 1
            if result == 0:
                times_officer_won += 1
            print(result)
        print(f"Black won: {times_officer_won} times")
        print(f"White won: {times_tower_won} times")


    """
    private method that returns the points for each player in problem6
    depending on which piece eats which
    @param tower_row: the row that the towes is in
    @param tower_col: the col that the tower is in
    @param officer_row: the row that the officer is in
    @param officer_col: the col that the officer is in
    @param queen_row: the row that the queen is in
    @param queen_col: the col that the queen is in
    officer and tower represent white player
    queen represents black player
    returns dict which each player points
    """
    def __getPointsProblem6(self, tower_row, tower_col, officer_row, officer_col,queen_row, queen_col) -> dict:
        white_player_points = 0
        black_player_points = 0
        # check for white player
        tower_eats_queen = False
        if tower_col == queen_col or tower_row == queen_row:
            tower_eats_queen = True
        officer_eats_queen = False
        i = 1
        while(self.__height - i > 0 and self.__width - i > 0):
            if(officer_row - i == queen_row and officer_col - i == queen_col):
                officer_eats_queen = True
            elif(officer_row - i == queen_row and officer_col + i == queen_col):
                officer_eats_queen = True
            elif(officer_row + i == queen_row and officer_col - i == queen_col):
                officer_eats_queen = True
            elif(officer_row + i == queen_row and officer_col + i == queen_col):
                officer_eats_queen = True
            i += 1

        if tower_eats_queen:
            white_player_points += 1
        if officer_eats_queen:
            white_player_points += 1
        # # check for black player
        if queen_row == tower_row or queen_col == tower_col:
            black_player_points += 1
        if queen_row == officer_row or queen_col == officer_col:
            black_player_points += 1
        i = 1
        # check diagnoly for queen
        while(self.__height - i > 0 and self.__width - i > 0):
            # for tower
            if(queen_row - i == tower_row and queen_col - i == tower_col):
                black_player_points +=1
            elif(queen_row - i == tower_row and queen_col + i == tower_col):
                black_player_points += 1
            elif(queen_row + i == tower_row and queen_col - i == tower_col):
                black_player_points +=1
            elif(queen_row + i == tower_row and queen_col + i == tower_col):
                black_player_points += 1
            #for officer 
            if(queen_row - i == officer_row and queen_col - i == officer_col):
                black_player_points +=1
            elif(queen_row - i == officer_row and queen_col + i == officer_col):
                black_player_points += 1
            elif(queen_row + i == officer_row and queen_col - i == officer_col):
                black_player_points +=1
            elif(queen_row + i == officer_row and queen_col + i == officer_col):
                black_player_points += 1
            i += 1
        return { "white_player_points": white_player_points, "black_player_points": black_player_points}
    """
    method for generating the random games for problem6 
    and printing the results
    @param printBoard: wether user wants to see the boards that
    get generated (WT represents white tower, 
    WO represents white officer, BQ represents black queen)
    """
    def generateGamesProblem6(self, printBoard) -> None:
        white_player_points = 0
        black_player_points = 0
        # generate the random 100 games for the problem6
        for i in range(100):
            self.__chessboard = self.generateBoard(8, 8)
            tower_row = random.randint(0, self.__height - 1)
            tower_col = random.randint(0, self.__width - 1)
            officer_row = random.randint(0, self.__height - 1)
            officer_col = random.randint(0, self.__width - 1)
            queen_row = random.randint(0, self.__height - 1)
            queen_col = random.randint(0, self.__width - 1)
            self.__chessboard[tower_row][tower_col] = "WT"
            self.__chessboard[officer_row][officer_col] = "WO"
            self.__chessboard[queen_row][queen_col] = "BQ"
            if printBoard:
                self.printBoard(self.__chessboard)
            # check who eats who
            results = self.__getPointsProblem6(tower_row, tower_col, officer_row, officer_col, queen_row, queen_col)
            white_player_points += results["white_player_points"]
            black_player_points += results["black_player_points"]

        print(f"White player points: {white_player_points}")
        print(f"Black player points: {black_player_points}")