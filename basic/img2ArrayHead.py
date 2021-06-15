from PIL import Image
import numpy as np

import sys


def map(x,in_min,in_max,out_min,out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


argc = len(sys.argv)

if(argc != 5):
    print("use img2Array.py [infile] [out W] [out H] [outFile]")
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

ofv = open(sys.argv[4],'wb')

sb = width.to_bytes(2,byteorder = "big",signed = False)
ofv.write(sb)

sb = height.to_bytes(2,byteorder = "big",signed = False)
ofv.write(sb)

for y in range(0,height):
    for x in range (0,width):
        #img_array[y,x]
        b=0
        g=0
        r=0
        a=0
        if(len(img_array[y,x]) == 4):
            b,g,r,a = img_array[y,x]
        if(len(img_array[y,x]) == 3):
            b,g,r = img_array[y,x]
        
        b5 = map(b,0,255,0,0x1f)
        g5 = map(g,0,255,0,0x3f)
        r5 = map(r,0,255,0,0x1f)
        
        bgr = ((b5 & 0x1f)<<11) | ((g5 & 0x3f)<<5) | (r5 & 0x1f)
        bgr &= 0xffff

        sb = bgr.to_bytes(2,byteorder = "big",signed = False)
        ofv.write(sb)
        #print(sb)

        pass
    pass

ofv.close()

