class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevprev=cost[0]
        prev=cost[1]
        n=len(cost)
        for i in range(2,n):
            curr=min(prev,prevprev)+cost[i]
            prevprev=prev
            prev=curr
        return min(prev,prevprev)

