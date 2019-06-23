"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000


Find the sum of all the multiples of a or b below n.

"""


def pe1(n, a, b):
    sum = 0
    for i in range(n):
        if i % a == 0: # if i is divisible by a
            sum += i
        elif i % b == 0:
            sum += i
    return sum

print(pe1(1000, 3, 5))
