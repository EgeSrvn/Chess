from chess.game.piece.piece import pawn,rook,knight,bishop,queen,king

class board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.currboard = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.pieces = list()
        self.blackPieces = list() #[7] --> King
        self.whitePieces = list() #[7] --> King
        self.initialize(self.pieces,self.blackPieces,self.whitePieces)

        
    
    def initialize(self, pieces, blackPieces, whitePieces):
        self.currboard[0][7] = rook(1, 0, 7)
        pieces.append(self.currboard[0][7])
        blackPieces.append(self.currboard[0][7])
        
        self.currboard[7][7] = rook(1, 7, 7)
        pieces.append(self.currboard[7][7])
        blackPieces.append(self.currboard[7][7])
        
        self.currboard[1][7] = knight(1, 1, 7)
        pieces.append(self.currboard[1][7])
        blackPieces.append(self.currboard[1][7])
        
        self.currboard[6][7] = knight(1, 6, 7)
        pieces.append(self.currboard[6][7])
        blackPieces.append(self.currboard[6][7])
        
        self.currboard[2][7] = bishop(1, 2, 7)
        pieces.append(self.currboard[2][7])
        blackPieces.append(self.currboard[2][7])
        
        self.currboard[5][7] = bishop(1, 5, 7)
        pieces.append(self.currboard[5][7])
        blackPieces.append(self.currboard[5][7])
        
        self.currboard[3][7] = queen(1, 3, 7)
        pieces.append(self.currboard[3][7])
        blackPieces.append(self.currboard[3][7])
        
        self.currboard[4][7] = king(1, 4, 7)
        pieces.append(self.currboard[4][7])
        blackPieces.append(self.currboard[4][7])


        
        self.currboard[0][0] = rook(0, 0, 0)
        pieces.append(self.currboard[0][0])
        whitePieces.append(self.currboard[0][0])
        
        self.currboard[7][0] = rook(0, 7, 0)
        pieces.append(self.currboard[7][0])
        whitePieces.append(self.currboard[7][0])
        
        self.currboard[1][0] = knight(0, 1, 0)
        pieces.append(self.currboard[1][0])
        whitePieces.append(self.currboard[1][0])
        
        self.currboard[6][0] = knight(0, 6, 0)
        pieces.append(self.currboard[6][0])
        whitePieces.append(self.currboard[6][0])
        
        self.currboard[2][0] = bishop(0, 2, 0)
        pieces.append(self.currboard[2][0])
        whitePieces.append(self.currboard[2][0])
        
        self.currboard[5][0] = bishop(0, 5, 0)
        pieces.append(self.currboard[5][0])
        whitePieces.append(self.currboard[5][0])
        
        self.currboard[3][0] = queen(0, 3, 0)
        pieces.append(self.currboard[3][0])
        whitePieces.append(self.currboard[3][0])
        
        self.currboard[4][0] = king(0, 4, 0)
        pieces.append(self.currboard[4][0])
        whitePieces.append(self.currboard[4][0])
        
        for i in range(8):
            self.currboard[i][6] = pawn(1, i, 6)
            self.currboard[i][1] = pawn(0, i, 1)
            
            pieces.append(self.currboard[i][6])
            pieces.append(self.currboard[i][1])

            blackPieces.append(self.currboard[i][6])
            whitePieces.append(self.currboard[i][1])
            
        for i in range(2, 6):
            for j in range(8):
                self.currboard[j][i] = None


