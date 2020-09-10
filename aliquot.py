def Sum(n):
	return sum([i for i in range(1,n//2+1) if n%i == 0])
def aliquot(n):
	if n == 1 :
		return '1'
	s = Sum(n)
	if s != n :
		return str(n) +" "+ aliquot(s)
	return str(n)
print(aliquot(int(input())))
