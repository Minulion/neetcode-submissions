class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: [] for i in range(len(board))}
        cols = {i: [] for i in range(len(board))}
        squares = {(y//3, x//3): [] for x in range(len(board)) for y in range(len(board))}
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] == '.':
                    continue
                if board[y][x] in rows[y]: 
                    return False
                else:
                    rows[y].append(board[y][x]) #append number to row
                if board[y][x] in cols[x]: 
                    return False
                else:
                    cols[x].append(board[y][x])
                if board[y][x] in squares[(y//3, x//3)]:
                    return False
                else:
                    squares[(y//3, x//3)].append(board[y][x])
        return True 
        