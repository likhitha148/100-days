n=2545
h=''
while n:
    r=n%16
    if r<10:
        h+=str(chr(r+48))
    else:
        h+=str(chr(r+55))
    n=n//16
print(h[::-1])
