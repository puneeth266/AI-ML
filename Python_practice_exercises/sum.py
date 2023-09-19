import sys

if len(sys.argv) != 3:
    print("Usage: python sum.py <integer1> <integer2>")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please provide two valid integers as command-line arguments.")
