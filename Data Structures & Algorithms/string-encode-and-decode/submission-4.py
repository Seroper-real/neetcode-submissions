class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for val in strs:
            out += val.replace("\\","\\\\").replace(";","\\;")
            out += ";"
        #print(out)
        return out

    def decode(self, s: str) -> List[str]:
        if not s: return []
        s = s[:-1]
        s = s.replace("\\;",";").replace("\\\\","\\")
        return s.split(";")


    