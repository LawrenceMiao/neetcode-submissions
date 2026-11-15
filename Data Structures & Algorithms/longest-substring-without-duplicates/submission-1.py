class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest: int = 0
        letter_pool = set()

        left = 0
        right = 0

        while right < len(s):
            while s[right] in letter_pool:
                letter_pool.remove(s[left])
                left += 1
            letter_pool.add(s[right])
            longest = max(longest, right + 1 - left)
            right += 1

        return longest