class InsertionSort:
    @staticmethod
    def Sort(a,b):
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


a=[3,2,1]
b=3
InsertionSort.Sort(a, b)
print(a)
        
         
        