class Solution:
    def __init__(self):
        self.min_cost_table = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # target floor: len(cost)
        
        # i + 1 cost?  = cost[i]
        # i + 2 cost?  = min(cost[i] , cost[i] + cost[i+1])
        # i + 3 cost?
        #   either {i+2 cost + cost[i+2]} 
        #   or {i+1 cost + cost[i+1]}
        # i + 4 cost?
        #   either {i+3 cost + cost[i+3]} // single jump
        #   or {i+2 cost + cost[i+2]}  // double jump
        # ...
        # 0 + len(cost)?
        #   either {len(cost)-1 cost + cost[-1]} // single jump
        #   or {len(cost)-2 cost + cost[-2]}  // double jump

        # base case
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])

        cached_min_cost_single = self.min_cost_table.get(len(cost)-1, -1)
        cached_min_cost_double = self.min_cost_table.get(len(cost)-2, -1)

        singleJumpCost = cost[-1] + self.minCostClimbingStairs(cost[:-1]) if (cached_min_cost_single == -1) else cost[-1] + cached_min_cost_single
        doubleJumpCost = cost[-2] + self.minCostClimbingStairs(cost[:-2]) if (cached_min_cost_double == -1) else cost[-2] + cached_min_cost_double

        self.min_cost_table[len(cost)] = min(singleJumpCost, doubleJumpCost)
        return self.min_cost_table[len(cost)]