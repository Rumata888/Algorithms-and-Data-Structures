def InputArray():
    a=True
    array=[]
    while a:
        b=input()
        if b=='exit':
            break
        array=array+[int(b)]
    return array

def FindSum(a,b):
    Min=[0]
    i=1
    while i<=b:
        c=None
        for k in a:
            if(i>=k):
                if(Min[i-k]!=None):
                    if(c!=None):
                        if(c>Min[i-k]+1):
                            c=Min[i-k]+1
                    else:
                        c=Min[i-k]+1
        Min.append(c)
        i=i+1
    return Min[b]

print('Please enter the coin numbers')
a=InputArray()
b=int(input('Please enter sum: '))
print('Solution: '+str(FindSum(a,b)))
            
                
            
            