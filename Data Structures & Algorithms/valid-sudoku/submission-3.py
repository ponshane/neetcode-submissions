class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i: set() for i in range(9)}
        col_map = {j: set() for j in range(9)}
        answer_map = {}
        for i in range(9):
            answer_map[i] = {}
            for j in range(9):
                answer_map[i][j] = set()

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                
                if val == ".":
                    continue
                
                if val in answer_map[row // 3][col // 3] or val in row_map[row] or val in col_map[col]:
                    return False
                
                row_map[row].add(val)
                col_map[col].add(val)
                answer_map[row // 3][col // 3].add(val)
        
        return True

                
                