def LoadArrayFromFile(a):
    f=open(a,'r')
    b=[]
    for k in f:
        b.append(int(k))
    f.close()
    return b

def ZigZag(a):
    zig=[[1,1]]
    i=1
    max=1
    while i<len(a):
        zig.append([1,1])
        k=0;
        for el in a[0:i]:
            if((zig[k][0]+1)>zig[i][1])&(a[i]<el):
                zig[i][1]=zig[k][0]+1
                if(max<zig[i][1]):
                    max=zig[i][1]
            if((zig[k][1]+1)>zig[i][0])&(a[i]>el):
                zig[i][0]=zig[k][1]+1
                if(max<zig[i][0]):
                    max=zig[i][0]
            k=k+1
        i=i+1
    return max

print('Longest ZigZag (solved by dp): '+str(ZigZag(LoadArrayFromFile(input('Please enter file: ')))))
            