class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        if n==3:
            return max(nums[0],nums[1],nums[2])
        prev=max(nums[0],nums[1])
        prevprev=nums[0]
        for i in range(2,n-1):
            curr=max(prev,prevprev+nums[i])
            prevprev=prev
            prev=curr
        sum1=prev

        prev=max(nums[1],nums[2])
        prevprev=nums[1]
        for i in range(3,n):
            curr=max(prev,prevprev+nums[i])
            prevprev=prev
            prev=curr
        sum2=prev
        return max(sum1,sum2)
    