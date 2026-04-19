class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        
        prefix_product = {}
        product=1
        for i,v in enumerate(nums):
            prefix_product[i]=product
            product*=v

        suffix_product = {}
        product=1
        n = len(nums)
        for i in range(n - 1, -1, -1):
            suffix_product[i]=product
            product*=nums[i]

        result = []
        for i in range(n):
            result.append(prefix_product[i] * suffix_product[i])
        return result