

def main():
	maxno = 0
	for x in xrange(1000, 100, -1):
		for y in xrange(1000, 100, -1):
			if str(x*y) == str(x*y)[::-1]:
				if x*y > maxno:
					maxno = x*y

	print maxno
			
			
if __name__ == "__main__":
	main()

