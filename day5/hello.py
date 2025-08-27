def get_int():
    try:
        x = int(input("What's x? "))
    except ValueError:
        pass
    else:
        print(f"x is {x}")

get_int()