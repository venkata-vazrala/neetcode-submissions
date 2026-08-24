class Solution:
    def isValid(self, s: str) -> bool:
        p=[]
        b="{[("
        c="}])"
        for i in s:
            if i in b:
                p.append(i)
            elif len(p)>0 and b[c.index(i)] == p[-1]:
                p.pop()
            else:
                return False
        return len(p) == 0

        