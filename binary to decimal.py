n=1110
d=0
b=1
while n:
    r=n%10
    n=n//10
    d+=r*b
    b*=2
print(d)
