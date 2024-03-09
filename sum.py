#Write a Python program to calculate the sum of two numbers and print the result.

def sum():
  num1=int(input("Enter 1st number: "))
  num2=int(input("Enter 2st number: "))
  add=num1+num2
  return (f"Sum of the 2 numbers is: {add}")
b=sum()
print(b)