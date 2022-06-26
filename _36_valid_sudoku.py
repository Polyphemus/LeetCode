# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        su_dicts = {}
        for i in range(9):
            su_dicts['row' + str(i)] = []
            su_dicts['column'+ str(i)] = []
        for l in range(3):
            for m in range(3):
                su_dicts['square'+ str(l) + str(m)] = []
        
        for j in range(9):
            for k in range(9):
                if board[j][k].isnumeric():
                    su_dicts['row'+str(j)].append(board[j][k])
                    su_dicts['column'+str(k)].append(board[j][k])
                    su_dicts['square'+str(j//3)+str(k//3)].append(board[j][k])           
        
        for val in su_dicts.values():
            if len(val) != len(set(val)):
                return False
        return True
