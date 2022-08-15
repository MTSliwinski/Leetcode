class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = len(matrix)-1 
        x = len(matrix[0])-1
        i = 0
        while (i<=y):
            if target <= matrix[i][x]:
                for j in matrix[i]:
                    if target == j:
                        return True
                return False
            else:
                i+=1
        return False