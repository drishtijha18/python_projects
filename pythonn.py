# PYTHON CALCULATOR

print("Choose a number:")
print("(1) - Add")
print("(2) - Subtract")
print("(3) - Multiply")
print("(4) - Divide")

question = int(input("Choose a sign: "))  # variable name fixed here

result = 0

if question in [1, 2, 3, 4]:  
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: ")) 

    if question == 1:
        result = num1 + num2
    elif question == 2:
        result = num1 - num2
    elif question == 3:
        result = num1 * num2
    elif question == 4:
        if num2 == 0:  # Handling division by zero
            print("Error: Cannot divide by zero.")
            exit()
        result = num1 // num2  # ealing with Integer thatswhy

    print(f"The result of the operation is {result}.")  
else:
    print("Invalid operation entered.") 

