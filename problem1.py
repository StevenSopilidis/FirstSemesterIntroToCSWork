import random

from Utils.Board import Board

# class for problem1 game
class Game(Board):
    __board = []
    # width and height of board
    __boardHeight = 3
    __boardWidth = 3

    """
    private method for randomly getting a ring
    @param big_left: ammount of big rings left
    @param medium_left: ammount of medium rings left
    @param small_left: ammount of small rings left
    """
    def __getRandomRing(self, big_left, medium_left, small_left) -> None:
        got_ring = False
        ring = 0
        while got_ring == False:
            # 1 -> big ring, 2 -> medium, 3 -> small
            ring = random.randint(1, 3)
            match ring:
                case 1:
                    if(big_left > 0):
                        got_ring = True
                        break
                case 2:
                    if(medium_left > 0):
                        got_ring = True
                        break
                case 3:
                    if(small_left > 0):
                        got_ring = True
                        break
        # get the chars that represent the ring and put them into
        # the board
        chars = ""
        match ring:
            case 1:
                chars = "BR"
            case 2:
                chars = "MR"
            case 3:
                chars = "SR"
        return chars

    """
    private method for putting a ring into the board
    @param ring: the ring that we need to put into the board
    """
    def __putRingIntoBoard(self, ring):
        while True:
            row = random.randint(0, self.__boardWidth - 1)
            col = random.randint(0, self.__boardHeight - 1)
            if ring not in self.__board[row][col]:
                self.__board[row][col] += ring
                return

    """
    @param ring: ring that we are checking for
    returns true if three same rings are on the same row 
    """ 
    def __checkHorizontallyForSame(self, ring) -> bool:
        if ring in self.__board[0][0] and ring in self.__board[0][1] and ring in self.__board[0][2]:
            return True
        elif ring in self.__board[1][0] and ring in self.__board[1][1] and ring in self.__board[1][2]:
            return True
        elif ring in self.__board[2][0] and ring in self.__board[2][1] and ring in self.__board[2][2]:
            return True
        return False
    
    """
    @param ring: ring that we are checking for
    returns true if three same rings are on the same col 
    """
    def __checkVerticallyForSame(self, ring) -> bool:
        if ring in self.__board[0][0] and ring in self.__board[1][0] and ring in self.__board[2][0]:
            return True
        elif ring in self.__board[0][1] and ring in self.__board[1][1] and ring in self.__board[2][1]:
            return True
        elif ring in self.__board[0][2] and ring in self.__board[1][2] and ring in self.__board[2][2]:
            return True
        return False     
    
    """
    @param ring: ring that we are checking for
    returns true if three same rings are on the same diagnol 
    """
    def __checkDiagnollyForSame(self, ring):
        if ring in self.__board[0][0] and ring in self.__board[1][1] and ring in self.__board[2][2]:
            return True
        elif ring in self.__board[0][2] and ring in self.__board[1][1] and ring in self.__board[2][0]:
            return True
        return False

    """
    returns true if rings are in an ascending order on the same row
    """
    def __checkHorizontallyForDiffrent(self):
        if "SR" in self.__board[0][0] and "MR" in self.__board[0][1] and "BR" in self.__board[0][2]:
            return True
        elif "SR" in self.__board[1][0] and "MR" in self.__board[1][1] and "BR" in self.__board[1][2]:
            return True
        elif "SR" in self.__board[2][0] and "MR" in self.__board[2][1] and "BR" in self.__board[2][2]:
            return True
        return False
    
    """
    returns true if rings are in an ascending order diagnolly
    """
    def __checkDiagnollyForDiffrent(self):
        if "BR" in self.__board[0][0] and "MR" in self.__board[1][1] and "SR" in self.__board[2][2]:
            return True
        elif "SR" in self.__board[0][2] and "MR" in self.__board[1][1] and "BR" in self.__board[2][0]:
            return True
        return False


    """
    returns true if rings are in an ascending order on the same col
    """
    def __checkVerticallyForDiffrent(self):
        if "BR" in self.__board[0][0] and "MR" in self.__board[1][0] and "SR" in self.__board[2][0]:
            return True
        elif "BR" in self.__board[0][1] and "MR" in self.__board[1][1] and "SR" in self.__board[2][1]:
            return True
        elif "BR" in self.__board[0][2] and "MR" in self.__board[1][2] and "SR" in self.__board[2][2]:
            return True
        return False

    """
    private method for checking if game finished
    it returns a Boolean indicating wether the game has finished
    """
    def __gameFinished(self):
        if self.__checkHorizontallyForSame("SR") or self.__checkVerticallyForSame("SR") or self.__checkDiagnollyForSame("SR"):
            return True
        elif self.__checkHorizontallyForSame("MR") or self.__checkVerticallyForSame("MR") or self.__checkDiagnollyForSame("MR"):
            return True
        elif self.__checkHorizontallyForSame("BR") or self.__checkVerticallyForSame("BR") or self.__checkDiagnollyForSame("BR"):
            return True
        elif self.__checkHorizontallyForDiffrent() or self.__checkVerticallyForDiffrent() or self.__checkDiagnollyForDiffrent():
            return True
        return False

    """
    method for generating the games and returning the
    avarage steps it took for the game to finish
    @param times: How many games to generate
    @param printBoard: If user wants the boards to be printed 
    BR represents big ring
    MR represents medium ring
    SR represents small ring
    """
    def generateGames(self, times, printBoard) -> int:
        total_steps = 0
        # play the game randomly
        ammount_of_big_rings_left = 9
        ammount_of_medium_rings_left = 9
        ammount_of_small_rings_left = 9
        for i in range(times):
            self.__board = self.generateBoard(self.__boardWidth, self.__boardHeight)
            # while game not finished get a ring and put it into board
            finished = False
            steps = 0
            while finished == False:
                steps += 1
                ring = self.__getRandomRing(ammount_of_big_rings_left, ammount_of_medium_rings_left, ammount_of_small_rings_left)
                self.__putRingIntoBoard(ring)

                finished = self.__gameFinished()
            total_steps += steps
            # print the board if user wants to
            if printBoard:
                self.printBoard(self.__board)
            
            print(f"Game {i} took: {steps} steps")
        return total_steps / times


game = Game()
average_steps = game.generateGames(100, True)
print(f"The games took an average of {average_steps} steps")