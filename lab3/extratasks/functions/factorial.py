n=int(input())
def recursive_func_factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n* recursive_func_factorial(n-1)
print(recursive_func_factorial(n))