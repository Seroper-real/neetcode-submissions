class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s:
            if self.isValid(c):
                filtered+=c
        if filtered == "": return True
        print(filtered)
        lid, rid = 0, len(filtered) - 1
        while lid < rid:
            print(f"comparing: {lid},{rid}")
            if not self.isEqual(filtered[lid],filtered[rid]): return False
            lid+=1
            rid-=1
        return True

    def isValid(self, c: str) -> bool:
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'

    def isEqual(self, a:str, b:str) -> bool:
        return a.upper() == b.upper()
        #print(ord(a),ord(b),ord('A'),ord('a'))
        #return a == b or (ord(a) - ord('A')) == (ord(b) - ord('a')) or (ord(a) - ord('a')) == (ord(b) - ord('A'))