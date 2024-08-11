import make_testcase
import answer
import os
import zipfile

output_dir = '지름 구하기 test_case'
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(f"{output_dir}/test_case.zip", 'w') as zipf:
    cnt = 1
    for i in range(1, 31):
        
        # .txt 파일 생성
        first_file = f"{output_dir}/{cnt}.in"
        with open(first_file, 'w') as f:
            num = make_testcase.Calculate(i)
            board = num.values()
            for j in range(2):
                if j==0:
                    f.write(str(board[j])+' ')
                else:
                    f.write(str(board[j]))
        
        # .out 파일 생성
        second_file = f"{output_dir}/{cnt}.out"
        with open(second_file, 'w') as ff:
            ff.write(str(answer.ans(board)))

        zipf.write(first_file, arcname=f"{cnt}.in")
        zipf.write(second_file, arcname=f"{cnt}.out")
        cnt+=1

        os.remove(first_file)
        os.remove(second_file)

print("zip 파일 생성")
