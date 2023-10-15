# This function adds two numbers
def add(x, y):
   return x + y 

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function modulus two numbers
def modulus(x, y):
    return x % y

# This function exponentialize two numbers
def exponentation(x, y):
    return(x ** y)

# This function floor divide two numbers
def floordivide(x, y):
    return(x // y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Exponentialize")
print("7.Floor divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6','7'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1': 
                round(print(num1, "+", num2, "=", (add(num1, num2))), 2)

        elif choice == '2':
            round(print(num1, "-", num2, "=", subtract(num1, num2)), 2)

        elif choice == '3':
            round(print(num1, "*", num2, "=", multiply(num1, num2)), 2)

        elif choice == '4':
            try:
                round(print(num1, "/", num2, "=", divide(num1, num2)), 2)
            except ZeroDivisionError:
                print("Can't divide 0")
                
        elif choice == '5':
            round(print(num1, "%", num2, "=", modulus(num1, num2)), 2)

        elif choice == '6':
            round(print(num1, "**", num2, "=", exponentation(num1, num2)), 2)

        elif choice == '7':
            round(print(num1, "//", num2, "=", floordivide(num1, num2)), 2)
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        else:
            print("Invalid Input. Returning to start")
    else:
        print("Invalid Input")