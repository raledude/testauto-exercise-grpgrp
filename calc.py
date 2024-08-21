def multiplication():
    pass

def addition():
    pass

def subtraction():
    pass


def division():
    x = int(input("Skriv in den första siffran: "))
    y = int(input("Skriv in den andra siffran: "))
    if y != 0:
        result = x / y
        print("Resultat:", result)
    else:
        print("Fel: Division med noll är inte tillåtet.")

def square_root():
    pass


while True:
    print("[1] X")
    print("[2] -")
    print("[3] +")
    print("[4] /")

    choice = input("What do you want to do?")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        division()
    else:
        print("Invalid choice")
