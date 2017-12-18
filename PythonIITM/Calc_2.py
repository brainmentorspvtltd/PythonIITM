def add(x,y):
    result = x + y
    print("Addition",result)

def sub(x,y):
    result = x - y
    print("Subtraction",result)

def div(x,y):
    result = x/y
    print("Divison",result)

def mul(x,y):
    result = x * y
    print("Multiplication",result)

while True:

    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    result = 0


    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
        }

    todo.get(userChoice)(num_1, num_2)




    
