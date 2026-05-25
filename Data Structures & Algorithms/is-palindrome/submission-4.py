class Solution:
    def isPalindrome(self, s: str) -> bool:
        lid, rid = 0, len(s) - 1
        while lid < rid:
            while lid < rid and not self.isValid(s[lid]): lid+=1
            while lid < rid and not self.isValid(s[rid]): rid-=1
            #print(f"comparing: {lid},{rid}")
            if not self.isEqual(s[lid],s[rid]): return False
            lid+=1
            rid-=1
        return True

    def isValid(self, c: str) -> bool:
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'

    def isEqual(self, a:str, b:str) -> bool:
        return a.upper() == b.upper()