from PIL import Image
import numpy as np

import sys


def map(x,in_min,in_max,out_min,out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def getpx(a,b,c,fix):
    if(a > fix and b > fix and c > fix):
        return 1
    return 0


argc = len(sys.argv)

if(argc != 5):
    print("use img2XBM.py [infile] [out W] [out H] [outFile]")
    pass


img_in = Image.open(sys.argv[1])

#img.show()

pwidth = int(sys.argv[2])
pheight = int(sys.argv[3])
img = img_in.resize((pwidth, pheight),Image.ANTIALIAS)

img_array = np.array(img)#把图像转成数组格式img = np.asarray(image)

shape = img_array.shape
height = shape[0]
width = shape[1]

if(width % 8 != 0):
    print("error width % 8 != 0(W = %d)"%width)
    exit(-1)

width = int(width / 8)

ofv = open(sys.argv[4],'wb')

widthHd = width * 8;
sb = widthHd.to_bytes(2,byteorder = "big",signed = False)
ofv.write(sb)

sb = height.to_bytes(2,byteorder = "big",signed = False)
ofv.write(sb)

ffix = 128
imod = 0


imod = len(img_array[1,1])

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

            if(imod == 4):
                [b,g,r,a] = img_array[y,(8*x) + i]
            elif(imod == 3):
                [b,g,r] = img_array[y,(8*x) + i]

            xbm |= getpx(r,g,b,ffix) << (i)
        


        xbm = xbm & 0xff
        sb = xbm.to_bytes(1,byteorder = "big",signed = False)
        ofv.write(sb)
        #print(sb)

        pass
    pass

ofv.close()

