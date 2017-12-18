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

    if userChoice == "1":
        result = num_1 + num_2
        print("Result is",result)
    elif userChoice == "2":
        result = num_1 - num_2
        print("Result is",result)
    elif userChoice == "3":
        result = num_1 / num_2
        print("Result is",result)
    elif userChoice == "4":
        result = num_1 * num_2
        print("Result is",result)
    else:
        print("Wrong Choice")
    








