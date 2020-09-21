n=8
b=''
while n:
    b+=str(n%2)
    n=n//2
print(b[::-1])
