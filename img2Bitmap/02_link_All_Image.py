#python 02_link_All_Image.py C:\Users\Administrator\Desktop\新建文件夹\新建文件夹 .png 16 .16bin 1 out.binarya
import os 
import img2XBM
from PIL import Image
import numpy as np
import sys
import lookout_All_Img

def countFile(workdir,endwith):
    cnt = 0
    lin = list()
    for root, dirs, files in os.walk(workdir):#"C:\\Users\\Administrator\\Desktop\\新建文件夹\\新建文件夹"
        for name in files:
            if(name.endswith(endwith)):
                cnt+=1
                lin.append( "\\" + name)
                pass
            pass
        pass
    return cnt,lin;
                


#print(sys.argv[0])

if __name__ == "__main__":
    if(len(sys.argv) != 8):
        #                  0                 1           2           3         4          5     6               7
        print("use 01_lookout_All_Img.py [workDir] [img end with] [size] [out end with] [bpp] [fix] [link out file name]")
        exit(0);

    if(int(sys.argv[3]) >255):
        print("error icon max size is 255 x 255")
        exit(0);

    print("\r\n\r\n============================converting==============================\r\n\r\n")

    lookout_All_Img.ModAll(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

    print("\r\n\r\n============================linking==============================\r\n\r\n")
    
    iconSZ = int(sys.argv[3]) * int(sys.argv[3]) / 8
    lkofdir = sys.argv[1] + "\\" + sys.argv[7]
    infilecount,infileList = countFile(sys.argv[1],sys.argv[4])#C:\\Users\\Administrator\\Desktop\\新建文件夹\\新建文件夹
    print("icon file cnt : %d"%infilecount)
    print("icon file size : %d Bytes"%iconSZ)
    print("icon size : %s x %s"%(sys.argv[3],sys.argv[3]))

    print("output file : %s"%lkofdir)
    print("input file :")
    for ll in infileList:
        print(ll)

    try:
        os.remove(lkofdir)
    except:
        print("file is new")
    
    lkoff = open(lkofdir,'wb')
    '''
    //byteorder = "big"
	typedef struct {
        
		uint16_t icon_cnt;
		uint8_t icon_Size;
		uint16_t icon_length;
		uint8_t** icon;

	}icon_struct;
    
    os.remove(path)  
    '''
    print("HeadWriter count : 0x%04x (%d)"%(int(infilecount) , int(infilecount)))
    print("HeadWriter size : 0x%04x (%d)"%(int(sys.argv[3]) , int(sys.argv[3])))
    print("HeadWriter count : 0x%04x (%d)"%(int(iconSZ) , int(iconSZ)))
    #icon cnt
    sb = int(infilecount).to_bytes(2,byteorder = "big",signed = False)
    lkoff.write(sb);
    #icon size
    sc = int(sys.argv[3]).to_bytes(1,byteorder = "big",signed = False)
    lkoff.write(sc);
    #icon_length
    sd = int(iconSZ).to_bytes(2,byteorder = "big",signed = False)
    lkoff.write(sd);
    

    for ll in infileList:
        
        ffsize  = os.path.getsize(sys.argv[1] + ll)
        print("copy %d byte data from %s to %s"%(ffsize,ll,sys.argv[7]))
        tmpfp = open(sys.argv[1] + ll,"rb");
        tmp = tmpfp.read(ffsize)
        lkoff.write(tmp);
        tmpfp.close()
        print("remove tmp file %s\r\n"%(sys.argv[1] + ll))
        os.remove(sys.argv[1] + ll)
        pass
    lkoff.close()
    print("!!!  PLEASE CHECK FILE HEADER WITH DOWN VALUE  !!!")
    print("Header 0:1 -> %04x"%(int(infilecount)))
    print("Header 2 -> %02x"%(int(sys.argv[3])))
    print("Header 3:4 -> %04x "%(int(iconSZ)))
    print("\r\n\r\noutput file : %s"%lkofdir)
    print("output file size: %s Bytes"%os.path.getsize(lkofdir))
    print("\r\n\r\n============================script end==============================\r\n\r\n")

    
    