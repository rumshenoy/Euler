s = 1000

def gcd(x, y):
	
	if y > x :
		temp = x
		x = y
		y = temp

	while(y):
		x, y = y, x % y

	return x



