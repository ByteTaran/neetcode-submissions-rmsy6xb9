class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            isSeen = set()
            for col in range(9):
                if board[row][col] != "." and board[row][col] in isSeen:
                    return False
                isSeen.add(board[row][col])
        
        for row in range(9):
            isSeen = set()
            for col in range(9):
                if board[col][row] != "." and board[col][row] in isSeen:
                    return False
                isSeen.add(board[col][row])
            
        
        for subBoard in range(9):
            isSeen = set()
            for i in range(3):
                for j in range(3):
                    row = i + (subBoard // 3) * 3
                    col = j + (subBoard % 3) * 3
                    if board[col][row] != "." and board[col][row] in isSeen:
                        return False
                    isSeen.add(board[col][row])
        
        return True