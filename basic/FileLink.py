import os 
import sys

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
                
def LinkFile(workdir,ifend,ofname):
    print("\r\n\r\n============================linking==============================\r\n\r\n")

    infilecount,infileList = countFile(workdir,ifend)

    lkofdir = workdir + "\\" + ofname

    print("output file : %s"%lkofdir)
    print("input file :")
    for ll in infileList:
        print(ll)

    try:
        os.remove(lkofdir)
    except:
        print("file is new")
    
    lkoff = open(lkofdir,'wb')

    for ll in infileList:
        
        ffsize  = os.path.getsize(sys.argv[1] + ll)
        print("copy %d byte data from %s to %s"%(ffsize,ll,ofname))
        tmpfp = open(sys.argv[1] + ll,"rb");
        tmp = tmpfp.read(ffsize)
        lkoff.write(tmp);
        tmpfp.close()
        #print("remove tmp file %s\r\n"%(sys.argv[1] + ll))
        os.remove(sys.argv[1] + ll)
        pass
    lkoff.close()

    print("\r\n\r\noutput file : %s"%lkofdir)
    print("output file size: %s Bytes"%os.path.getsize(lkofdir))
    print("\r\n\r\n============================script end==============================\r\n\r\n")
    pass


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        #              0            1               2                  3 
        print("use FileLink.py [workDir] [LinkFile End with] [link out file name]")
        exit(0);
    LinkFile(sys.argv[1],sys.argv[2],sys.argv[3])



    
    