class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False
        low = 0
        n = len(matrix[0])-1
        high = n
        i = 0
        while i<len(matrix):    
            low = 0 
            high = n
            while low<=high:
                if matrix[i][high]<target:
                    break
                mid=(low+high)//2
                if matrix[i][mid]==target:
                    return True
                if matrix[i][mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            i+=1
        return False
                