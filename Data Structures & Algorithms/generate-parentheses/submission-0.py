class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(lp, rp, partial):
            if lp == 0 and rp == 0: res.append(partial)

            if lp > 0:
                partial += '('
                dfs(lp-1, rp, partial)
                partial = partial[:-1]
            
            if rp > 0 and rp > lp:
                partial += ')'
                dfs(lp, rp - 1, partial)
                partial = partial[:-1]
        
        dfs(n,n, "")
        return res
        