class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row and column
        subboxCnt = defaultdict(dict)
        for i in range(9):
            rowcnt = {}
            columncnt = {}
            for j in range(9):
                num = board[i][j]
                col_num = board[j][i]
                rowcnt[num] = rowcnt.get(num, 0) + 1
                columncnt[col_num] = columncnt.get(col_num, 0) + 1

                subbox_index = 0
                box_i = i // 3
                box_j = j // 3
                if box_i == 0 and box_j ==0:
                    subbox_index = 0
                elif box_i == 0 and box_j ==1:
                    subbox_index = 1
                elif box_i == 0 and box_j ==2:
                    subbox_index = 2
                elif box_i == 1 and box_j ==0:
                    subbox_index = 3
                elif box_i == 1 and box_j ==1:
                    subbox_index = 4
                elif box_i == 1 and box_j ==2:
                    subbox_index = 5 
                elif box_i == 2 and box_j ==0:
                    subbox_index = 6
                elif box_i == 2 and box_j ==1:
                    subbox_index = 7
                elif box_i == 2 and box_j ==2:
                    subbox_index = 8
                subboxCnt[subbox_index][num] = subboxCnt[subbox_index].get(num, 0) + 1
            
            # check row
            for key, val in rowcnt.items():
                if key != "." and val > 1:
                    return False
            
            # check column
            for key, val in columncnt.items():
                if key != "." and val > 1:
                    return False


        # check subbox
        for i in range(9):
            for key, val in subboxCnt[i].items():
                if key != "." and val > 1:
                    return False
        
        return True

