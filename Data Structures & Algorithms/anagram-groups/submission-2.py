class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = ordered string
        # value = list of unordered strings (spelled properly)
        anagram_dict = {}

        for string in strs:
            ordered_string = str(sorted(list(string)))
            if ordered_string not in anagram_dict:
                anagram_dict[ordered_string] = []
            anagram_dict[ordered_string].append(string)

        # discard keys, keep values
        return list(anagram_dict.values())
        