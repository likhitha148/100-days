n='1AB'
d=0
b=1
for  i in range(len(n)):
    r=n[-1]
    if r.isdigit():
        d+=(ord(r)-48)*b
    else:
        d+=(ord(r)-55)*b
    n=n[:-1]
    b*=16
print(d)
