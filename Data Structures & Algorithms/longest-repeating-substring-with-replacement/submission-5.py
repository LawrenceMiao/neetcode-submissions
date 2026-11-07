class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_seq = 0
        for i in range(0, len(s) - 1):
            direction = 1 # 1 for right -1 for left
            seq = 0 # seq_len
            k_p = k # number of chars left
            j = i # index of a char to replace
            character = s[i] # char we are replacing with
            while j != -1:
                if s[j] != character: # replace condition
                    if k_p == 0: # no more left, return seq
                        break
                    k_p -= 1 # replace successful
                seq += 1
                j += direction
                if j == len(s): # checking left side characters
                    direction = -1
                    j = i
                    seq -= 1
            max_seq = max(max_seq, seq)

        return max_seq
            

            