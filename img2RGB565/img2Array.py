from PIL import Image
import numpy as np

import sys


def map(x,in_min,in_max,out_min,out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)



def conv(inf,onf,imw,imh,cha,alphaColor,alphaadj):
    print("in file : %s"% inf)
    print("out file : %s"% onf)
    print("adj_width : %d"% int(imw))
    print("adj_height : %d"% int(imh))
    print("channel : %d"% int(cha))

    apc = int(alphaColor).to_bytes(2,byteorder = "big",signed = False)
    print("alpha color : ",end="")
    print(apc)

    print("alpha adj : %d"%int(alphaadj))
    
    img_in = Image.open(inf)
    #img.show()
    pwidth = int(imw)
    pheight = int(imh)
    img = img_in.resize((pwidth, pheight),Image.ANTIALIAS)

    img_array = np.array(img)#把图像转成数组格式img = np.asarray(image)
    shape = img_array.shape

    height = shape[0]
    width = shape[1]

    ofv = open(onf,'wb')

    try:
        pixlen = len(img_array[1,1])
        use_plen = pixlen
        print('\r\n')
    except:
        use_plen = 1
        print("only one channel\r\n")

    for y in range(0,height):
        for x in range (0,width):
            #img_array[y,x]
            b=0
            g=0
            r=0
            a=0
            allowSkip = 0
            if(use_plen == 4):
                b,g,r,a = img_array[y,x]
                if(a > int(alphaadj)):
                    allowSkip = 1;
            if(use_plen == 3):
                b,g,r = img_array[y,x]
            
            
            if(allowSkip):
                ofv.write(apc)
            else:
                b5 = map(b,0,255,0,0x1f)
                g5 = map(g,0,255,0,0x3f)
                r5 = map(r,0,255,0,0x1f)
        
                bgr = ((b5 & 0x1f)<<11) | ((g5 & 0x3f)<<5) | (r5 & 0x1f)
                bgr &= 0xffff

                sb = bgr.to_bytes(2,byteorder = "big",signed = False)
                ofv.write(sb)

            pass  #x
        pass

    ofv.close()
    pass


if __name__ == "__main__":
    argc = len(sys.argv)

    if(argc != 8):
        print("use img2Array.py [infile] [out W] [out H] [outFile] [channel] [alpha color] [alpha adj]")
        exit(0);
    pass
    conv(sys.argv[1],sys.argv[4],sys.argv[2],sys.argv[3],sys.argv[5],sys.argv[6],sys.argv[7])




