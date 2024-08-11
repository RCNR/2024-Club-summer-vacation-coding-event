# 무조건적으로 S or M만
import random

class Calculate:
    def __init__(self, n):
        self.n = n
    
    def values(self):
        res = ''
        for _ in range(self.n * 2): # 인원수의 2배 만큼
            uppercase_letter = random.choice(['S', 'M'])
            res += uppercase_letter
        return res


