class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case
        if len(s) < 2:
            return len(s)

        longest = 1
        letters = set() # hashset


        left = 0
        right = 0
        letters.add(s[0])

        while right < len(s) - 1:
            right += 1
            while s[right] in letters: # letter collision
                    letters.remove(s[left])
                    left += 1
            # left and right are stabilized
            letters.add(s[right])
            longest = max(longest, right - left + 1)

        return longest