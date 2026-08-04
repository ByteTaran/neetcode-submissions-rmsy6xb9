class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            isSeen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in isSeen:
                    return False
                isSeen.add(board[row][col])
        
        for col in range(9):
            isSeen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in isSeen:
                    return False
                isSeen.add(board[row][col])

        for subBoard in range(9):
            isSeen = set()
            for i in range(3):
                for j in range(3):
                    row = (subBoard // 3) * 3 + i
                    col = (subBoard % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in isSeen:
                        return False
                    isSeen.add(board[row][col])
        return True
