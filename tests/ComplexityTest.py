import random

from game.Board import Board


class ComplexityTest:
    def __init__(self, testCases):
        self.__testCases = testCases
        self.boardWidth = 5
        self.boardHeight = 5

    def run(self):
        print("Running test on " + str(self.__testCases) + " test cases.")
        valid = 0
        for i in range(self.__testCases):
            randomBoard = self.createRandomBoardState()
            valid += 1 if self.validateBoardState(randomBoard) else 0

        print("Valid: " + str(valid) + " out of: " + str(self.__testCases))

    def createRandomBoardState(self):
        board = Board(self.boardWidth, self.boardHeight)
        board.clearBoard()
        emptyElementsCount = (self.boardWidth * self.boardHeight) - (2 * self.boardWidth)

        # Add empty elements.
        availableElements = [board.emptyField for i in range(emptyElementsCount)]
        # Add white pawn elements.
        availableElements.extend(board.whitePawn for i in range(self.boardWidth - 1))
        # Add black pawn elements.
        availableElements.extend(board.blackPawn for i in range(self.boardWidth - 1))
        # Add kings elements.
        availableElements.extend([board.blackKing, board.whiteKing])

        # Insert one element foreach field on the board.
        for y in range(board.boardHeight):
            for x in range(board.boardWidth):
                elementsLen = len(availableElements)
                if elementsLen == 1:
                    board.setFieldValue(x, y, availableElements.pop())
                else:
                    drawIndex = random.randrange(-1, elementsLen - 1)
                    board.setFieldValue(x, y, availableElements.pop(drawIndex))

        return board

    @staticmethod
    def validateBoardState(board):
        # Rules:
        # 1. Only the king can stand in the middle of the board.
        kingsValley = board.getKingsValleyField()
        kingsValleyVal = board.getFieldValue(kingsValley["x"], kingsValley["y"])

        return kingsValleyVal != board.blackPawn and kingsValleyVal != board.whitePawn