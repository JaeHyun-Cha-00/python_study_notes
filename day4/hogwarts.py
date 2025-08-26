# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])


# students = {"Hermione": "Gyr", 
#             "Harry": "Gyr", 
#             "Ron": "Gyr",
#             "Draco": "Sly"
# }

# print(students["Hermione"])


students = [
    {"name": "Hermione", "house": "Gry", "patronus": "None"}
]

for student in students:
    print(student["name"], student["house"], sep=", ")