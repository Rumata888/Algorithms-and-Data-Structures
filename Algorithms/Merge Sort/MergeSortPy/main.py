class FileWork:
    @staticmethod
    def LoadFile(a):
        f=open(a,'r')
        array=[]
        for line in f:
            array=array+[int(line)]
        f.close()
        return array
    @staticmethod
    def SaveFile(a,b):
        f=open(a,'w+')
        for line in b:
            f.write(str(line)+"\n")
        f.close()
class Sorts:
    @staticmethod
    def Merge(a,b):
        c=[]
        d=0
        e=0
        while ((d<len(a))&(e<len(b))):
            if (a[d] < b[e]):
                c.append(a[d])
                d=d+1
            else:
                c.append(b[e])
                e=e+1
        while(d<(len(a))):
            c.append(a[d])
            d=d+1

        while(e<(len(b))):    
            c.append(b[e])
            e=e+1
        return c;
    @staticmethod
    def MergeSort(a,x):
        if(len(a)>1):
            b=Sorts.MergeSort(a[0:int(len(a)/2)],x+"1")
            
            c=Sorts.MergeSort(a[int(len(a)/2):int(len(a))],x+"0")
            d=Sorts.Merge(b,c)
            return d
        else:
            return a
        
a=FileWork.LoadFile("sequence.txt")
a=Sorts.MergeSort(a,"")
FileWork.SaveFile("output.txt", a)