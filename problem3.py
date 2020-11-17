'''The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?
 
 solution
 >>> print(prime_factors[-1])
	 6857
'''

import math

num = 600851475143
prime_factors = []
def is_prime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if(n%i== 0):
			return False
	else:
		return True
#print(is_prime(5))
for i in range(2,int(math.sqrt(num))+1):
	if is_prime(i):
#		print(i)
		if (num % i == 0):
			prime_factors.append(i)

print(prime_factors[-1])


