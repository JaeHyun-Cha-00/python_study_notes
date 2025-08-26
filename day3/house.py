# name = input("What's your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Darco":
#     print("Slytherin")
# else:
#     print("Who?")

name = input("What's your name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")