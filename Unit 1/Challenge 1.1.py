def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x - 1)


num = int(input("Enter a number:"))
print("The factorial of", num, "is", fact(num))
