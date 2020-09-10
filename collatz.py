n=int(input())
def collatz(n):
    if n==1:
        return str(1)
    else:
        if n%2==0:
            n1=n//2
            return(str(n) + " " + collatz(n1))
        else:
            n1=n*3+1
            return(str(n) + " " +collatz(n1))
print(collatz(n))
    
