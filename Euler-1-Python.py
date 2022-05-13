# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Checking if number is divisible by 3 or 5
def check(num):
    
    if num % 3 == 0 or num % 5 == 0:
        return True

    return False


# Function that goes from 1 to maxNum and sums only numbers divisible by 3 and 5
def listNumbers(maxNum):

    sumD = 0

    for i in range(1, maxNum):

        if check(i):
            sumD += i

    print(f"Sum = {sumD}")


listNumbers(1000)

# Ans: Sum = 233168
    
