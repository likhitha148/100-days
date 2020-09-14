def prime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return(1)
n=int(input('enter a number'))
a=n
cnt=1
while prime(n) and (n>0):
    n=n//10
    if prime(n):
        cnt=1
    else:
        cnt=0
if cnt==1:
    print(a,'right truncanted prime')
else:
    print(a,'not a right truncanted prime')
