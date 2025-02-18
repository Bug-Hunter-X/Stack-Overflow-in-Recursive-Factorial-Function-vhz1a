def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 5
result = factorial(number)
print(result)

number = -5
try:
    result = factorial(number)
    print(result)
except ValueError as e:
    print("Error:", e)