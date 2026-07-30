class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(lp, rp, partial):
            if lp == 0 and rp == 0: res.append(partial)

            if lp > 0:
                dfs(lp-1, rp, partial + '(')
            
            if rp > 0 and rp > lp:
                dfs(lp, rp - 1, partial + ')')
        
        dfs(n,n, "")
        return res
        