#Fibonacci sequence: number is the sum of the two preceding ones, starting from 0 and 1.
#Recursive function

def getNthFibanocci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return getNthFibanocci(n-1) + getNthFibanocci(n-2)


#Test cases
print(getNthFibanocci(9))#21
print(getNthFibanocci(4))#2