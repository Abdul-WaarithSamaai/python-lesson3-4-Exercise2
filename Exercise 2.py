x = 5
y = 3
x = (x + 3 )
y = ( y * 2 )
result = x/y
print(result)

a = 20
b = 10
c = 5
condition1 = a > b 
condition2 = b == 0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)
print(final_condition)

score = int(input ("test scores"))
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70: 
  print("C")
elif score >= 60:  
  print("D")
else:
  print("F")

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
operation = input("enter an operation(+,-, *, /);")
if operation == "+":
  result = num1 + num2
  print("result:", result)
elif operation == "-":
  result = num1 - num2
  print("result:", result)  
elif operation == "*":
  result = num1 * num2
  print("result", result)
elif operation == "/":
  result = num1 / num2
  print("result:", result)
  if num2 == 0:  
    print("error: divisiion by zero not allowed.")
  else:
    result = num1 / num2
    print("result:", result)
else:
  print("invalid operation entered.")


