n=int(input('enter a number:'))
def num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**2
        n=n//10
    return(s)
def xyz(n):
    s1=0
    for i in range(2,n//2+1):
        if n%i==0:
            print(i)
            s1+=i
    if (s1)==num(n):
        return True
    else:
        return False
print(xyz(n))
