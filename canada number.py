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
    for i in range(1,int((n**0.5))+1):
        if n%i==0:
            if i==n//i:
                print('if',i)
                s1+=i
            else:
                print('else',i)
                s1+=(i+n//i)
    return(s1-1-n)
def prgrm(n):
    if(xyz(n)==num(n)):
        return(True)
    else:
        return(False)
print(prgrm(n))
    

        
