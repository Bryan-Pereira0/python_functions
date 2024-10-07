#task123
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return ("You cannot divide by 0.")
    return a / b
def calculator():
    print("Select how you want to calculate: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        calculate = input("Enter the number of how you wish to calculate (1,2,3,4): ")
        
        if calculate in ["1", "2", "3", "4"]:
            a1 = input("Enter your first number: ")
            b1 = input("Enter your second number: ")
            
            if not(float(a1) and float(b1)):
                print("Numbers only")
                continue
            
            a1 = float(a1)
            b1 = float(b1)
            
            if calculate == "1":
                print(f"{a1}+{b1} = {add(a1,b1)}")
            elif calculate == "2":
                print(f"{a1}-{b1} = {subtract(a1,b1)}")
            elif calculate == "3":
                print(f"{a1}*{b1} = {multiply(a1,b1)}")
            elif calculate == "4":
                print(f"{a1}/{b1} = {divide(a1,b1)}")
        else:
            print("You can't do that.")
        calculate_again = input("Do another calculation?: y/n: ")
        if calculate_again != 'y':
            break
calculator()   
                