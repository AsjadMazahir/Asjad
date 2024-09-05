# factorial function
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# lambda function
x = lambda a: a**3
print(x(3))