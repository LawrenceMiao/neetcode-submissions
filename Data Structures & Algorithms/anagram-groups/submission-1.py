class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s1, s2):
            return sorted(list(s1)) == sorted(list(s2))
        out = []
        while len(strs) > 0:
            compare = strs[len(strs) - 1]
            collection = [compare]
            del strs[len(strs) - 1]
            i = len(strs) - 1
            while i >= 0:
                if isAnagram(compare, strs[i]):
                    collection.append(strs[i])
                    del strs[i]
                i -= 1
            out.append(collection)
        return out
