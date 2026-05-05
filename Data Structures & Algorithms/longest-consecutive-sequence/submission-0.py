class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sol={}
        for i,v in enumerate(nums):
            sol[v]=0
        print(sol)
        longest=0
        for key in sol:
            if key-1 not in sol:
                curr=key
                curr_count=1
                
                while curr+1 in sol:
                    curr+=1
                    curr_count+=1
            
                longest=max(curr_count,longest)
        return longest