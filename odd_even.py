#Write a Python program to check if a given number is even or odd.
def eveodd():
  while True:
    x = int(input("Enter a number (Enter 0 or negative number to exit): "))
    if x <= 0:
      break
    if x % 2 == 0 and x > 1:
      print(f"Number entered is even: ({x})")
    elif x % 2 != 0 and x>=1:
      print(f"Number entered is odd: ({x})")

eveodd()
