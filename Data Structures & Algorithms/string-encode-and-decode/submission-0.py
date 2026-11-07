class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        
        for i in strs:
            length = str(len(i))
            length = "0" * (3 - len(length)) + length

            out += length + i

        return out
    def decode(self, s: str) -> List[str]:
        out: list[str] = []
        lengthStart = 0

        while lengthStart < len(s):
            length = s[lengthStart: lengthStart + 3]
            if length == "000":
                length = 0
            else:
                length = int(length.lstrip("0"))

            out.append(s[lengthStart + 3 : lengthStart + 3 + length])
            lengthStart += 3 + length


        return out
