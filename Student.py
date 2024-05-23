class Student:
    def __init__(self, name, roll_number, subjects):
        self.name = name
        self.roll_number = roll_number
        self.subjects = subjects
        self.marks = {subject: None for subject in subjects}

    def input_marks(self):
        for subject in self.subjects:
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject}: "))
                    if 0 <= mark <= 100:
                        self.marks[subject] = mark
                        break
                    else:
                        print("Please enter a mark between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def display_marks(self):
        print("\nMarks:")
        for subject, mark in self.marks.items():
            if mark is not None:
                grade, grade_point, remarks = self.get_grade(mark)
                print(f"{subject}: {mark} - Grade: {grade}, Grade Point: {grade_point}, Remarks: {remarks}")
            else:
                print(f"{subject}: No marks entered")

    def calculate_percentage(self):
        if all(mark is not None for mark in self.marks.values()):
            total_marks = sum(self.marks.values())
            percentage = (total_marks / (len(self.subjects) * 100)) * 100
            return percentage
        else:
            print("Marks for all subjects have not been entered.")
            return None

    def calculate_cgpa(self):
        if all(mark is not None for mark in self.marks.values()):
            total_grade_points = sum(self.get_grade(mark)[1] for mark in self.marks.values())
            cgpa = total_grade_points / len(self.subjects)
            return cgpa
        else:
            print("Marks for all subjects have not been entered.")
            return None

    def get_grade(self, mark):
        if 80 <= mark <= 100:
            return 'A+', 4.00, 'Outstanding'
        elif 75 <= mark < 80:
            return 'A', 3.75, 'Excellent'
        elif 70 <= mark < 75:
            return 'A-', 3.50, 'Very Good'
        elif 65 <= mark < 70:
            return 'B+', 3.25, 'Good'
        elif 60 <= mark < 65:
            return 'B', 3.00, 'Satisfactory'
        elif 55 <= mark < 60:
            return 'B-', 2.75, 'Above Average'
        elif 50 <= mark < 55:
            return 'C+', 2.50, 'Average'
        elif 45 <= mark < 50:
            return 'C', 2.25, 'Below Average'
        elif 40 <= mark < 45:
            return 'D', 2.00, 'Pass'
        else:
            return 'F', 0.00, 'Fail'


def main():
    name = input("Enter student's name: ")
    roll_number = int(input("Enter student's roll number: "))
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = [input(f"Enter subject {i + 1}: ") for i in range(num_subjects)]

    student = Student(name, roll_number, subjects)

    while True:
        print("\n---- Student Management System -----")
        print("1. Input Marks")
        print("2. Display Marks")
        print("3. Calculate Percentage")
        print("4. Calculate CGPA")
        print("5. All Information")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student.input_marks()
        elif choice == '2':
            student.display_marks()
        elif choice == '3':
            percentage = student.calculate_percentage()
            if percentage is not None:
                print(f"Percentage: {percentage:.2f}%")
        elif choice == '4':
            cgpa = student.calculate_cgpa()
            if cgpa is not None:
                print(f"CGPA: {cgpa:.2f}")
        elif choice == '5':
            student.display_marks()
            percentage = student.calculate_percentage()
            if percentage is not None:
                print(f"Percentage: {percentage:.2f}%")
            cgpa = student.calculate_cgpa()
            if cgpa is not None:
                print(f"CGPA: {cgpa:.2f}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
