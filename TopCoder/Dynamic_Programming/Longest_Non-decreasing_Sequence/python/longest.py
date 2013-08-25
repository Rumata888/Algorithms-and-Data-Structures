def InputArray():
    a=True
    array=[]
    while a:
        b=input()
        if b=='exit':
            break
        array=array+[int(b)]
    return array
def FindSolution(a):
    save=1
    Min=[1]
    i=1
    while i<len(a):
        j=0;
        Min.append(1)
        for k in Min[0:i]:
            if (a[j]<=a[i]):
                if(Min[i]<(k+1)):
                    Min[i]=k+1
            j=j+1
        if Min[i]>save:
            save=Min[i]
        i=i+1
    return  save

print("Please input sequence")
a=InputArray()
print('Solution: '+ str(FindSolution(a)))