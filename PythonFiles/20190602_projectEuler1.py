# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
for i in range(1000): # this is wrong
    if i % 3 == 0: # if i is divisible by 3
        sum += i 
    if i % 5 == 0: # if i is divisible by 5
        sum += i 
    
print(sum)



sum = 0
for i in range(1000): # this is right
    if i % 3 == 0:
        sum += i 
    if i % 5 == 0:
        sum += i
    if i % 15 == 0:
        sum -= i

print(sum)



sum = 0
for i in range(1000): # this is right 
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i 

print(sum)



def pe1(a, b, number):
    sum = 0
    for i in range(number):
        if i % a == 0:
            sum += i
        elif i % b == 0:
            sum += i 
        
    return sum

print(pe1(3, 5, 1000))

print(pe1(12, 31, 124012))
