class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s:
            if self.isValid(c):
                filtered+=c
        if filtered == "": return True
        lid, rid = 0, len(filtered) - 1
        while lid < rid:
            #print(f"comparing: {lid},{rid}")
            if not self.isEqual(filtered[lid],filtered[rid]): return False
            lid+=1
            rid-=1
        return True

    def isValid(self, c: str) -> bool:
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'

    def isEqual(self, a:str, b:str) -> bool:
        return a.upper() == b.upper()