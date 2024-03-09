def fibonnaci():
  value= int(input("Enter the number of fibonacci you want: "))
  prev=0 
  current=1

  fib_list=[0,1]
  for i in range(2,value):
    next=prev+current
    fib_list.append(next)
    prev=current
    current=next
  return fib_list
x=fibonnaci()
print(x)