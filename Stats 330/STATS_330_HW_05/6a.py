import math
ans = 0
for i in xrange(9 + 1):
	ans += math.exp(-5)* pow(5, i)/ math.factorial(i)
print( ans )

