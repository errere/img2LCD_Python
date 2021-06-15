from PIL import Image
import numpy as np

import sys


def map(x,in_min,in_max,out_min,out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def getpx(a,b,c,fix):
    if(a > fix and b > fix and c > fix):
        return 1
    return 0



def conv(ifdir,ofdir,offW,offH,mm,usrfix=128):
    print("input file name : %s"%ifdir)
    print("output file name : %s"%ofdir)

    img_in = Image.open(ifdir)
    print("icon: : W : %d H : %d"%(img_in.width,img_in.height))

    pwidth = int(offW)
    print("adj_width : %d"%pwidth)
    pheight = int(offH)
    print("adj_height : %d"%pheight)
    

    img = img_in.resize((pwidth, pheight),Image.ANTIALIAS)

    img_array = np.array(img)#把图像转成数组格式img = np.asarray(image)

    shape = img_array.shape
    height = shape[0]
    width = shape[1]

    if(width % 8 != 0):
        print("error width % 8 != 0(W = %d)"%width)
        exit(-1)

    width = int(width / 8)

    ofv = open(ofdir,'wb')

    widthHd = width * 8;
    sb = widthHd.to_bytes(2,byteorder = "big",signed = False)
    #ofv.write(sb)

    sb = height.to_bytes(2,byteorder = "big",signed = False)
    #ofv.write(sb)

    ffix = int(usrfix)
    print("fix : %s"%ffix)
    imod = 0

    #imod = len()
    try:
        pixlen = len(img_array[1,1])
        use_plen = pixlen
        print("\r\n")
    except:
        use_plen = 1
        print("only one channel\r\n")


    for y in range(0,height):
        for x in range (0,width):
        #img_array[y,x]

            xbm = 0

            ts = 7

            for i in range(0,8):
        
                b=0
                g=0
                r=0
                a=0

                if(use_plen == 4):
                    [b,g,r,a] = img_array[y,(8*x) + i]
                elif(use_plen == 3):
                    [b,g,r] = img_array[y,(8*x) + i]
                elif(use_plen == 1):
                    r = img_array[y,(8*x) + i]
                    b=r;
                    g=r;
                    #print("%d",int(r))

                xbm |= getpx(r,g,b,ffix) << (i)
        


            xbm = xbm & 0xff
            sb = xbm.to_bytes(1,byteorder = "big",signed = False)
            ofv.write(sb)
        #print(sb)

            pass
        pass

    ofv.close()
    pass


if __name__ == "__main__":
    argc = len(sys.argv)

    if(argc != 7):
        print("use img2XBM.py [infile] [out W] [out H] [outFile] [pixel channal] [fix]")
        pass

    conv(sys.argv[1],sys.argv[4],sys.argv[2],sys.argv[3],sys.argv[5],sys.argv[6])