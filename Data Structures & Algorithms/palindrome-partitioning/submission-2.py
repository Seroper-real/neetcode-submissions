class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s: str) -> bool:
            mx = len(s)-1
            for i in range((mx // 2)+1):
                if s[i] != s[mx-i]: return False
            return True
        
        res = []
        def sub_part(s: str, partial: List[str]):
            if len(s) == 0:
                res.append(list(partial))
                return
            tmp = ""
            for i in range(len(s)):
                tmp+=s[i]
                #print(partial, tmp)
                if is_palindrome(tmp):
                    partial.append(tmp)
                    sub_part(s[i+1:],partial)
                    partial.pop()

        sub_part(s,[])
        return res
