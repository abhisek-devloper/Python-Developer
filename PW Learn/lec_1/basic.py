'''basic - python
-> variable,keyword, comments, operator,data type
-> input and output
-> function
-> control statement
-> loops'''

# example calculator
# Basic Python calculator example

def get_input():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("+", "-", "*", "/", "%", "**", "//")
    c = input("Choose Operation: ")

    return a, b, c

def calculate(a: int, b: int, c: str):
    if c == "+":
        print(f"Result: {a + b}")
    elif c == "-":
        print(f"Result: {a - b}")
    elif c == "*":
        print(f"Result: {a * b}")
    elif c == "/":
        print(f"Result: {a / b}")
    elif c == "%":
        print(f"Result: {a % b}")
    elif c == "**":
        print(f"Result: {a ** b}")
    elif c == "//":
        print(f"Result: {a // b}")
    else:
        print("Invalid operation🤔")

if __name__ == "__main__":
    a, b, c = get_input()
    calculate(a, b, c)

