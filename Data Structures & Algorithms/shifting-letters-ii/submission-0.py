class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        f_prime: list[int] = [0 for i in range(len(s))]
        for start, end, direction in shifts:
            f_prime[start] += 1 if direction == 1 else -1
            if end+1 < len(f_prime):
                f_prime[end+1] -= 1 if direction == 1 else -1

        f: list[int] = [0 for i in range(len(s))]
        slope = 0

        for i in range(len(f_prime)):
            slope += f_prime[i]
            f[i] = slope

        letter_list = []

        for i in range(len(s)):
            new_letter = chr((((ord(s[i]) - ord('a')) + f[i]) % 26) + ord('a'))
            letter_list.append(new_letter)

        # print(f_prime)
        # print(f)

        return "".join(letter_list)


        