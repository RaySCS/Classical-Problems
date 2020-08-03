# Factorial: 4! = 4*3*2*1

def getNthFactorial(n):
    if (n==1):
        return 1
    else:
        return n * getNthFactorial(n-1)


#Test Cases
print(getNthFactorial(4))#24
print(getNthFactorial(5))#120