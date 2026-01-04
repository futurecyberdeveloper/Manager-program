# Base class for all people in school
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name} | Age : {self.age}")


# Access class (role in school)
class SchoolAccess(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def show_role(self):
        print(f"===== Role Information =====")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Role : {self.role}")
        print(f"============================")


# Student class
class Student(SchoolAccess):
    def __init__(self, name, age, role, score):
        super().__init__(name, age, role)
        self.score = score

    def add_score(self, amount):
        if self.score + amount > 100:
            print("Adding this amount will exceed the maximum score (100)")
        else:
            self.score += amount
            print("Score added successfully")
            print(f"Current score of {self.name}: {self.score}")


# Show student list with number
def show_number_list(data):
    print("======= Student Number List =======")
    for k, v in data.items():
        print(f"No: {k} | Name: {v.name}")
    print("===================================")


# Add score to selected student
def add_student_score(data):
    while True:
        show_number_list(data)

        choice = input("Enter student number to add score (q to quit): ")

        if choice.lower() == "q":
            break
        elif not choice.isdigit():
            print("Input must be a number!")
            continue

        choice = int(choice)
        student = data.get(choice)

        if student is not None:
            while True:
                print(f"Initial score of {student.name}: {student.score}")
                amount = input("Enter score to add (q to quit): ")

                if amount.lower() == "q":
                    break
                elif not amount.isdigit():
                    print("Input must be a number!")
                    continue

                student.add_score(int(amount))
        else:
            print("Invalid student number!")


# Show role of selected person
def show_person_role(data):
    while True:
        show_number_list(data)

        choice = input("Enter number to view role (q to quit): ")

        if choice.lower() == "q":
            break
        elif not choice.isdigit():
            print("Input must be a number!")
            continue

        choice = int(choice)
        person = data.get(choice)

        if person is not None:
            person.show_role()
        else:
            print("No data found for that number!")


# Show all data
def show_all_data(data):
    print("================== All Student Data ==================")
    for k, v in data.items():
        print(
            f"No: {k} | Name: {v.name} | Age: {v.age} | Role: {v.role} | Score: {v.score}"
        )
    print("=======================================================")


# Main function
def main():
    s1 = Student("Rusdi", 20, "student", 100)
    s2 = Student("Murti", 19, "student", 85)
    s3 = Student("Yarto", 26, "student", 70)
    s4 = Student("Joko", 30, "student", 85)
    s5 = Student("Edi", 35, "student", 65)

    data = {
        1: s1,
        2: s2,
        3: s3,
        4: s4,
        5: s5,
    }

    while True:
        print("====================================")
        print("1. Show all data")
        print("2. Add student score")
        print("3. Show role")
        print("4. Exit")

        choice = input("Choose: ")

        if not choice.isdigit():
            print("Choice must be a number!")
            continue

        choice = int(choice)

        if choice == 1:
            show_all_data(data)
        elif choice == 2:
            add_student_score(data)
        elif choice == 3:
            show_person_role(data)
        elif choice == 4:
            break
        else:
            print("Invalid menu option!")

    print("Program exited.")


if __name__ == "__main__":
    main()

#.🧠 HOW IT WORKS (STEP BY STEP)

#1.Program starts from main()
#2.Objects are created from classes
#3.Data is stored inside a dictionary
#4.Menu is shown to the user
#5.User chooses an option
#6.Program runs the selected function
#7.Data is updated inside the objects
#8.Program loops until exit