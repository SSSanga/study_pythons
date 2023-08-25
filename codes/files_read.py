## open 할때 정확한 위치의 파일이 존재하는지 확인필. 
## - 기존 txt 파일을 codes로 수동 옮김
## 1. 파일 존재 확인 (wihdow기반으로 진행하므로 import os)
## os.path.exists: 파일 여부 확인
import os

file_path = 'codes/temp_file.txt'

if os.path.exists(file_path): # 존재여부의 return True or False
    ## 2. 파일 관련 업무 실행
    ## file 읽기. temp_file.txt
    ## .read()
    with open(file_path,'r') as fr :
        pass
        load_file_read = fr.read()
        pass
else : 
    print('File Not Exists!')







