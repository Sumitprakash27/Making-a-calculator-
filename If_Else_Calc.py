def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Not Defined"
    else: 
        return x/y

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Choose:(1/2/3/4/5) = ")
    if choice in ("1", "2", "3", "4"):
        A = float(input("Enter number = "))
        B = float(input("Enter number = "))
        
        if choice == "1":
            print("ANS 👉 ", add(A,B) , "👈")
        elif choice =="2":
            print("ANS 👉 ", subtract(A,B), "👈")
        elif choice == "3":
            print("ANS 👉 ", multiply(A,B), "👈")
        elif choice == "4":
            print("ANS 👉 " , divide(A,B), "👈")
    elif choice == "5":
        print("Exitting ... \n Thanks for using calculator")
        break
    else:
        print("Error! Input a correct option.")