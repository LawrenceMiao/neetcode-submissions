class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_table: list = [0] * 26


        for character in s:
            freq_table[ord(character) - ord('a')] += 1


        for character in t:
            freq_table[ord(character) - ord('a')] -= 1


        return freq_table == [0] * 26