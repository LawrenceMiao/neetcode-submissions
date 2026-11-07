class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num2length = dict()
        # key: num
        # value: if num is sequence start/end, length of sequence
        #        else: i dont care
        longest_length = 0

        for num in nums:
            if num in num2length:
                # skip
                pass
            elif num - 1 in num2length and num + 1 in num2length:
                new_length = 1 + num2length[num - 1] + num2length[num + 1]
                num2length[num - num2length[num - 1]] = new_length
                num2length[num + num2length[num + 1]] = new_length
                num2length[num] = 1

            elif num - 1 in num2length:
                # num is to the right
                new_length = num2length[num - 1] + 1
                num2length[num] = new_length
                num2length[num - num2length[num - 1]] = new_length
            elif num + 1 in num2length:
                # num to the left
                # new start to sequence
                # set length of sequence
                new_length = num2length[num + 1] + 1
                num2length[num] = new_length
                num2length[num + num2length[num + 1]] = new_length
            else: # no neighbors, unique number
                num2length[num] = 1

        for i in num2length.values():
            if i > longest_length:
                longest_length = i

        return longest_length