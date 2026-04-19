class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        count={}
        prevprev=cost[0]
        prev=cost[1]
        n=len(cost)
        for i in range(2,n):
            curr=min(prev,prevprev)+cost[i]
            prevprev=prev
            prev=curr
            print(curr)

        
        return min(prev,prevprev)

