""" 
    Problme 7
    10001st prime 

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10001st prime number?

    >>> 10001th prime number is 104743

""" 
import math

def is_prime(number):
    """return True if number is prime number else False

        Args:
            number ([int]): [should Enter the integer value]

        Returns:
            [bool]: [returns the boolean type ]
    """
    if number <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if(number % i== 0):
                return False
        else:
            return True


def nthPrime(number):
    """return the nth number prime      

        Args:
            number ([integer]): [nth number of the prime number]

        Returns:
            [interger]: [return the nth number prime]
    """

    count = 0
    prime_count = 1
    while(prime_count <= number ):
        if (is_prime(count)):
            # print('{},{}'.format(prime_count,count))
            prime_count +=1
        count += 1
    return count-1



if __name__ == "__main__":
    print("10001th prime number is",nthPrime(10001))

