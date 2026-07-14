class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            groups.setdefault("".join(sorted(string)), []).append(string)
        return list(groups.values())