class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])

        low = 0 
        high = n*m-1
        while low<=high:
            mid = (low + high) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value==target:
                return True
            elif mid_value<target:
                low= mid + 1
            else:
                high=mid -1

        return False
                