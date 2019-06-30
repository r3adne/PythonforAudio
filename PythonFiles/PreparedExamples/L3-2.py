# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

def isPrime(n):
    """ checks whether a number n is prime """
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, (n // 2) + 1):

        if n % i == 0: # if n is divisible by i
            return False

    return True


i = 1 # nth prime
n = 3 # number to check

while i < 10001:
    if isPrime(n):
        i += 1
        print('{}: {}'.format(i, n))

    n += 2

