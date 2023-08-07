#TEST
import copy

import pygame, sys
from chess.game.board.board import board
from chess.game.piece.piece import pawn, rook, knight, bishop, queen, king

class game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))

        color = (100, 100, 100)
        self.window.fill(color)

        #Quit Button for the game
        color = (250, 250, 250)
        pygame.draw.rect(self.window, color, [700, 50, 100, 50])
        font = pygame.font.SysFont('Corbel', 35)
        color = (0, 0, 0)
        pygame.draw.rect(self.window, color, [700, 50, 100, 50], 3)
        text = font.render("Quit", True, color)
        self.window.blit(text, (717, 57))
        pygame.display.update()

        self.pieceCodes = {
            "bpawn": 0,
            "wpawn": 1,
            "brook": 2,
            "wrook": 3,
            "bknight": 4,
            "wknight": 5,
            "bbishop": 6,
            "wbishop": 7,
            "bqueen": 8,
            "wqueen": 9,
            "bking": 10,
            "wking": 11
        }

        self.scores = {
            "bpawn": 10,
            "wpawn": 10,
            "brook": 50,
            "wrook": 50,
            "bknight": 30,
            "wknight": 30,
            "bbishop": 30,
            "wbishop": 30,
            "bqueen": 90,
            "wqueen": 90,
            "bking": 900,
            "wking": 900
        }

        self.running = True

        self.sprites = list()
        self.initSprites(self.sprites)

        self.game = board()

        self.available = False
        self.availables = list()
        self.selectedPiece = None
        self.turn = 0 #1 --> Black, 0 --> White
        self.draw = False
        self.checkB = False
        self.checkW = False

        self.notChoose = True
        self.pawnToConvert = None

        self.refreshBoard()
        self.start()

    def start(self):
        while (self.running):
            self.gameloop()

    def gameloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posX = pos[0]
                posY = pos[1]

                if posX <= 800 and posX >= 700 and posY <= 100 and posY >= 50:
                    self.running = False
                    sys.exit()

                elif posX <= 650 and posX >= 50 and posY <= 650 and posY >= 50 and self.notChoose:
                    square = self.reConvertCoordinate(posX, posY)

                    if self.available and [square[0], square[1]] in self.availables:

                        if self.game.currboard[square[0]][square[1]] != None:
                            self.game.currboard[square[0]][square[1]].available = False

                        temp = [self.selectedPiece.x, self.selectedPiece.y]

                        self.game.currboard[square[0]][square[1]] = self.selectedPiece
                        self.game.currboard[square[0]][square[1]].x = square[0]
                        self.game.currboard[square[0]][square[1]].y = square[1]
                        self.game.currboard[temp[0]][temp[1]] = None

                        if (self.selectedPiece.name == "bpawn" or self.selectedPiece.name == "wpawn"):
                            self.selectedPiece.notMoved = False

                        self.refreshBoard()
                        self.available = False
                        if self.turn == 0:
                            self.turn = 1
                        else:
                            self.turn = 0


                        if self.selectedPiece.name == "bpawn" and square[1] == 0:
                            self.pawnToConvert = self.selectedPiece
                            self.askForConversion(1)

                        if self.selectedPiece.name == "wpawn" and square[1] == 7:
                            self.pawnToConvert = self.selectedPiece
                            self.askForConversion(0)


                        self.checkChecks()
                        condition = self.checkGameConditions()

                        if condition != -1:
                            for i in range(8):
                                for j in range(8):
                                    self.game.currboard[i][j] = None
                            self.refreshBoard()
                    else:
                        if self.game.currboard[square[0]][square[1]] != None and self.game.currboard[square[0]][square[1]].side == self.turn:

                            if self.turn == 0:
                                king = self.game.whitePieces[7]
                            else:
                                king = self.game.blackPieces[7]

                            self.selectedPiece = self.game.currboard[square[0]][square[1]]
                            if self.selectedPiece.name == "bking" or self.selectedPiece.name == "wking":
                                self.availables = self.selectedPiece.availableSquares(self.game.currboard, self.game.pieces)
                            else:
                                self.availables = self.selectedPiece.availableSquares(self.game.currboard, self.game.pieces, king)

                            self.refreshBoard()
                            for pos in self.availables:
                                posRelScreen = self.coordinateConverter(pos[0], pos[1])
                                pygame.draw.circle(self.window, (250, 0, 0), (posRelScreen[0]+37, posRelScreen[1]+37), 5)
                                pygame.display.update()
                            self.available = True
                elif not self.notChoose:
                    tempX = self.pawnToConvert.x
                    tempY = self.pawnToConvert.y
                    tempSide = self.pawnToConvert.side

                    if posX >= 700 and posX < 775 and posY >= 150 and posY < 225:
                        self.game.pieces.remove(self.game.currboard[tempX][tempY])
                        self.game.currboard[tempX][tempY] = knight(tempSide, tempX, tempY)
                        self.game.pieces.append(self.game.currboard[tempX][tempY])
                        self.notChoose = True
                        self.refreshBoard()
                        pygame.display.update()

                    elif posX >= 775 and posX < 850 and posY >= 150 and posY < 225:
                        self.game.pieces.remove(self.game.currboard[tempX][tempY])
                        self.game.currboard[tempX][tempY] = queen(tempSide, tempX, tempY)
                        self.game.pieces.append(self.game.currboard[tempX][tempY])
                        self.notChoose = True
                        self.refreshBoard()
                        pygame.display.update()

                    elif posX >= 700 and posX < 775 and posY >= 225 and posY < 300:
                        self.game.pieces.remove(self.game.currboard[tempX][tempY])
                        self.game.currboard[tempX][tempY] = rook(tempSide, tempX, tempY)
                        self.game.pieces.append(self.game.currboard[tempX][tempY])
                        self.notChoose = True
                        self.refreshBoard()
                        pygame.display.update()

                    elif posX >= 775 and posX < 850 and posY >= 225 and posY < 300:
                        self.game.pieces.remove(self.game.currboard[tempX][tempY])
                        self.game.currboard[tempX][tempY] = bishop(tempSide, tempX, tempY)
                        self.game.pieces.append(self.game.currboard[tempX][tempY])
                        self.notChoose = True
                        self.refreshBoard()
                        pygame.display.update()

                    else:
                        pass


    def display(self, img, x, y ):
        self.window.blit(img, (x, y))

    def coordinateConverter(self, x, y):
        newX = 50 + (75 * x)
        newY = 50 + (75 * y)

        newCoordinate = (newX, newY)
        return newCoordinate

    def reConvertCoordinate(self, x, y):
        reX = x - 50
        reY = y - 50

        retX = int(reX / 75)
        retY = int(reY / 75)

        return (retX, retY)

    def initSprites(self, sprites):
        Default_Image_size = (75, 75)

        bp = pygame.image.load('./sprites/pawn_black.png')
        bp = pygame.transform.scale(bp, Default_Image_size)
        sprites.append(bp)

        wp = pygame.image.load('./sprites/pawn_white.png')
        wp = pygame.transform.scale(wp, Default_Image_size)
        sprites.append(wp)

        br = pygame.image.load('./sprites/rook_black.png')
        br = pygame.transform.scale(br, Default_Image_size)
        sprites.append(br)

        wr = pygame.image.load('./sprites/rook_white.png')
        wr = pygame.transform.scale(wr, Default_Image_size)
        sprites.append(wr)

        bk = pygame.image.load('./sprites/knight_black.png')
        bk = pygame.transform.scale(bk, Default_Image_size)
        sprites.append(bk)

        wk = pygame.image.load('./sprites/knight_white.png')
        wk = pygame.transform.scale(wk, Default_Image_size)
        sprites.append(wk)

        bb = pygame.image.load('./sprites/bishop_black.png')
        bb = pygame.transform.scale(bb, Default_Image_size)
        sprites.append(bb)

        wb = pygame.image.load('./sprites/bishop_white.png')
        wb = pygame.transform.scale(wb, Default_Image_size)
        sprites.append(wb)

        bq = pygame.image.load('./sprites/queen_black.png')
        bq = pygame.transform.scale(bq, Default_Image_size)
        sprites.append(bq)

        wq = pygame.image.load('./sprites/queen_white.png')
        wq = pygame.transform.scale(wq, Default_Image_size)
        sprites.append(wq)

        bK = pygame.image.load('./sprites/king_black.png')
        bK = pygame.transform.scale(bK, Default_Image_size)
        sprites.append(bK)

        wK = pygame.image.load('./sprites/king_white.png')
        wK = pygame.transform.scale(wK, Default_Image_size)
        sprites.append(wK)

    def refreshBoard(self):
        color = (100, 100, 100)

        pygame.draw.rect(self.window, color, [0, 0, 650, 650])
        pygame.draw.rect(self.window, color, [700, 150, 150, 150])

        color = (108, 168, 124)
        for i in range(0, 300, 75):
            for j in range(0, 300, 75):
                pygame.draw.rect(self.window, color, [50 + (2 * i), 50 + (2 * j), 75, 75])

        for i in range(0, 300, 75):
            for j in range(0, 300, 75):
                pygame.draw.rect(self.window, color, [125 + (2 * i), 125 + (2 * j), 75, 75])

        color = (0, 0, 0)
        pygame.draw.rect(self.window, color, [50, 50, 600, 600], 3)

        for i in range(8):
            for j in range(8):
                curr = self.game.currboard[i][j]
                coordinate = self.coordinateConverter(i, j)
                if curr == None:
                    continue
                else:
                    img = self.sprites[self.pieceCodes[curr.name]]
                    self.display(img, coordinate[0], coordinate[1])

        pygame.display.update()

    def noOfAvailableMoves(self, turn):
        count = 0
        if turn == 1:
            for piece in self.game.blackPieces:
                if piece.available:
                    if piece.name != "wking" and piece.name != "bking":
                        count += len(piece.availableSquares(self.game.currboard, self.game.pieces, self.game.blackPieces[7]))
                    else:
                        count += len(piece.availableSquares(self.game.currboard, self.game.pieces))
        else:
            for piece in self.game.whitePieces:
                if piece.available:
                    if piece.name != "wking" and piece.name != "bking":
                        count += len(piece.availableSquares(self.game.currboard, self.game.pieces, self.game.whitePieces[7]))
                    else:
                        count += len(piece.availableSquares(self.game.currboard, self.game.pieces))
        return count

    def checkGameConditions(self):
        if self.noOfAvailableMoves(1) == 0 and self.checkB:
            return 0 #-->White Wins
        elif self.noOfAvailableMoves(0) == 0 and self.checkW:
            return 1 #-->Black Wins
        elif (self.noOfAvailableMoves(0) == 0 and not self.checkW) or (self.noOfAvailableMoves(0) == 0 and not self.checkB):
            return 2 #-->Draw
        else:
            return -1 #-->Continues

    def checkChecks(self):
        bk = self.game.blackPieces[7]
        wk = self.game.whitePieces[7]

        if bk.canBeEaten(bk.x, bk.y, self.game.currboard, self.game.pieces):
            self.checkB = True
            print("CheckB")
        else:
            self.checkB = False
            print("!CheckB")

        if wk.canBeEaten(wk.x, wk.y, self.game.currboard, self.game.pieces):
            self.checkW = True
            print("CheckW")
        else:
            self.checkW = False
            print("!CheckW")

    def askForConversion(self, side):
        color = (0, 0, 0)

        pygame.draw.rect(self.window, color, [700, 150, 75, 75], 2)
        pygame.draw.rect(self.window, color, [775, 150, 75, 75], 2)
        pygame.draw.rect(self.window, color, [700, 225, 75, 75], 2)
        pygame.draw.rect(self.window, color, [775, 225, 75, 75], 2)

        if side == 1:
            knight = "bknight"
            queen = "bqueen"
            rook = "brook"
            bishop = "bbishop"
        else:
            knight = "wknight"
            queen = "wqueen"
            rook = "wrook"
            bishop = "wbishop"

        #Knight
        img = self.sprites[self.pieceCodes[knight]]
        self.display(img, 700, 150)
        #Queen
        img = self.sprites[self.pieceCodes[queen]]
        self.display(img, 775, 150)
        #Rook
        img = self.sprites[self.pieceCodes[rook]]
        self.display(img, 700, 225)
        #Bishop
        img = self.sprites[self.pieceCodes[bishop]]
        self.display(img, 775, 225)

        pygame.display.update()

        self.notChoose = False