class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            n = len(string)
            code += f"{n}#{string}"
        return code

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            n = int(n)
            i += 1
            strings.append("".join(s[i: i + n]))
            i += n
        return strings
        

            
