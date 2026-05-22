class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            group = self.get_group(s)
            groups[group].append(s)
        return list(groups.values())

    def get_group(self, s:str) -> str:
        return str(sorted(s))