def multiplication():
    y = int(input("Type any number: "))
    x = int(input("Type in the number you want to multiply it with: "))
    result = y * x
    print(f"This is your number: {result} \n")
    
def addition():
    pass

def subtraction():
    pass

def division():
    pass

def square_root():
    pass


while True:
    print("[1] X")
    print("[2] -")
    print("[3] +")
    print("[4] /")


    choice = input("What do you want to do?")

    if choice == "1":
        multiplication()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    else:
        print("Invalid choice")

