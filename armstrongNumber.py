#An armstrong number, also known as a narcissistic number is  the sum of cubes of each digit is equal to the number itself.
import math

def isArmstrong(number):
    sum = 0
    len_Num = len(str(number))
    for digit in str(number):
        num = int(digit)
        sum += math.pow(num,len_Num)

    if(math.trunc(sum) == number):
        print(number, "is an armstrong number.")
    else:
        print(number, "is not an armstrong number.")

isArmstrong(153)#Valid, yes armstrong
isArmstrong(500)#Invalid, not armstrong