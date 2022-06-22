class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        ans = 0
        while (i < m and j >=0):
            
            print("val {} target {}".format(matrix[i][j],target))
            if (matrix[i][j] == target):
                ans = 1
                break
            elif (matrix[i][j] > target):
                j -= 1
            elif (matrix[i][j] < target):
                i += 1
                
        if ans == 0:
            return "false"
        else:
            return "true"
        
                
        
