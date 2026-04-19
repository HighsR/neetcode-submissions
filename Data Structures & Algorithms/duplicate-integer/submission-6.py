class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        
        count = {}
        for i,v in enumerate(nums):
            if v not in count:
                count[v]=1
            else:
                count[v]+=1

            if count[v]>1:
                return True
        return False