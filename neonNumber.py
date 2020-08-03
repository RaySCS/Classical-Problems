#Neon number: A number is said to be a Neon Number if the sum of digits of the square of the number is equal to thenumber itself. Example 9 is a Neon Number. 9*9=81 and 8+1=9.Hence it is a Neon Number.


import math

def isNeonNumber(number):
    squaredNum = math.pow(number,2)
    #seperate digits of squaredNum
    sum = 0
    for digit in str(math.trunc(squaredNum)):
        num = int(digit)
        sum+=num

    if(sum == number):
        print(squaredNum, "is a neon number")
    else:
        print(squaredNum, "is not a neon number")

isNeonNumber(9)#Valid Neon number
isNeonNumber(10)#Invalid Neon number