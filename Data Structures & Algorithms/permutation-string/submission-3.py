class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store1 = defaultdict(int)
        for c in s1: store1[c] += 1
        lid, rid = 0, 0
        store2 = defaultdict(int)
        while rid < len(s2):
            c = s2[rid]
            store2[c] += 1
            if (rid-lid+1) > len(s1):
                ch = s2[lid]
                store2[ch] -= 1
                lid+=1
            rid+=1
            found = True
            for k,val in store1.items():
                if k not in store2 or store2[k] != val:
                    found = False
                    break
            if found: return True
        return False