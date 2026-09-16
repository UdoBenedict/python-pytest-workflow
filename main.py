from src.calculator import add, multiply

def main():
    print("Enter two numbers:")
    x = float(input("First number: "))
    y = float(input("Second number: "))

    print(f"Sum: {add(x, y)}")
    print(f"Product: {multiply(x, y)}")

if __name__ == "__main__":
    main()