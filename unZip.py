from readXML import dehtml
from os import listdir, path, mkdir,  
import zipfile
import time

def main(): 
    zipDir = 'data/CorpusZip'
    txtDir = 'data/CorpusTXT'
    exDir = 'data/extract'
    
    if path.isdir(zipDir):mkdir(zipDir) 
    if path.isdir(txtDir):mkdir(txtDir) 
    if path.isdir(exDir):mkdir(exDir) 
    
    zipFiles = listdir(zipDir) 
    startTime = time.time()
    for fileName in zipFiles:
        name = fileName.split('.')[0]
        if(not path.exists(txtDir + '\\' + name + '.txt')):
            with zipfile.ZipFile(zipDir + '\\' + fileName, 'r') as zf:
                zf.extractall(path = exDir)
            
            
            with open(exDir + '\\' + name,'r',encoding='utf_8') as f1:
                s = f1.read() 
                nukown = ['\u3038','\uf6d7','\uf752','\ufffd','\uf751']
                for ch in nukown:
                    s = s.replace(ch,"")
                
                with open(txtDir + '\\' + name + '.txt','w') as f2:
                    f2.write(dehtml(s))
                with open('time.txt','w') as f3:
                    f3.write(str(time.time() - startTime))
    print('The total Time: {} mins'.format((time.time() - startTime)//60))
 
if __name__ == '__main__': 
    main() 
    

    