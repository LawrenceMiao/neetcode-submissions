class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            while not s[i].isalpha() and not s[i].isnumeric():
                i += 1
                if j <= i:
                    return True
            while not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            
            if j <= i:
                return True