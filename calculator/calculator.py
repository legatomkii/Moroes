import sys

def add(x, y):
  return x + y

if len(sys.argv) != 3:
    print("Error: Provide two numbers as arguments.")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(add(num1, num2))
    except ValueError:
        print("Error: Invalid input. Please provide numbers.")
