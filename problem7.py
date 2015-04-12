p = 2
n = 105500

l = [None] * n

for i in range(p, n):
	if l[i] == None:
		j = 2
		while (j*p) < n:
			l[j*p] = False
			j+=1
		l[i] = True
		p = i
		if l.count(True) == 10001:
			print "yesy"
			break;

print l.count(True)
print len(l) - l[::-1].index(True)-1
