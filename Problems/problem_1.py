def sumDivisibleBy(i, n):
	p = i // n
	return (n*(p*(p+1))) // 2

def sumInRange(_from, _to):
	s = 0
	for i in range(_from, _to):
		if(i % 3 == 0 or i % 5 == 0):
			s += i
	return s


if __name__ == '__main__':
	_from, _to = 0, 1000000000
	#~ print(sumInRange(_from, _to))
	k = sumDivisibleBy(999, 3) + sumDivisibleBy(999, 5) - sumDivisibleBy(999, 15)
	print(k)
