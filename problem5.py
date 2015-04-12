n = 2
d = 2

def gcd(x, y):
	
	if y > x :
		temp = x
		x = y
		y = temp

	while(y):
		x, y = y, x % y

	return x
	

def lcm(x, y):
	return (x * y) / gcd( x, y)
	

while(d != 20):
	print n, d
	if n % d == 0:
		d = d + 1	
	else:
		k = lcm(n, d)
		print "lcm of " + str(n) + " and " + str(d) + ": " + str(k) 
		n = lcm(n, d)

print n
