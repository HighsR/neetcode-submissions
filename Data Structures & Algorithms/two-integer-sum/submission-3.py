class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}
        for i,v in enumerate(nums):
            solution[target-v]=i
        
        for i,v in enumerate(nums):
            if v in solution and i != solution.get(v):
                return [i,solution.get(v)]
        return []