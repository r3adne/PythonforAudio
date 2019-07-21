# this file is called 'divisibility.py'

def divisibleByThree(number):
    """ returns True if number is divisible by 3, returns False otherwise. """
    sum = 0
    for i in list(str(number)):
        sum += int(i)

    if len(str(sum)) > 1:
        if divisibleByThree(sum) == True:
            return True
        else:
            return False
    else:
        if (sum == 9 or sum == 6 or sum == 3):
            return True
        else:
            return False






number_to_test = 3747


