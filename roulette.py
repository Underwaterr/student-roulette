import random

students = []

answer = 'y'

# Create the file if it does not exist
with open('student-cache.csv', 'w+') as file:
    students = file.read().splitlines()

    # If file is empty, pull from primary list
    if len(students) == 0:
        with open('students.csv') as file:
            students = file.read().splitlines()


while len(students) > 0:

    # Shuffle students each loop
    random.shuffle(students)

    # `answer` will always be 'y' the first time
    if answer == 'y' or answer == 'yes':
        input("Your next presenter is...")
        next_student = students.pop()
        input(next_student + "!")

        # Remove student name from file
        with open('student-cache.csv', 'w') as file:
            for line in students:
                if line.strip('\n') != next_student:
                    file.write(line+'\n')

        # Ask before repeating
        answer = input("Pull another name? ")

    else:
        break
