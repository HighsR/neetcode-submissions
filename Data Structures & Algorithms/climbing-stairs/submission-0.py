class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        A=[0]*(n+1)
        A[1]=1
        A[2]=2
        for i in range(3,n+1):
            A[i]=A[i-1] + A[i-2]
        return A[n]
        