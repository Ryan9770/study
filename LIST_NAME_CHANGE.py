import os

file_path = os.path.join("C:\\Users\\USER\\Desktop\\your_path") # 파일이 존재하는 경로

i=1
for file in os.listdir(file_path):                      # 경로 안에 존재하는 파일 리스트
    if i < 10:
        file_nm = '05_img_0'+str(i)+'.png'                 #변경하고 싶은 파일 이름
    else:
        file_nm = '05_img_'+str(i)+'.png'
    
    os.rename(file_path+'\\'+file,file_path+'\\'+file_nm)  # 원본파일 경로\\원본파일, 변경파일 경로\\변경파일명
    i += 1      #인덱스 증가시 사용
    

