class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return False
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            print(f"low:{low}")
            print(f"high:{high}")
            if low==high:
                return nums[low]
            if nums[mid]<nums[high]:
                high=mid
            else:
                low=mid+1
        return -1
        