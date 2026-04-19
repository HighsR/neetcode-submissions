class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None:
            return []
        count = {}

        for i,v in enumerate(nums):
            if v not in count:
                count[v]=1;
            else:
                count[v]+=1;
        result =[]
        while k>0:
            max_val_key=max(count,key=count.get)
            result.append(max_val_key)
            del count[max_val_key]
            k-=1
        return result