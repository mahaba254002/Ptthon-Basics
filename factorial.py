#Write a Python program to calculate the factorial of a number.

n=int(input("Enter number to factorise: "))
def factorial():
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result =result* i
        return result

factorial_result=factorial()
print(f"The factorial of {n} is: {factorial_result}")