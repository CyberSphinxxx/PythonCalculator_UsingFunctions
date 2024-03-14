def separator():
    print("---------------------------")

def addition(num1, num2):
    result = num1 + num2
    print(result)

def division(num1, num2):
    result = num1 / num2
    print(result)

def multiplication(num1, num2):
    result = num1 * num2
    print(result)

def subtraction(num1, num2):
    result = num1 - num2
    print(result)

valid_math_modes = {"+", "-", "/", "*"}

while True:
    separator()
    math_mode = input('Enter Math Mode: ')
    if math_mode in valid_math_modes:
        separator()
        print(f"Math Mode is: {math_mode}")

        while True:
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        if math_mode == '+':
            addition(num1, num2)

        elif math_mode == '-':
            subtraction(num1, num2)

        elif math_mode == '*':
            multiplication(num1, num2)

        elif math_mode == '/':
            division(num1, num2)

        separator()
        while True:
            calculate_again = input("Do you want to calculate again? y/n?: ")
            if calculate_again == 'y':
                break

            elif calculate_again == 'n':
                break

            else:
                separator()
                print("Invalid Choice, only 'y' for YES and 'n' for NO")
        if calculate_again == 'n':
            break

        else:
            separator()
            print("Invalid Math Mode!")
            print("Please Choose: + - * /")
