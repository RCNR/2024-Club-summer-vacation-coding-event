# 구해야 하는 것 -> 칠판의 한 변의 길이 : N, 다른 한 변의 길이 : M
# 같아도 달라도 상관 없음
from random import randrange

class Calculate:
    def __init__(self, n):
        self.n = n
    
    def values(self):
        res = []
        a = randrange(1, 501)
        b = randrange(1, 501)
        res.append(a)
        res.append(b)
        return res
            
