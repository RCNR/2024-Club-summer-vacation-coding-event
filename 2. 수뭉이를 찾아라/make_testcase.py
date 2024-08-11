# 구해야 하는 것 : A~Z 두개씩 뽑아야함 -> 총 개수는 반드시 짝수개임이 자명함
# 최소 1명 ~ 최대 30명임 -> 그럼 글자는 2 ~ 60개임
import random
import string

class Calculate:
    def __init__(self, n):
        self.n = n
    
    def values(self):
        res = ''
        
        for _ in range(self.n):
            # 요청한 인원의 2배 만큼 루프 돌리는 게 맞음 -> 하지만 한번 돌 때 무조건적으로 대문자 2개를 넣을 것임
            # 이는 S가 나오면 바로 다음 문자를 M으로 고정시키기 위함
            # 하지만 SSMS -> 0 같은 경우는 따로 넣어줘야 할 듯
            uppercase_letter = random.choice(string.ascii_uppercase)
            if uppercase_letter == 'S':
                res += uppercase_letter + 'M' # 무조건적으로 M 추가
            else:
                res += uppercase_letter + random.choice(string.ascii_uppercase)
        return res


