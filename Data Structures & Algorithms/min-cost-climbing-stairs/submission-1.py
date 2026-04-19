class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        count={}
        count[0]=cost[0]
        count[1]=cost[1]
        n=len(cost)
        for i in range(2,n):
            count[i]=min(count[i-1],count[i-2])+cost[i]
        print(count)
        return min(count[n-1],count[n-2])

