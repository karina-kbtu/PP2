n=int(input())
def recursive_func_fibonacci(n):
    if(n<=1):
        return n
    else:
        return recursive_func_fibonacci(n-1)+recursive_func_fibonacci(n-2)
print(recursive_func_fibonacci(n))