class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        original = []
        for k in c.keys():
            if k == 0:
                if c[k] % 2 > 0:
                    return []
                original += [0] * (c[k]//2)
            elif c[k] > 0:
                x = k
                while x % 2 ==0 and x //2 in c:
                    x = x //2
                while x in c:
                    if c[x] > 0:
                        original += [x]* c[x]
                        if c[x+x] < c[x]:
                            return []
                        c[x+x] -= c[x]
                        c[x] = 0
                    x += x
        return original