from art import logo

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

# dictionary with operators as keys and function as value 
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  # prompt the user for inputs
  num1 = float(input("Enter the first value: "))
  for symbol in operations:
    print(symbol)

  more_math = True

  while more_math:
    operator = input("Enter the operation you would like to use: ")
    num2 = float(input("Enter the next value: "))

    # get the operator
    calc_function = operations[operator]

    # calculate and print the answer
    total = calc_function(num1, num2)
    print(f"{num1}{operator}{num2} is {total}")  

    do_more_math = input(f"Do you want to continue doing math with {total}? ")
    if do_more_math == "yes":
      num1 = total
    else:
      more_math = False
      calculator() # this is recursion, the fuction is calling itself

calculator()
