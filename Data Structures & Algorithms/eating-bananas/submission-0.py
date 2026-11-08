class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles) + 1
        # print(r)
        # minimum_k = r

        m = 0
        valid_k = -1
        while r > l:
            m = (r + l) // 2
            k = m
            
            hours_needed = 0
            for pile in piles:
                hours_needed += pile // k + (1 if pile % k != 0 else 0)

            if hours_needed <= h: # it is valid
                r = m
                valid_k = m
            else: # it is not valid
                l = m + 1

        return valid_k
