fib0 = 0
fib1 = 1
s = 0
while(fib1 < 4000000):

	fib2 = fib0 + fib1
	fib0 = fib1
	fib1 = fib2
	if fib1 % 2 == 0:
		s += fib1

	
print s
