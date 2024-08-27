# Recursion : It is a function which call itself.

# def factorial (n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))


def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n-1) + fibonacci(n-2)

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i))
