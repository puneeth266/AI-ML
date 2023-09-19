import sys

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <expression>")
    else:
        expression = sys.argv[1]
        result = calculator(expression)
        print(f"Result: {result}")
