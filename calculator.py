a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))

x = int(input("""
1. Enter 1 for add
2. Enter 2 for Sub
3. Enter 3 for Div
4. Enter 4 for Mul\n
"""))

match x:

    case 1:
        c = a + b
        print ("Add is: ", c)

    case 2:
        c = a - b
        print ("Sub is: ", c)

    case 3:
        
        if b == 0:
            print("Div is: Infinite")
        else:
            c = a / b
            print ("Div is: ", c)
            
    case 4:
        c = a * b
        print ("Mul is: ", c)
    case _:
        print("Enter the correct option")