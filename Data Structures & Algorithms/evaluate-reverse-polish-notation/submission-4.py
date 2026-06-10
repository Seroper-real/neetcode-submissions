class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        for token in tokens: store.append(token)
        return self.rec_eval(store)

    def rec_eval(self, store: List[str]) -> int:
        #print(f"store:{store}")
        sign = store.pop()
        if self.is_int(sign): return int(sign)
        right = int(store.pop()) if not self.is_sign(store[-1]) else self.rec_eval(store)
        left  = int(store.pop()) if not self.is_sign(store[-1]) else self.rec_eval(store)
        #print(f"{left} {sign} {right}")
        if sign == '+': return left + right
        if sign == '-': return left - right
        if sign == '*': return left * right
        if sign == '/': return int(left / right)


    def is_sign(self, char:str) -> bool:
        return char in {'+','-','*','/'}

    def is_int(self, val:str) -> bool:
        try:
            int(val)
            return True
        except Exception:
            return False