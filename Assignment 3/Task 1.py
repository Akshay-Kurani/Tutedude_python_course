a = int(input("Enter a number here:" ))


def factorial(a):
    if a < 2:
        return 1
    else: 
        return a * factorial(a-1)

result = factorial(a)
print(result, "is the factorial of", a)
