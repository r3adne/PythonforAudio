# this file is called 'divisibility.py'

def divisibleByThree(number):
    sum = 0
    for i in list(str(number)):
        sum += int(i)

    if len(str(sum)) > 1:
        if divisibleByThree(sum) == True:
            return True
    else:
        if (sum == 9 or sum == 6 or sum == 3):
            return True
        else:
            return False

