data = "write somethings"

# java의 try cache 역할을 함.
# with open(파일 이름 , 목적(w(=작성), r, etc...)) as fw(with 아래 변수로 사용하려고 ) : 영역표시
    # fw.write(data)
        # with가 자동 close해줌. 
with open ('temp_file.txt', 'w') as fw :
    fw.write(data)

pass
