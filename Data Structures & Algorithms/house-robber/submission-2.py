class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        prev=max(nums[0],nums[1])
        prevprev=nums[0]
        for i in range(2,n):
            print(f"prev:{prev}")
            print(f"prevprev:{prevprev}")
            curr=max(prev,prevprev+nums[i])
            prevprev=prev
            prev=curr
            print(f"curr:{curr}")
        return max(prev,curr)
