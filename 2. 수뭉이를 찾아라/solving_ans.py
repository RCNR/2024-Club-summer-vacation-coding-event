import sys
input = sys.stdin.readline
cnt = 0
str = input().rstrip()

# for i in range(0,len(str), 2):
#     if(str[i] == 'S' and str[i+1] == 'M'):
#         cnt+=1

# print(cnt)


board = [str[i:i+2] for i in range(0, len(str), 2)]
for is_it_SM in board:
    if is_it_SM == 'SM':
        cnt+=1
print(cnt)

# print(str.count('SM'))