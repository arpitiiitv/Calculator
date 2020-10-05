print("\n")


# welcome note
print("Welcome In Python Calculator")
print("\n")


# user input his first value
n1 = float(input("Please Enter Your First Value: "))


# user input his second value
n2 = float(input("Please Enter Your Second Value: "))
print("\n")


# operation slection
print("Operation Types")
print("\n")


# operation types
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Quotient")
print(" 6. Reminder")
print("\n")


# operator selection 
operator= int(input("Please Slect Anyone Opeartion From Above Options: "))


# for result 
result = 0
print("\n")


# using if else condition for addition 
if operator == 1:
  result = n1+n2
  print(f"Your Result Of Your Both Addition Values Is: {result}")


# using if else condition for subtraction 
elif operator == 2:
  result = n1-n2
  print(f"Your Result Of Your Both Subtraction Values Is: {result}")


# using if else condition for multiplicatio 
elif operator == 3:
  result = n1*n2
  print(f"Your Result Of our Both Multiplication Values Is: {result}")


# using if else condition for division
elif operator == 4:
  result = n1/n2
  print(f"Your Result Of Your Both Division Values Is: {result}")



# using  if else condition for reminder
elif operator == 5:
  result = float(n1) % float(n2)
  print(f"Your Result Of Your Reminder Is: {result}")



# using if else condition for quotient
elif operator == 6:
  result = float(n1) // float(n2)
  print(f"Your Result Of Your Quotient Values Is: {result}")


# end of using if else condition 
else:
    print("You Have Entered An Invalid Operation")
print("\n")
