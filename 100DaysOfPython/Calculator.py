from Calculator_art import logo


def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

operations = {'+': add,
             '-': subtract,
             '*': multiply,
             '/': divide}

def calculator():
  print(logo)
  calc = True
  first = float(input("What is the first number? "))
  while calc:
    next = float(input("What is the next number? "))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation. ")
    function = operations[operation_symbol]
    answer = function(first, next)
    print(f"{first} {operation_symbol} {next} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation.: ") == 'y':
      first = answer
    else:
      calc = False
      calculator()

calculator()