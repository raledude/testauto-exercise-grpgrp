import math

def multiplication():
    pass

def addition():
    pass

def subtraction():
    pass

def division():
    pass

def square_root():
    x = int(input("Type a number you want to know the square root of"))
    result = math.sqrt(x)
    print(result)

while True:
    print("[1] X")
    print("[2] -")
    print("[3] +")
    print("[4] /")
    print("[5] √")

    choice = input("What do you want to do?")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        square_root()
    else:
        print("Invalid choice")

