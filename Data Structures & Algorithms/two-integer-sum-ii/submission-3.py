class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None:
            return []
        i=0
        j=len(numbers)-1

        while i<j:
            curr=numbers[i]+numbers[j]
            if curr == target:
                return [i+1,j+1]
            elif curr<target:
                i+=1
            else:
                j-=1
        return []