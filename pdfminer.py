from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
# from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
 
path = "D:\\path" #경로 

for (root, directories, files) in os.walk(path): #path 안의 경로/ 디렉토리/ 파일들을 읽어옴
    for file in files: # 파일이 존재하면
        if '.pdf' in file: #만약 파일이 .pdf로 끝나면
            file_path = os.path.join(file) #file의 경로 저장
            
            rsrcmgr = PDFResourceManager()  # PDFResourceManager 선언
            retstr = StringIO()             # StringIO 선언
            codec = 'utf-8'                 # 코텍
            laparams = LAParams()           # pdf layout 읽어옴
            
            file = file.replace('.pdf','')  # 파일 이름을 사용하기 위해 .pdf 제거
            
            f = open(file+'.html', 'wb')   # file이름.html 바이너리/쓰기 모드로 오픈

            device = HTMLConverter(rsrcmgr, f, codec=codec, laparams=laparams) # 변환
            
            fp = open(file_path, 'rb') # 
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0 #is for all
            caching = True
            pagenos=set()
            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
                interpreter.process_page(page)
            fp.close()
            device.close()
            str = retstr.getvalue()
            retstr.close()
            f.close()
