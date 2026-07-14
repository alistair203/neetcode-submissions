class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(s)) for s in strs]
        return ",".join(lengths) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        lengths = s.split("#")[0].split(",")
        lengths = [int(n) for n in lengths if n != ""]
        s = s[len(s.split("#")[0]) + 1:]
        strings = []
        i = 0
        for n in lengths:
            strings.append("".join(s[i:i + n]))
            i += n
        return strings
        

            
