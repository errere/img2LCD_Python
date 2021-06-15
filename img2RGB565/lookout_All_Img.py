import os 
import img2Array
from PIL import Image
import numpy as np
import sys

#print(sys.argv[0])

def ModAll(workdir,endwith,outw,outh,outendwith,channel,alphaColor,fix=128):
    for root, dirs, files in os.walk(workdir):#"C:\\Users\\Administrator\\Desktop\\新建文件夹\\新建文件夹"
        for name in files:
            if(name.endswith(endwith)):
                #print(root + "\\" + name)
                ifd = root + "\\" + name
                ofd = root + "\\" + name + outendwith
                #img2XBM.conv(ifd,ofd,Osize,bpp,fix)
                img2Array.conv(ifd,ofd,outw,outh,channel,alphaColor,fix)


if __name__ == "__main__":
    if(len(sys.argv) != 9):
        #print("use img2Array.py [infile] [out W] [out H] [outFile] [channel] [alpha color] [alpha adj]")
        print("use 01_lookout_All_Img.py [workDir] [img end with] [out W] [out H] [out end with] [channel] [alpha color] [alpha adj]")
        exit(0)
    print("\r\n\r\n")
    ModAll(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
    