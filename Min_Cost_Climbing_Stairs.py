#This is a aplication of fibonacci series
class Solution:
    def minCostClimbingStairs( cost: list[int]) -> int:
        a=cost[0]
        b=cost[1]
        res=0
        if len(cost)>2:
            for i in range(2,len(cost)):
                res=min(cost[i]+a,cost[i]+b)
                a=b
                b=res
        return min(a,b)
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(minCostClimbingStairs(cost))


# Runtime: 72 ms, faster than 79.05% 
# Memory Usage: 13.9 MB, less than 74.19%