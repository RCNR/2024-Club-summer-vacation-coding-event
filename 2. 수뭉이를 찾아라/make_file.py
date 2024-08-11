import make_testcase
import make_SM_testcase
import answer
import os
import zipfile

output_dir = "수뭉이를 찾아라 test_case"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(f"{output_dir}/test_case.zip", 'w') as zipf:
    cnt = 1 # 파일 개수
    for i in range(1, 31):
        # .in 파일 생성
        first_file = f"{output_dir}/{cnt}.in"
        with open(first_file, 'w') as f:
            num = make_testcase.Calculate(i)
            string_res = num.values()

            f.write(string_res)
        
        # .out 파일 생성
        second_file = f"{output_dir}/{cnt}.out"
        with open(second_file, 'w') as ff:
            ff.write(str(answer.ans(i, string_res)))
        
        zipf.write(first_file, arcname=f"{cnt}.in")
        zipf.write(second_file, arcname=f"{cnt}.out")
        cnt+=1
        os.remove(first_file)
        os.remove(second_file)
#----------------------------------------------------------#
    for i in range(1, 31):
        # .in 파일 생성
        first_file = f"{output_dir}/{cnt}.in"
        with open(first_file, 'w') as f:
            num = make_SM_testcase.Calculate(i)
            string_res = num.values()
            f.write(string_res)
        
        # .out 파일 생성
        second_file = f"{output_dir}/{cnt}.out"
        with open(second_file, 'w') as ff:
            ff.write(str(answer.ans(i, string_res)))
        
        zipf.write(first_file, arcname=f"{cnt}.in")
        zipf.write(second_file, arcname=f"{cnt}.out")
        cnt+=1
        os.remove(first_file)
        os.remove(second_file)


print("zip 파일 생성")
