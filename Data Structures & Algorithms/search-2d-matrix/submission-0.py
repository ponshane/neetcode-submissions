class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        m_l = 0
        m_r = m

        while m_l <= m_r:

            m_m = m_l + (m_r-m_l) // 2

            if matrix[m_m][0] <= target <= matrix[m_m][n]:
                # do 1D search
                l = 0
                r = n

                while l <= r:
                    m = l + (r-l)//2
                    
                    if matrix[m_m][m] == target:
                        return True
                    
                    if matrix[m_m][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                
                return False

            elif matrix[m_m][0] < target:
                m_l = m_m + 1
            else:
                m_r = m_m - 1 
                
        return False