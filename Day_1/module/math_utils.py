def square (num):
    return num * num
    
def cube (num):
    return num * num * num
    
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
def square_root(x):
    if x < 0:
        return "Square root not defined for negative numbers"
    return x ** 0.5
