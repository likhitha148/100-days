a=[1,0,2,3,0,4,5,0]
s=[]
for i in range(len(a)):
    if a[i]!=0:
        s.append(a[i])
    else:
        s.extend([a[i],0])
print(s[:len(a)])
