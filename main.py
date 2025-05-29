class Student:
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")

        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor_roll = "NO"
        self.letter_grade = "F"

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print(f"Invalid grade '{grade}': must be a number.")
            return
        if grade < 0 or grade > 100:
            print(f"Invalid grade '{grade}': must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calc_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        avg = self.calc_average()
        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

    def determine_pass_fail(self):
        self.is_passed = "Passed" if self.calc_average() >= 60 else "Failed"

    def check_honor_roll(self):
        self.honor_roll = "YES" if self.calc_average() >= 90 else "NO"

    def remove_grade_by_index(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Invalid index {index}. Cannot remove grade.")

    def remove_grade_by_value(self, value):
        if value in self.grades:
            self.grades.remove(value)
        else:
            print(f"Grade value {value} not found.")

    def update_status(self):
        self.determine_letter_grade()
        self.determine_pass_fail()
        self.check_honor_roll()

    def generate_summary(self):
        self.update_status()
        print("--- Student Summary Report ---")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {self.calc_average():.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {self.is_passed}")
        print(f"Honor Roll: {self.honor_roll}")


def start_run():
    try:
        student_obj = Student("001", "Alice")
    except ValueError as e:
        print(e)
        return

    student_obj.add_grade(95)
    student_obj.add_grade(85.5)
    student_obj.add_grade(70)
    student_obj.add_grade("bad input")  # Invalid input
    student_obj.add_grade(101)           # Invalid input
    student_obj.remove_grade_by_index(5)  # Out of bounds
    student_obj.remove_grade_by_value(99) # Not found

    student_obj.generate_summary()

start_run()
