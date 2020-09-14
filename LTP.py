def prime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return(1)
n=int(input('enter a number'))
leng=len(str(n))
cnt=0
while(prime(n)==1 and n>0):
    num=10**(leng-1)
    n%=num
    leng-=1
    if(prime(n)==1):
        cnt=1
    else:
         break
if cnt==1:
    print("yes left truncanted prime")
else:
    print("not a left truncanted prime")
