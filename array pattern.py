def pattern():
        a=[1,2,3,1,2]
        m=2
        k=2
        i=0
        n=len(a)
        j=i+m
        c=0
        while j<n:
                if a[i]==a[j]:
                        c+=1
                        if c==m*(k-1):
                                return True
                else:
                        c=0
                        i+=1
                        j+=1
        return False
print(pattern())
