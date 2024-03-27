N=5
def factorial(N):
    for i in range(1, N+1):
        if(N==0):
              return 1
        elif(N==1):
               return 1
        else:
               return i* factorial(i-1)
        


factorials = factorial(N)

for factorial in factorials :
    print(factorial)