def calculate(operation, number1, number2):
  if operation == "add":
    result = number1 + number2  #or simply just return number1 + number2
    return result
  elif operation == "subtract":
    result = number1 - number2
    return result
  elif operation == "multiply":
    result = number1 * number2
    return result
  elif operation == "divide":
    if number2 == 0:
      return "Cannot divide by zero"
    else:
      result = number1 / number2
      return result
  else:
    print("Select a valid operation")

chosen_operation = input("Enter the operation (add, subtact, multiply, divide): ").lower() #.lower() is a method that will force the user to type in lower cases as Python is case sensitive
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result1 = calculate(chosen_operation, num1, num2)

print("The result is:", result1)