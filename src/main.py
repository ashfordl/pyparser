import pyparser

def main():
    expression = input("Enter expression: ")

    pyparser.parse(expression)

# Run the application
if __name__ == "__main__":
    main()
