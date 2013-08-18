class InsertionSort:
    @staticmethod
    def Sort(a):
        b=len(a)
        c=1
        while c<b:
            d=c-1
            k=a[c]
            while d>=0:
                if k<a[d]:
                    a[d+1]=a[d]
                    d=d-1
                else:
                    break
            a[d+1]=k;
            c=c+1;
        return a;
     
class FileWork:
    @staticmethod
    def LoadArray(a):
        f=open(a,'r');
        array=[];
        for line in f:
            array=array+[int(line)]
        f.close()
        return array;
    @staticmethod
    def SaveArray(a,b):
        f=open(a,'w+')
        for line in b:
            f.write(str(line)+"\n")
        f.close()

a=FileWork.LoadArray("sequence.txt")
a=InsertionSort.Sort(a)
FileWork.SaveArray("output.txt", a)
        
         
        