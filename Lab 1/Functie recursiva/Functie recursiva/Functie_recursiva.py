def factorial(x):
    if x==1:
       return 1 
    else:
        return (x * factorial(x-1))
num = int(input("Introdu numaruyl pt. factor. "))
print("Factorialul",num,"este",factorial(num))
