#building a calculator

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

print("(1) Add")
print("(2) Substract")
print("(3) Multiply")
print("(4) Divide")
operation = input("Which operation do you want to choose?")

if operation in ("1", "2", "3", "4"):
    if operation == "1": 
       print("x + y = ", add(3,2)) 

    if operation == "2": 
       print("x - y = ", substract(3,2)) 

    if operation == "3": 
       print("x * y = ", multiply(3,2)) 

    if operation == "4": 
       print("x / y = ", divide(3,2)) 

else:
    raise "Not in the scope of operations"
